import streamlit as st
import pandas as pd

# Basic setup
st.set_page_config(page_title="Dr. Mathew Divine: Expert Data Scientist & AI Strategist", layout="centered")

# Sidebar for job profile input
st.sidebar.header("Create a New Job Profile")
job_title = st.sidebar.text_input("Job Title", "Data Product Owner")
responsibilities = st.sidebar.text_area("Responsibilities", "Enter the job responsibilities...")
skills_required = st.sidebar.text_area("Skills Required", "Enter the required skills...")

# Button to submit the job profile
if st.sidebar.button("Generate Profile"):
    st.session_state["job_title"] = job_title
    st.session_state["responsibilities"] = responsibilities
    st.session_state["skills_required"] = skills_required

if "job_title" in st.session_state:
    # Displaying job profile in a new "tab" like page
    tab1, tab2 = st.tabs([st.session_state["job_title"], "Existing Profile"])

    # New Job Profile Tab
    with tab1:
        st.title(st.session_state["job_title"])
        st.subheader("Responsibilities")
        st.write(st.session_state["responsibilities"])
        st.subheader("Required Skills")
        st.write(st.session_state["skills_required"])

        # You can dynamically generate other content here like tables, charts, etc.

    # Existing Profile Tab (like the original page with hard and soft skills)
    with tab2:
        st.title("Dr. Mathew Divine: Expert Data Scientist & AI Strategist")
        # Display your existing dashboard content here

    if "job_title" in st.session_state:
        # Placeholder for tables, charts, and radar plots related to the new job profile
        st.subheader(f"Skills Assessment for {st.session_state['job_title']}")

        # Example: Display Hard Skills Table (dynamically generated based on input)
        hard_skills = pd.DataFrame({
            'Skill': ['Python', 'AWS', 'Data Engineering'],
            'Proficiency (1-10)': [9, 8, 7],
            'Relevant Experience Summary': ['15+ years', '7+ years', '10 years']
        })

        st.table(hard_skills)

        # Placeholder for the radar plot (you can reuse the plot_radar function)
        # plot_radar(hard_skills, "Hard Skills Assessment")
