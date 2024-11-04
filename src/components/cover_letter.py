import streamlit as st
from pathlib import Path


class CoverLetterComponent:
    """Component to display the candidate's cover letter with a signature and divider."""

    def __init__(self, cover_letter_file, signature_image, divider=True):
        """
        Initializes the component with paths for the cover letter file and signature image.

        :param cover_letter_file: Path to the cover letter markdown file.
        :param signature_image: Path to the candidate's signature image.
        :param divider: Whether to display a divider line below the content.
        """
        self.cover_letter_file = cover_letter_file
        self.signature_image = signature_image
        self.divider = divider

    def display(self):
        """Displays the cover letter with the candidate's signature and an optional divider."""
        # Read and display cover letter content
        cover_letter = Path(self.cover_letter_file).read_text()
        st.markdown(cover_letter, unsafe_allow_html=True)

        # Display signature image
        st.image(self.signature_image, width=300)

        # Optionally display a divider line
        if self.divider:
            st.markdown("---")