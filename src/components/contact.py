import streamlit as st


class ContactInfoComponent:
    """A component to display contact information with links to professional profiles."""

    def __init__(self, name="Dr. Mathew Divine", location="Frankfurt Region, Germany", linkedin_url="", scholar_url="",
                 github_url=""):
        self.name = name
        self.location = location
        self.linkedin_url = linkedin_url or "https://www.linkedin.com/in/dr-mathew-divine/"
        self.scholar_url = scholar_url or "https://scholar.google.de/citations?user=wGJeTZQAAAAJ&hl=en"
        self.github_url = github_url or "https://github.com/mrdivine/Data-Science-Dashboard"

    def display(self):
        """Displays the contact information with provided profile links."""
        st.header("Contact Information")
        st.markdown(f"""
        **{self.name}**  
        {self.location}  
        [LinkedIn]({self.linkedin_url}) | [Google Scholar]({self.scholar_url}) | [GitHub]({self.github_url})
        """)
