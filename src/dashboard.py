import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Basic setup
st.set_page_config(page_title="Dr. Mathew Divine: Expert Data Scientist & AI Strategist", layout="centered")
ms = st.session_state
if "themes" not in ms:
    ms.themes = {"current_theme": "light",
                 "refreshed": True,

                 "light": {"theme.base": "dark",
                           "theme.backgroundColor": "black",
                           "theme.primaryColor": "#c98bdb",
                           "theme.secondaryBackgroundColor": "#5591f5",
                           "theme.textColor": "white",
                           "button_face": "🌜"}
                 }

# Custom CSS for vertical centering
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        align-items: center;
        height: 100%;
        justify-content: center;
        padding-right: 20px;
    }

    h2 {
        line-height: 0.1; /* Reduces the space between the h2 lines */
        margin-bottom: 3px; /* This can add some breathing room under the h2 */
        letter-spacing: 1px; /* This can add some breathing room under the h2 */
    }
    .title-h1 {
        margin-bottom: 40px; /* Adds space between h1 and h2 */
        font-weight: 200; /* Make your name more prominent */
        letter-spacing: 1px; /* Subtle spacing to give it more presence */
        color: #dec89f; /* Keeping the text white to play against the dark background */
    }
    # .centered h1, .centered h2 {
    #     text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.7); /* Slight glow to make the text pop */
    # }
    # 
    # body {
    #     background: linear-gradient(135deg, #141E30 0%, #243B55 100%); /* Dark-to-light gradient for more dynamic contrast */
    # }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating a two-column layout: Panorama image on the right and executive statement on the left
col1, col2 = st.columns([7, 5])  # Adjusting the width of the columns as necessary

# Left column for the executive statement

with col1:
    st.markdown(
        """
        <div class="centered">
            <div>
                <h1 class="title-h1">Dr. Mathew Divine</h1>
                <h2>Expert Data Scientist</h2>
                <h2>&</h2>
                <h2>AI Strategist</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Right column for the panorama image
with col2:
    st.image("src/assets/images/head_shot_round.png", use_column_width=True)

st.markdown(
"""
---
""",
)
# Placeholder for Job Profile
st.title("Applying for *Data Product Owner*")
st.markdown(
"""
---
""",
)

cover_letter = """
To whom it concerns:

With over 15 years of experience in Data Engineering and Machine Learning, I bring extensive expertise in developing and implementing data solutions that perfectly align with the requirements of your position as Product Owner for Data & Analytics.

Based on my self-assessment and project experience, I have developed significant proficiency in cloud technologies and data engineering. Over the past 7+ years, I have implemented cloud-based pipelines in AWS and OpenShift, utilizing technologies such as AWS Sagemaker, Snowflake, and Azure Cognitive Services, which are also relevant in the environment you have described. My skills, as visualized in the radar diagram, highlight a strong focus on Data Engineering, Data Modeling, and ETL processes, which I have applied in various projects, including the development of a clinical data catalog and a bioinformatics pipeline.

In the area of product development and management, I have led a team as Product Owner for the Analytics Landing Page, which developed innovative data products used in business intelligence and cognitive search functionalities. Particularly relevant to your requirements for data architecture and prototyping is my experience in the agile development of data solutions within a multinational environment for one of the top 20 pharmaceutical companies. In this role, I also implemented a CI/CD system for genome assemblies operating at a petabyte scale — clear evidence of my ability to successfully manage complex data structures and modern technologies.

In addition to technical skills (Cloud Computing, Data Visualization, NLP, Snowflake, and Python), my self-assessment also highlights strong soft skills, particularly in leadership, creative thinking, and project management. I have demonstrated these abilities in various leadership roles, most recently as Interim Head of Data Science and Head of Digital Lab, where I coached agile teams and led digital initiatives.

My analytical thinking and problem-solving skills, as shown in my self-assessment, support me in developing efficient solutions that meet both business and technology requirements.

With my outstanding communication skills in both German and English, I can seamlessly work in an international environment and foster collaboration between business and IT.

I would be thrilled to bring my comprehensive knowledge and diverse experience to your team and look forward to a personal conversation to discuss how I can optimally support your company’s goals.

Thank you for considering my application.

Best regards,

Dr. Mathew Divine
"""
st.write(cover_letter)
st.markdown(
"""
---
""",
)

# Hard Skills Table and Radar Plot
st.subheader("Hard Skills Self-Assessment")

hard_skills = pd.read_csv("src/assets/docs/hard_skills.csv", index_col=None)
st.table(hard_skills)


# Plotting radar chart for Hard Skills
def plot_radar(data, title):
    # Extracting 'Skill' and 'Proficiency' columns for the radar chart
    categories = data['Skill'].tolist()  # Skills as categories
    values = data['Proficiency (1-10)'].tolist()  # Proficiency values to plot

    # Creating the radar chart
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Proficiency'
    ))

    # Updating layout to enhance visibility and make the chart visually appealing
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],  # Assuming proficiency is scored from 1 to 10
                showticklabels=True,  # Ensuring tick labels are shown
                tickfont=dict(color="black")  # Set tick label color to black
            )
        ),
        title=title,
        showlegend=False
    )

    # Display the radar chart in the Streamlit app
    st.plotly_chart(fig)


plot_radar(hard_skills, "Hard Skills Radar Chart")

# Soft Skills Table and Radar Plot
st.subheader("Soft Skills Self-Assessment")
soft_skills = pd.read_csv("src/assets/docs/soft_skills.csv", index_col=None)
st.table(soft_skills)

# Plotting radar chart for Soft Skills
plot_radar(soft_skills, "Soft Skills Radar Chart")
st.markdown(
"""
---
""",
)

# Resume Download Button
with open("src/assets/docs/FullResume.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(label="Download Full Resume with Comple Project List", data=pdf_bytes, file_name="FullResume.pdf", mime="application/pdf")

st.markdown(
"""
---
""",
)
st.header("Contact Information")
st.markdown("""
**Dr. Mathew Divine**\n
Frankfurter Region, Deutschland\n
[LinkedIn](https://www.linkedin.com/in/dr-mathew-divine/) | [Google Scholar](https://scholar.google.de/citations?user=wGJeTZQAAAAJ&hl=en) | [Check out this GitHub Repo](https://github.com/mrdivine/Data-Science-Dashboard)
""")