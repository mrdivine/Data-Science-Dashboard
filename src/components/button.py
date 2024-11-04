# src/components/contact_button.py
import streamlit as st
from pathlib import Path


class ContactButtonComponent:
    """Component to display a customizable, styled contact button with optional spacing."""

    def __init__(self, header="Get in Touch",
                 description="Feel free to schedule a call for further discussion.",
                 button_text="Schedule a Call with Dr. Mathew Divine",
                 link="https://cal.com/dr-mathew-divine/15min"):
        self.header = header
        self.description = description
        self.button_text = button_text
        self.link = link

    def display(self):
        """Displays the contact button and its header/description in Streamlit with custom styling."""
        st.header(self.header)
        st.markdown(self.description)

        # Custom HTML & CSS for CTA button with spacing and neutral colors
        st.markdown(
            f"""
            <style>
            .cta-button {{
                display: inline-block;
                padding: 12px 24px;
                font-size: 18px;
                color: #ffffff;
                background-color: #4b4b4b;
                border: none;
                border-radius: 5px;
                text-align: center;
                text-decoration: none;
                cursor: pointer;
                font-weight: 500;
                transition: background-color 0.3s ease;
            }}
            .cta-button:hover {{
                background-color: #6b6b6b;
            }}
            .spacer {{
                margin-top: 20px;
                border-top: 1px solid #e0e0e0;
                padding-top: 20px;
            }}
            </style>
            <a href="{self.link}" target="_blank" class="cta-button">{self.button_text}</a>
            <div class="spacer"></div>
            """,
            unsafe_allow_html=True
        )


class ResumeDownloadButtonComponent:
    """Component to display a download button for the candidate's resume."""

    def __init__(self, resume_pdf_path, button_text="Download Full Resume"):
        """
        Initializes the component with the resume file path and button display settings.

        :param resume_pdf_path: Path to the resume PDF file, including the filename.
        :param button_text: Text displayed on the download button.
        """
        self.resume_pdf_path = resume_pdf_path
        self.button_text = button_text
        # Extract the filename directly from the path
        self.file_name = Path(resume_pdf_path).name

    def display(self):
        """Displays a download button for the resume file."""
        # Read and display the download button for the resume
        with open(self.resume_pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(
                label=self.button_text,
                data=pdf_bytes,
                file_name=self.file_name,
                mime="application/pdf"
            )
