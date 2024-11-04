from config import Config
from langchain_openai import ChatOpenAI
from pydantic import ValidationError
from pydantic import BaseModel, Field
import os
from config import Config
from utils import read_csv_as_string, parse_executive_summary, save_to_file, save_csv


class CoverLetterOutput(BaseModel):
    """Represents the generated cover letter as a single text field."""
    cover_letter: str = Field(description="The content of the cover letter generated for the job application.")


class CoverLetterBotTool:
    """Generates a cover letter by combining job profile, projects, and executive summary."""

    def __init__(self, profile_title: str):
        self.config = Config(profile_title)
        self.llm = ChatOpenAI()

    def load_job_profile_skills(self) -> str:
        """Read job profile skills CSV file as a string for prompt injection."""
        job_profile_skills_file = self.config.get("job_profile_skills_file")
        if job_profile_skills_file:
            return read_csv_as_string(self.config["job_profile_skills_file"])
        raise FileNotFoundError("Job profile skills file path is missing in config.")

    def load_candidate_skills(self) -> str:
        """Read candidate skills CSV file as a string for prompt injection."""
        candidate_skills_file = self.config["candidate_skills_file"]
        if candidate_skills_file:
            return read_csv_as_string(self.config["candidate_skills_file"])
        raise FileNotFoundError("Candidate skills file path is missing in config.")

    def load_job_profile_title(self) -> str:
        """Read the job profile title from the config file as a string for prompt injection."""
        job_profile_title = self.config["profile_title"]
        if job_profile_title:
            return job_profile_title
        raise FileNotFoundError("Job profile title missing in config.")

    def load_executive_summary(self) -> str:
        executive_summary = parse_executive_summary(self.config["candidate_projects_list_file"])
        if executive_summary:
            return executive_summary
        raise FileNotFoundError("Executive summary file path is missing in config.")

    def generate_prompt(self) -> str:
        """Generate the cover letter prompt using job profile and executive summary."""

        return f"""
        You are tasked with generating a personalized cover letter for a candidate, objectively evaluating their fit for the job role based on provided data.

        Use the following Job Profile Title to write in the cover letter:
        {self.load_job_profile_title()}
        
        For inspiration and understanding of the Candidates Executive Summary:
        {self.load_executive_summary()}

        The objective Candidate's Skills Assessment on which to base your analysis :
        {self.load_candidate_skills()}
        
        The Objective Job Profile Skills Assessment on which to base your analysis:
        {self.load_job_profile_skills()}

        **Instructions**:
        - Make a bridge between the job profile skills and the candidate skills.
        - Make a convingin argument why the candidate maybe qualified, overqualified, or under-qualified.
        - Begin with an **objective overview** of the candidate’s fit for the role, listing key matching skills and experiences.
        - Highlight specific **relevant projects** and how they align with the job's requirements.
        - **Note any gaps** and propose how other skills may compensate.
        - End with a **polished closing** that conveys enthusiasm for the role.


        **Expected Output**:
        A single cover letter that objectively highlights the candidate's strengths, identifies areas of partial fit, and emphasizes complementary skills.
        written in markdown. You should have an Objective Overview, Relevant Projects, Addressing Gaps, and Polished Closing as part of the cover letter.
        close the letter with just "Sincerley",
        """

    def execute_llm_and_save(self):
        """Executes the LLM to generate the cover letter and saves it."""

        prompt = self.generate_prompt()
        structured_llm = self.llm.with_structured_output(CoverLetterOutput)
        attempts, max_attempts = 0, 2

        while attempts < max_attempts:
            try:
                self.structured_output = structured_llm.invoke(prompt)
                save_to_file(self.config['cover_letter_file'], self.structured_output.cover_letter)
                break
            except ValidationError:
                attempts += 1
                if attempts == max_attempts:
                    raise Exception(f"Failed to generate cover letter after {attempts} retries.")

    def run(self):
        """Main method to generate and save the cover letter."""
        self.execute_llm_and_save()
        return self.structured_output


if __name__ == "__main__":

    job_profile_title = "Business Analyst"
    bot_tool = CoverLetterBotTool(profile_title=job_profile_title)
    structured_output = bot_tool.run()

    print(structured_output)
