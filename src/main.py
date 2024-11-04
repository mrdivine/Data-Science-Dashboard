from pathlib import Path
from assessment import JobProfileBotTool
from cover_letter import CoverLetterBotTool

# Main entry point
if __name__ == "__main__":

    job_profile_name = "Product Owner"
    job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    JobProfileBotTool(job_profile_name, job_profile_text).run()
    CoverLetterBotTool(job_profile_name).run()

    job_profile_name = "Data Science Expert - NLP Focus"
    job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    JobProfileBotTool(job_profile_name, job_profile_text).run()
    CoverLetterBotTool(job_profile_name).run()

    job_profile_name = "Data Engineer"
    job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    JobProfileBotTool(job_profile_name, job_profile_text).run()
    CoverLetterBotTool(job_profile_name).run()

    job_profile_name = "Python Cloud Developer"
    job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    JobProfileBotTool(job_profile_name, job_profile_text).run()
    CoverLetterBotTool(job_profile_name).run()

    job_profile_name = "Business Analyst"
    job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    JobProfileBotTool(job_profile_name, job_profile_text).run()
    CoverLetterBotTool(job_profile_name).run()
