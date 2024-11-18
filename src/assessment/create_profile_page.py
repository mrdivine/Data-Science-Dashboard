import streamlit as st
from utils import load_json
from components.radar_plot import DetailedRequirementsComponent
from components.header import HeaderComponent
from components.cover_letter import CoverLetterComponent
from components.contact import ContactInfoComponent
from components.button import ResumeDownloadButtonComponent
from config import Config
from pathlib import Path


class ProfilePageMaker:
    def __init__(self, assessment_id: str):
        self.config = Config(assessment_id)

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

        col1, col2 = st.columns([7,12])
        with col1:
            ResumeDownloadButtonComponent(self.config["resume_pdf"]).display()
        with col2:
            assessment_link = f"?assessment_id={st.session_state['assessment_id']}"
            st.markdown(f"[Right-Click and Copy to share the link to this assessment!]({assessment_link})", unsafe_allow_html=True)

        st.markdown("<br></sb>", unsafe_allow_html=True)
        ContactInfoComponent(name=self.config["candidate_name"],
                             location=self.config["candidate_location"],
                             ).display()

    def setup_layout(self):
        st.markdown(f"<style>{self.config['header_css']}</style>", unsafe_allow_html=True)

    def display_requirements_assessment(self):
        # Load and display skills tables and charts
        requirements_assessment = load_json(self.config["requirements_assessment_file"])
        DetailedRequirementsComponent(requirements_assessment, title="candidate Requirements Assessment").display()

