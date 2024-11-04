import streamlit as st
from utils import read_and_clean_csv
from components.radar_plot import RadarChartComponent
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

        self.display_skills()

        ResumeDownloadButtonComponent(
            self.config["resume_pdf"]
        ).display()

        ContactInfoComponent(name=self.config["candidate_name"],
                             location=self.config["candidate_location"],
                             ).display()

    def setup_layout(self):
        st.set_page_config(page_title=self.config["page_title"], layout=self.config["layout"])
        st.markdown(f"<style>{self.config['header_css']}</style>", unsafe_allow_html=True)

    def display_skills(self):
        # Load and display skills tables and charts
        job_profile_skills = read_and_clean_csv(self.config["job_profile_skills_file"])
        candidate_skills = read_and_clean_csv(self.config["candidate_skills_file"])
        requirements_assessment = read_and_clean_csv(self.config["requirements_assessment_file"])

        # Display data with RadarChartComponent
        st.title("Job Profile Skills Assessment")
        with st.expander("Job Profile Skills Table", expanded=False):
            st.table(job_profile_skills)

        RadarChartComponent(job_profile_skills, "Job Profile Skills Radar Chart").display()
        st.title("Candidate Skills Assessment")
        with st.expander("Candidate Skills Table", expanded=False):
            st.table(candidate_skills)
        RadarChartComponent(candidate_skills, "Candidate Skills Radar Chart").display()
        st.title("Requirements Assessment")
        with st.expander("Requirements Assessment Table", expanded=False):
            st.table(requirements_assessment)

        st.markdown("---")



