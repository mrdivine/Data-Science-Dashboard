from langchain_openai import ChatOpenAI
from pydantic import ValidationError
from pydantic import BaseModel, Field
from config import Config
from utils import read_csv_as_string, parse_executive_summary, save_to_file


class CoverLetterOutput(BaseModel):
    """Represents the generated cover letter as a single text field."""
    cover_letter: str = Field(description="The content of the cover letter generated for the job application.")


class CoverLetterBotTool:
    """Generates a cover letter by combining job profile, projects, and executive summary."""

    def __init__(self, assessment_id: str):
        self.config = Config(assessment_id=assessment_id)
        self.llm = ChatOpenAI()
        self.structured_output = None

    def load_requirements_assessment(self):
        """Read requirements assessment CSV file as a string for prompt injection."""
        requirements_assessment_file = self.config["requirements_assessment_file"]
        if requirements_assessment_file:
            return read_csv_as_string(requirements_assessment_file)
        raise FileNotFoundError("Requirements assessment file path is missing in config.")

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
        You should write the letter in the {self.config["job_profile_language"]} language of the job profile requirements assessment.

        Use the following Job Profile Title to write in the cover letter:
        {self.load_job_profile_title()}
        
        For inspiration and understanding of the Candidates Executive Summary:
        {self.load_executive_summary()}

        The reuirements assessment for you to undersatnd how well the applications given experience matches the job profile requirements:
        {self.load_requirements_assessment()}

        **Instructions**:
        - Make a bridge between the job profile skills and the candidate skills.
        - Make a convingin argument why the candidate maybe qualified, overqualified, or under-qualified.
        - Begin with an **objective overview** of the candidate’s fit for the role, listing key matching skills and experiences.
        - Highlight specific **relevant projects** and how they align with the job's requirements.
        - **Note any gaps** and propose how other skills may compensate.
        - End with a **polished closing** that conveys enthusiasm for the role.


        **Expected Output**:
        A single cover letter written in the voice of the candidate that objectively highlights the candidate's strengths, identifies areas of partial fit, and emphasizes complementary skills.
        written in markdown. You should avoid extensive use of headings, and prefer a more personal approach in the form of a letter, without the heading. Just Dear,... or to whom it concerns" as the beginning.
        close the letter with just "Sincerley" if in English otherwise "mit freundlichen Grüßen" if in German.
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
