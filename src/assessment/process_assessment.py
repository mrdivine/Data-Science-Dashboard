from assessment.write_assessment import JobProfileBotTool
from assessment.write_cover_letter import CoverLetterBotTool
from config import Config


class ProcessAssessment:
    def __init__(self, input_text: str):
        self.input_text = input_text
        self.config = Config(job_profile_text=self.input_text)

    def run(self):
        JobProfileBotTool(self.input_text).run()
        CoverLetterBotTool(self.config["assessment_id"]).run()
        return self.config["assessment_id"]
