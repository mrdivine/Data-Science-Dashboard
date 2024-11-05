import streamlit as st
from utils import read_and_clean_csv, load_json
from components.radar_plot import RadarChartComponent, DetailedRequirementsComponent
from components.header import HeaderComponent
from components.cover_letter import CoverLetterComponent
from components.contact import ContactInfoComponent
from components.button import ResumeDownloadButtonComponent
from config import Config
from pathlib import Path


class ProfilePageMaker:
    def __init__(self, profile_title: str):
        self.config = Config(profile_title)

    def display_profile(self):
        self.setup_layout()

        HeaderComponent(
            name=self.config["candidate_name"],
            title=self.config["candidate_title"],
            subtitle=self.config["candidate_subtitle"],
            image_path=self.config["candidate_profile_image"]
        ).display()

        st.title(self.config["profile_title"])
        with st.expander("Profile Details", expanded=False):
            st.markdown(Path(self.config["job_profile_file"]).read_text(), unsafe_allow_html=True)

        CoverLetterComponent(
            cover_letter_file=self.config["cover_letter_file"],
            signature_image=self.config["signature_image"]
        ).display()

        self.display_requirements_assessment()

        ResumeDownloadButtonComponent(
            self.config["resume_pdf"]
        ).display()

        ContactInfoComponent(name=self.config["candidate_name"],
                             location=self.config["candidate_location"],
                             ).display()

    def setup_layout(self):
        st.set_page_config(page_title=self.config["page_title"], layout=self.config["layout"])
        st.markdown(f"<style>{self.config['header_css']}</style>", unsafe_allow_html=True)

    def display_requirements_assessment(self):
        # Load and display skills tables and charts
        requirements_assessment = load_json(self.config["requirements_assessment_file"])

        def json_to_markdown(requirements_data):
            """Converts a list of requirement assessments in JSON format to a Markdown string."""
            markdown_output = ""
            #st.write(requirements_data)
            for requirement in requirements_data:
                requirement_name = requirement.get("requirement_name", "")
                requirement_type = requirement.get("requirement_type", "")
                related_experience = requirement.get("related_experience", "")
                examples = requirement.get("examples", [])
                self_assessment_score = requirement.get("self_assessment_score", "")
                rationale = requirement.get("rationale", "")

                # Format the main requirement section
                markdown_output += f"- **{requirement_name} ({requirement_type})**\n"
                markdown_output += f"    - **Related Experience**: {related_experience}\n"

                # Add each example, if any
                if examples:
                    markdown_output += "    - **Examples**:\n"
                    for i, example in enumerate(examples, start=1):
                        markdown_output += f"        {i}. **{example}**\n"

                # Add self-assessment score and rationale
                markdown_output += f"    - **Self-Assessment**: {self_assessment_score}/10\n"
                markdown_output += f"    - **Rationale**: {rationale}\n\n"

            return markdown_output

        # st.title("Requirements Assessment")
        # with st.expander("Requirements Assessment Report", expanded=False):
        #     st.markdown(json_to_markdown(requirements_assessment))

        # st.markdown("---")

        #RadarChartComponent(requirements_assessment, title="Candidate Skills Assessment").display()
        DetailedRequirementsComponent(requirements_assessment, title="Candidate Requirements Assessment").display()

