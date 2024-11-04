import streamlit as st

from components.video import VideoComponent
from components.button import ContactButtonComponent
from components.form import SignUpFormComponent
from components.contact import ContactInfoComponent

from config import Config


def setup_layout():
    st.set_page_config(page_title="Dr. Mathew Divine: Expert Data Analysis & AI Strategy", layout="centered")
    # Custom CSS for centering and styling
    st.markdown(
        """
        <style>
        .centered { display: flex; align-items: center; height: 100%; justify-content: center; padding-right: 20px; }
        h2 { line-height: 0.1; margin-bottom: 3px; letter-spacing: 1px; white-space: nowrap; }
        .title-h1 { margin-bottom: 40px; font-weight: 200; letter-spacing: 1px; color: #dec89f; }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_site_info():
    """Displays site usage information and waitlist sign-up option."""
    st.header("Using the Site")
    st.write(
        "Welcome to my profile! Here you’ll find profiles for various roles where I could be a great fit. "
        "For now, you can explore the most common profiles, but I am also working on a feature that allows "
        "you to create a custom profile, enabling a unique cover letter and skills assessment tailored to your needs. "
        "This feature is coming soon—sign up below to join the waitlist for updates!"
    )
    st.markdown(
        """
        ---
        """
    )


def main():
    setup_layout()

    VideoComponent(
        header="Introduction Video",
        video_url="https://youtu.be/dQw4w9WgXcQ"  # Replace with the actual URL
    ).display()

    ContactButtonComponent(
        header="Contact Dr. Mathew Divine",
        description="Feel free to schedule a call to discuss potential collaborations.",
        button_text="Book a Call",
        link="https://cal.com/dr-mathew-divine"
    ).display()

    display_site_info()
    SignUpFormComponent().display()
    st.markdown(
        """
        ---
        """
    )
    ContactInfoComponent().display()


# Run the dashboard
if __name__ == "__main__":
    main()
