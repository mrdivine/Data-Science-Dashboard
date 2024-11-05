from pydantic import BaseModel, Field, ValidationError
from typing import List
from langchain_openai import ChatOpenAI
from pathlib import Path
from config import Config
import json


class RequirementEvaluation(BaseModel):
    """Captures evaluation details for job profile requirements."""
    requirement_name: str = Field(description="The name of the requirement (e.g., 'Project Management in Pharma')")
    requirement_type: str = Field(description="Type of requirement: essential or desirable")
    related_experience: str = Field(description="Summary of the candidate's relevant experience")
    examples: List[str] = Field(description="List of specific projects that match the requirement")
    self_assessment_score: float = Field(description="Self-assessment score from 1-10")
    rationale: str = Field(description="Rationale for the self-assessment score")


class RequirementsAssessment(BaseModel):
    """Structured output for job profile requirements assessment."""
    requirement_evaluations: List[RequirementEvaluation] = Field(description="List of all requirements and candidate assessments")


prompt_template = """
You are creating an application for a freelance position based on the provided job profile and projects list of the candidate. 

### Job Profile Requirements Assessment
Evaluate the candidate's compatibility for each requirement in the job profile. Identify relevant experience, match specific projects to requirements, and assess the requirements to the given job profile for applicability on a scale of 1-10. Format the output as follows:

- ** <Long Requirement Name> <Requirement Type>**
- ** <short Requirement Name> <Requirement Type>
    - **Related Experience**: Summarize relevant experience based on the project list, focusing on projects directly related to the requirement.
    - **Examples**:
        1. **Project 1**: Project title and context, detailing why it matches the requirement.
        2. **Project 2**: Additional examples as applicable.
    - **Self-Assessment**: X/10
    - **Rationale**: Justify the score based on specific experience, industry relevance, or any identified areas for potential development.

### Job Profile
{job_profile}

### Candidate's Project List
{projects_list}
"""


class JobProfileBotTool:
    """Handles job profile evaluation and output generation"""

    def __init__(self, job_profile_title: str, job_profile_text: str):
        self.config = Config(profile_title=job_profile_title, job_profile_text=job_profile_text)

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

        # Define the JSON file path
        json_file_path = Path(self.config["requirements_assessment_file"])

        # Save the JSON data
        with open(json_file_path, "w") as json_file:
            json.dump(requirements_data, json_file, indent=4)
        print(f"Data saved to {json_file_path}")

    def run(self):
        """Main method to execute tool"""
        self.execute_llm_and_save()


print("Here we go...")

if __name__ == "__main__":

    business_analyst_job_profile_title = "Business Analyst"
    config = Config(profile_title=business_analyst_job_profile_title)
    bot_tool = JobProfileBotTool(job_profile_title=config["profile_title"],
                                 job_profile_text=Path(config["job_profile_file"]).read_text())
    bot_tool.run()
