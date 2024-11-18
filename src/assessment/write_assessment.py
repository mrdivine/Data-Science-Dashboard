from pydantic import BaseModel, Field, ValidationError
from typing import List
from langchain_openai import ChatOpenAI
from pathlib import Path
from config import Config
import json


class RequirementEvaluation(BaseModel):
    """Captures evaluation details for job profile requirements."""
    requirement_name: str = Field(description="The name of the requirement (e.g., 'Project Management in Pharma') in the appropriate language")
    requirement_type: str = Field(description="Type of requirement: essential or desirable in the language of the job profile")
    related_experience: str = Field(description="Summary of the candidate's relevant experience in the language of the job profile")
    examples: List[str] = Field(description="List of specific projects that match the requirement in the language of the job profile")
    self_assessment_score: float = Field(description="Self-assessment score from 1-10 in the language of the job profile")
    rationale: str = Field(description="Rationale for the self-assessment score in the language of the job profile")


class RequirementsAssessment(BaseModel):
    """Structured output for job profile requirements assessment."""
    job_profile_language: str = Field(description="Language of the job profile typically either English or German")
    job_profile_title: str = Field(description="The Job Profile Title given or one that is descriptive of the job profile in the language of the job profile")
    requirement_evaluations: List[RequirementEvaluation] = Field(description="List of all requirements and candidate assessments in the language of the job profile")


prompt_template = """
You are creating an application for a freelance position based on the provided job profile and projects list of the candidate. 
You should assess the language of the job profile, and respond in that language, please. Sometimes the language can be mixed so pick the language most frequenlty used in the job profile READ THE WHOLE JOB PROFILE AND THEN DECIDE!! Thanks.
### Job Profile Requirements Assessment
Evaluate the candidate's compatibility for each requirement in the job profile. Identify relevant experience, match specific projects to requirements, and assess the requirements to the given job profile for applicability on a scale of 1-10. Format the output as follows:
You must validate the experience of the candidate by adding an example of their experience. Try to make 2-3 examples of their experience. Do not assume that the candidate has worked with a technology unless explicity stated in the candidate's project list.

- ** <Long Requirement Name> <Requirement Type>**
- ** <short Requirement Name> <Requirement Type>
    - **Related Experience**: Summarize relevant experience based on the project list, focusing on projects directly related to the requirement.
    - **Examples**:
        1. **Project 1**: Project title and context, detailing why it matches the requirement.
        2. **Project 2**: Additional examples as applicable.
    - **Self-Assessment**: X/10
    - **Rationale**: Justify the score based on specific experience, industry relevance, or any identified areas for potential development.

Make sure to have at least 5-8 requirements and even up to 10, but no more.

### Job Profile
{job_profile}

### candidate's Project List
{projects_list}
"""


class JobProfileBotTool:
    """Handles job profile evaluation and output generation"""

    def __init__(self, job_profile_text: str):
        self.config = Config(job_profile_text=job_profile_text)

        self.llm = ChatOpenAI()  # Initialize the LLM instance

    def generate_prompt(self) -> str:
        """Generate the prompt template"""
        return prompt_template.format(job_profile=Path(self.config["job_profile_file"]).read_text(),
                                      projects_list=Path(self.config["candidate_projects_list_file"]).read_text())

    def execute_llm_and_save(self):
        """Executes LLM with structured output and saves it"""
        prompt = self.generate_prompt()
        structured_llm = self.llm.with_structured_output(RequirementsAssessment)
        attempts, max_attempts = 0, 2

        while attempts < max_attempts:
            try:
                structured_output = structured_llm.invoke(prompt)

                break  # Exit if successful
            except ValidationError:
                attempts += 1
                if attempts == max_attempts:
                    raise Exception("Failed to get structured output from LLM after retries.")

        # Save output data
        self.save_output(structured_output)

    def save_output(self, structured_output: RequirementsAssessment):
        """Save structured output directly to a JSON file."""
        # Convert the structured output to a dictionary format for JSON
        requirements_data = [evaluation.dict() for evaluation in structured_output.requirement_evaluations]
        json_file_path = self.config["requirements_assessment_file"]

        with open(json_file_path, "w") as json_file:
            json.dump(requirements_data, json_file, indent=4)
        print(f"Data saved to {json_file_path}")

        self.config["profile_title"] = structured_output.job_profile_title
        self.config["job_profile_language"] = structured_output.job_profile_language

    def run(self):
        """Main method to execute tool"""
        self.execute_llm_and_save()


print("Here we go...")


