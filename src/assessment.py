from pydantic import BaseModel, Field, ValidationError
from typing import List
from langchain_openai import ChatOpenAI
import pandas as pd
from pathlib import Path
from config import Config


class Skill(BaseModel):
    """Represents a skill, proficiency level, and summary of relevant experience."""
    skill_type: str = Field(description="Type of the skill: 'hard' or 'soft'")
    skill_name: str = Field(description="Name of the skill")
    rating: float = Field(description="Importance or proficiency score from 0-10")
    relevant_experience: str = Field(description="Summary of experience for this skill")


class RequirementsAssessment(BaseModel):
    """Captures self-assessment scores and relevant experience for job requirements."""
    requirement_name: str = Field(description="The name or type of requirement (e.g., 'Project Management')")
    self_assessment_score: float = Field(description="Self-assessment score from 0-10")
    related_experience: List[str] = Field(description="List of related experiences from projects or roles")
    rationale: str = Field(description="Rationale for the self-assessment score")


class SkillsAssessment(BaseModel):
    """Structured output for skills and requirements in the assessment."""
    job_profile_skills: List[Skill] = Field(description="Skills required by the job profile, rated by importance")
    candidate_skills: List[Skill] = Field(description="Candidate's skills, rated by proficiency")
    requirements_assessment: List[RequirementsAssessment] = Field(description="Self-assessment of job requirements")


prompt_template = """
You are tasked with evaluating a candidate's project experience in alignment with a given job profile and crafting a customized cover letter to highlight this fit.

The job profile and project list are provided as follows:

Job Profile:
{job_profile}

Candidate's Project List:
{project_list}

**Instructions**:

1. **Identify the Role and Skills in the Job Profile**:
    - Identify **hard and soft skills** required in the job. 
    - For each skill, provide:
      - `Skill Type`: 'hard' or 'soft'
      - `Skill Name`
      - `Importance Rating`: Rate the criticality of this skill to the job (1-10)
      - `Relevant Experience`: Summarize why this skill is essential to the role

2. **Candidate's Skills and Alignment with the Job Profile**:
    - Review the candidate's project list to identify relevant **hard and soft skills** they have demonstrated.
    - For each skill, provide:
      - `Skill Type`: 'hard' or 'soft'
      - `Skill Name`
      - `Proficiency Rating`: Rate the candidate’s proficiency level for this skill (1-10)
      - `Relevant Experience`: Summarize specific experience or projects where the candidate demonstrated this skill, referring to specific projects in the list.

3. **Self-Assessment for Job Requirements**:
    - Analyze each requirement outlined in the job profile, comparing it to examples from the candidate's experience.
    - For each requirement, provide:
      - `Requirement Name`: Name or type of the requirement (e.g., "Project Management in Pharma")
      - `Self-Assessment Score`: Rate how well the candidate’s experience meets this requirement (1-10)
      - `Related Experience`: Identify specific projects or roles where the candidate addressed this requirement
      - `Rationale`: Explain the self-assessment score, noting any industry differences or other gaps. If no direct experience exists, provide a reasoned comparison with relevant experience in other regulated fields, like **pharma**.


**Expected Output Structure**:

1. **Job Profile Hard and Soft Skills**:
   - `Skill Type`: 'hard' or 'soft'
   - `Skill Name`
   - `Importance Rating`: 1-10
   - `Relevant Experience`

2. **Candidate's Hard and Soft Skills**:
   - `Skill Type`: 'hard' or 'soft'
   - `Skill Name`
   - `Proficiency Rating`: 1-10
   - `Relevant Experience`

3. **Self-Assessment of Requirements**:
   - `Requirement Name`
   - `Self-Assessment Score`: 1-10
   - `Related Experience`
   - `Rationale`

    """


class JobProfileBotTool:
    """Handles job profile evaluation and output generation"""

    def __init__(self, job_profile_title: str, job_profile_text: str):
        self.config = Config(profile_title=job_profile_title, job_profile_text=job_profile_text)

        self.llm = ChatOpenAI()  # Initialize the LLM instance

    def generate_prompt(self) -> str:
        """Generate the prompt template"""
        return prompt_template.format(job_profile=Path(self.config["job_profile_file"]).read_text(),
                                      project_list=Path(self.config["candidate_projects_list_file"]).read_text())

    def execute_llm_and_save(self):
        """Executes LLM with structured output and saves it"""
        prompt = self.generate_prompt()
        structured_llm = self.llm.with_structured_output(SkillsAssessment)
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

    def save_output(self, structured_output: SkillsAssessment):
        """Save structured output to files"""

        def save_csv(filename, data):
            pd.DataFrame([item.dict() for item in data]).to_csv(filename, index=False)

        save_csv(
            self.config["job_profile_skills_file"], structured_output.job_profile_skills)
        save_csv(
            self.config["candidate_skills_file"], structured_output.candidate_skills)
        save_csv(
            self.config["requirements_assessment_file"], structured_output.requirements_assessment)

    def run(self):
        """Main method to execute tool"""
        self.execute_llm_and_save()


print("Here we go...")

if __name__ == "__main__":
    job_profile_path = "assets/docs/input/Business Analyst/business_analyst_job_profile.md"
    nlp_job_profile_text = Path(job_profile_path).read_text()

    nlp_job_profile_title = "Business Analyst"

    bot_tool = JobProfileBotTool(job_profile_title=nlp_job_profile_title, job_profile_text=nlp_job_profile_text)
    bot_tool.run()
