import streamlit as st
from assessment.create_profile_page import ProfilePageMaker
from config import Config


class CustomAssessmentPageMaker(ProfilePageMaker):
    """A class to create and display a custom assessment page."""

    def __init__(self, assessment_id: str):
        """Initialize the Custom Assessment Page Maker.

        Args:
            assessment_id (str): Unique identifier for the assessment.
        """
        self.assessment_id = assessment_id

        # Try to initialize the Config with the given assessment_id
        try:
            self.config = Config(assessment_id=self.assessment_id)
        except FileNotFoundError:
            # If the assessment_id is invalid or missing, default to "01"
            st.warning(f"Assessment ID '{assessment_id}' not found. Defaulting to Product Owner.")
            self.assessment_id = "04"
            self.config = Config(assessment_id=self.assessment_id)

        # Initialize the superclass with the profile title from the config
        super().__init__(self.assessment_id)

    def display_profile(self):
        """Display the custom assessment profile."""
        #st.write(st.session_state)
        super().display_profile()


# Example usage
def custom_assessment():
    assessment_id = st.session_state.get("assessment_id")
    page_maker = CustomAssessmentPageMaker(assessment_id)
    page_maker.display_profile()
