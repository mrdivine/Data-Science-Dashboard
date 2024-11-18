import streamlit as st
import time
from assessment.process_assessment import ProcessAssessment
from config import Config


class AssessmentInput:
    """A reusable component class for handling assessment input in a Streamlit app."""

    def __init__(self, placeholder_text: str = "Your Job Profile Text goes here....", max_clicks: int = 3):
        self.config = None
        self.assessment_link = False
        self.is_disabled = False
        self.placeholder_text = placeholder_text
        self.max_clicks = max_clicks

        # Initialize the session state variables if not already set
        if "text_area_disabled" not in st.session_state:
            st.session_state.text_area_disabled = False
        if "data_privacy_agreed" not in st.session_state:
            st.session_state.data_privacy_agreed = False
        if "click_count" not in st.session_state:
            st.session_state.click_count = 0
        if "assessment_ids" not in st.session_state:
            st.session_state["assessment_ids"] = []

    def generate_assessment(self):
        """Handles the assessment generation process and tracks clicks."""
        # Increment the click counter
        st.session_state.click_count += 1
        if st.session_state.click_count >= self.max_clicks:
            # Disable both the text area and the checkbox if the click limit is reached.
            st.session_state["text_area_disabled"] = True
            st.session_state["data_privacy_agreed"] = False
            st.toast("Click limit reached. The assessment tool is now disabled.")
            return

        # Immediately uncheck the checkbox
        st.session_state["data_privacy_agreed"] = False
        # Disable the text area while processing
        st.session_state["text_area_disabled"] = True
        # Show a success message and simulate processing delay
        alert = st.toast("Assessment Processing...")
        try:
            # Attempt to run the assessment processing
            process_assessment = ProcessAssessment(st.session_state.get("text_area", ""))
            # This is where assessment_id is created and this is where it will be taken care of.
            assessment_id = process_assessment.run()
            self.config = Config(assessment_id=assessment_id)

            if len(st.session_state["assessment_ids"]) < 2:
                st.session_state["assessment_ids"].append(assessment_id)

            # Show a success message if processing completes successfully
            alert.empty()
            st.toast(f"Assessment {assessment_id} generated successfully!", icon="✅")
            time.sleep(1)

        except Exception as e:
            # Handle any errors that occur during processing
            alert.empty()
            st.toast(f"Error generating assessment: {str(e)}", icon="🚨")
            st.session_state["text_area_disabled"] = False
            return
        alert.empty()
        alert = st.toast("Assessment generated successfully!")
        time.sleep(1)
        alert.empty()
        # Re-enable the text area after processing
        st.session_state["text_area_disabled"] = False

    def assessment_disabled(self):
        """Checks if the assessment button should be enabled."""
        if not st.session_state["data_privacy_agreed"] and not st.session_state["click_count"] < self.max_clicks:
            self.is_disabled = True
            return True
        elif not st.session_state["data_privacy_agreed"]:
            return True

        return False


    def create_buttons(self, test=None):
        """Create a button for each assessment ID and handle navigation."""
        def _callback(**kwargs):
            """Callback function to store the assessment ID in session state."""
            st.session_state["assessment_id"] = kwargs["assessment_id"]

        if st.session_state["assessment_ids"]:
            st.markdown("### Your Custom Assessments:")

        for assessment_id in st.session_state["assessment_ids"]:
            # Create a button for each assessment ID
            on_click = st.button(
                f"View Assessment",
                key=f"{assessment_id}",
                kwargs={"assessment_id": assessment_id},
                on_click=_callback
            )

            # Check if the button was clicked and switch to the assessment page
            if on_click:
                st.switch_page(st.session_state["assessment_page"])

    def display(self):
        """Displays the input form and handles user interactions."""
        # Create a text area for job profile input
        st.text_area(
            "Job Profile",
            value="",
            placeholder=self.placeholder_text,
            disabled=st.session_state.get("text_area_disabled", False),
            key="text_area"
        )

        # Layout with two columns for better organization
        col1, col2 = st.columns([4, 11])
        with col2:
            # Checkbox for agreeing to the data privacy policy
            st.checkbox(
                "I have read and agree to the Data Privacy Agreement",
                key="data_privacy_agreed",
                disabled=st.session_state.click_count >= self.max_clicks
            )
        with col1:
            # Generate Assessment button
            st.button(
                "Generate Assessment",
                disabled=self.assessment_disabled(),
                on_click=self.generate_assessment
            )

        self.create_buttons()





