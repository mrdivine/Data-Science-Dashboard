import streamlit as st
# Display video placeholder


class VideoComponent:
    """Component to display an introduction video."""

    def __init__(self, header="Introduction Video", video_url="https://youtu.be/dQw4w9WgXcQ"):
        self.header = header
        self.video_url = video_url

    def display(self):
        """Displays the header and video."""
        st.header(self.header)
        st.video(self.video_url)
