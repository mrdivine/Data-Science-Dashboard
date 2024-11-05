import streamlit as st
import time
import os
import urllib.parse
from pathlib import Path
from config import Config

c = Config("Business Analyst")


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

# Check for the assessment_id in the URL
params = st.query_params
assessment_id = params.get("assessment_id", None)

# Show params for Testing
# st.markdown(params)

# Display assessment if the assessment_id is available
if assessment_id:
    assessment_folder = Path(f"src/assets/docs/output/assessments/{assessment_id}")
    st.write("# debugging....")
    st.write(assessment_folder)
    st.write(f"{assessment_id} \n\n --- \n\n", unsafe_allow_html=True )
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
    st.title("Custom Assessment Tool")
    st.markdown("""---""")
    st.write("""
        ### Instructions:
        Assess Dr. Mathew Divine against your job profile and see if he is the right fit for your project. 
        1. Paste your job profile into the text area below.
        2. Click "Generate Assessment".
        3. A unique link to view your custom assessment will be provided.
    """)

    # Job profile input field
    job_profile_input = st.text_area("Job Profile",
                                     height=300,
                                     placeholder=f"""{c["profile_title"]}\n\n{Path(c["job_profile_file"]).read_text() }""")


# Button to generate assessment
col1, col2 = st.columns([4, 11])
with col2:
    data_privacy_agreed = st.checkbox("I have read and agree to the [Liability Disclaimer and the Data Usage Policy](/Disclaimer)")
with col1:
    if st.button("Generate Assessment", disabled=not data_privacy_agreed):
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

with st.expander("**(optional)** Add a Custom List of Projects"):
        st.markdown("### Generate Custom Assessment for your Candidate  \n"
                    "Place your candidate's project's list and other professional experience to create a custom assessment.  \n"
                    "Add in a `Project Title`, `Bullet-Points (*)`, `soft-skills`, `hard-skills`, and `technologies` for as many projects"
                    "that are relevant for the job profile. You can add extra fields just by adding a heading in Markdown\n"
                    "followed by the relevant text. Below is a an example of what a project's list could look like using\n"
                    "the project's list of Dr. Mathew Divine. ")
        project_lists_input = st.text_area("Paste your list of projects here and other professional information...",
                                           height=400,
                                           placeholder=f"""{Path(c["candidate_projects_list_file"]).read_text()}""")
