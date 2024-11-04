import streamlit as st
import time
import os
import urllib.parse
from pathlib import Path


# Helper function to generate the assessment content and save it to a directory
def generate_assessment_content(job_profile_text, assessment_id):
    """Generates assessment content and saves it into a specific folder."""
    assessment_folder = Path(f"src/assets/docs/output/assessments/{assessment_id}")
    assessment_folder.mkdir(parents=True, exist_ok=True)

    # Simulated content generation for this example
    summary = "Summary: This job profile requires expertise in data engineering and cloud technologies."
    skills_assessment = "Skills: Python, Cloud Services, SQL, Kubernetes, Terraform"
    cover_letter = "Dear Hiring Team, this cover letter is customized for the role."

    # Save the content as text files
    (assessment_folder / "summary.txt").write_text(summary)
    (assessment_folder / "skills_assessment.txt").write_text(skills_assessment)
    (assessment_folder / "cover_letter.md").write_text(cover_letter)


# Main App
# st.set_page_config(page_title="Job Profile Assessment Tool")

# Check for the assessment_id in the URL
#params = st.experimental_get_query_params()
params = st.query_params
assessment_id = params.get("assessment_id", None)

st.markdown(params)

# Display assessment if the assessment_id is available
if assessment_id:
    assessment_folder = Path(f"src/assets/docs/output/assessments/{assessment_id}")
    st.write(assessment_folder)
    st.write(assessment_id)
    if assessment_folder.exists():
        st.header("Your Custom Job Profile Assessment")

        # Display the saved summary, skills assessment, and cover letter
        st.subheader("Job Profile Summary")
        st.write((assessment_folder / "summary.txt").read_text())

        st.subheader("Skills Assessment")
        st.write((assessment_folder / "skills_assessment.txt").read_text())

        st.subheader("Tailored Cover Letter")
        st.markdown((assessment_folder / "cover_letter.md").read_text())
    else:
        st.error("This assessment does not exist. Please generate an assessment first.")
else:
    # Show input form and assessment generation button
    st.title("Custom Job Profile Assessment Tool")
    st.write("""
        ### Instructions:
        1. Paste the job profile into the text area below.
        2. Click "Generate Assessment".
        3. A unique link to view your custom assessment will be provided.
    """)

    # Job profile input field
    job_profile_input = st.text_area("Paste your job profile here...", height=200)

    # Button to generate assessment
    if st.button("Generate Assessment"):
        if job_profile_input.strip():
            with st.spinner("Generating your assessment..."):
                # Generate a unique ID based on the current time
                unique_id = str(int(time.time()))

                # Generate and save assessment content
                generate_assessment_content(job_profile_input, unique_id)

                # Provide the custom URL with the assessment_id
                base_url = st.get_option("server.baseUrlPath")
                profile_url = f"{base_url}?assessment_id={urllib.parse.quote(unique_id)}"
                st.success("Assessment generated successfully!")
                st.markdown(f"### [View your custom assessment here]({profile_url})")
        else:
            st.error("Please enter a job profile to generate an assessment.")