import streamlit as st
from page.Welcome import welcome
from page.Disclaimer import disclaimer
from page.Custom_Assessment import custom_assessment

st.set_page_config(page_title="Dr. Mathew Divine 🚀", page_icon=":material/terminal:", initial_sidebar_state="collapsed")
# Check for the assessment_id in the URL
params = st.query_params
new_assessment_id = params.get("assessment_id", False)
current_assessment_id = st.session_state.get("assessment_id", False)

if new_assessment_id:
    st.session_state["assessment_id"] = new_assessment_id
    current_assessment_id = st.session_state["assessment_id"]


welcome_page = st.Page(welcome, title="Welcome", icon=":material/add_circle:", url_path="welcome")
disclaimer_page = st.Page(disclaimer, title="Disclaimer", icon=":material/delete:",  url_path="disclaimer")

if current_assessment_id:
    custom_assessment_page = st.Page(custom_assessment, title="Custom Assessment",
                                     icon=":material/circle:", default=True, url_path="custom_assessment")

    pages = st.navigation([welcome_page, custom_assessment_page, disclaimer_page])
    st.session_state["assessment_page"] = custom_assessment_page
else:
    pages = st.navigation([welcome_page, disclaimer_page])

pages.run()
