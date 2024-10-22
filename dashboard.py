import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Basic setup
st.set_page_config(page_title="Dr. Mathew Divine: Expert Data Scientist & AI Strategist", layout="centered")

# Custom CSS for vertical centering
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        align-items: center;
        height: 100%;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating a two-column layout: Panorama image on the right and executive statement on the left
col1, col2 = st.columns([12, 5])  # Adjusting the width of the columns as necessary

# Left column for the executive statement
with col1:
    st.markdown(
        """
        <div class="centered">
            <div>
                <h1>Dr. Mathew Divine</h1>
                <h2>Expert Data Scientist & AI Strategist</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Right column for the panorama image
with col2:
    st.image("long_pic.jpeg", use_column_width=True)

# Placeholder for Job Profile
st.title("Applying for: Data Product Owner")

st.subheader("Letter of Intent")
cover_letter = """
Sehr geehrte Damen und Herren,

mit über 15 Jahren Berufserfahrung im Bereich Data Engineering und Machine Learning biete ich umfassende Kenntnisse in der Entwicklung und Implementierung von Datenlösungen an, die perfekt mit den Anforderungen Ihrer Position als Product Owner für Data & Analytics übereinstimmen.

Laut meiner Selbsteinschätzung und Projekterfahrung habe ich umfangreiche Kompetenzen in Cloud-Technologien und Data Engineering aufgebaut. In den letzten 7+ Jahren habe ich Cloud-basierte Pipelines in AWS und OpenShift implementiert und dabei Technologien wie AWS Sagemaker, Snowflake, und Azure Cognitive Services genutzt, die auch im von Ihnen geforderten Umfeld relevant sind. Die Visualisierung meiner Erfahrung in der Radardiagramm zeigt einen herausragenden Fokus auf Data Engineering, Datenmodellierung und ETL-Prozesse, die ich in verschiedenen Projekten wie der Entwicklung eines klinischen Datenkatalogs oder der Bioinformatik-Pipeline angewendet habe.

Im Bereich der Produktentwicklung und -leitung habe ich als Product Owner der Analytics Landing Page ein Team geleitet, das innovative Datenprodukte entwickelte, die in den Bereichen Business Intelligence und kognitive Suchfunktionen Anwendung fanden. Besonders relevant für Ihre Anforderungen an Datenarchitektur und Prototyping ist meine Erfahrung in der agilen Entwicklung von Datenlösungen, die ich in einem multinationalen Umfeld für einen der Top-20 Pharmaunternehmen aufgebaut habe. Hier habe ich zudem ein CI/CD-System für Genomassemblierungen implementiert, das in einer Petabyte-Skala operierte – ein klarer Beweis für meine Fähigkeit, komplexe Datenstrukturen und moderne Technologien erfolgreich zu managen.

Zusätzlich zu den harten technischen Fähigkeiten (Cloud Computing, Datenvisualisierung, NLP, Snowflake, und Python) weise ich laut meiner Selbsteinschätzung auch starke Soft Skills auf, insbesondere in den Bereichen Teamführung, kreatives Denken und Projektmanagement. Diese Fähigkeiten habe ich in diversen Führungspositionen unter Beweis gestellt, zuletzt als Interim Head of Data Science, wo ich agile Teams coache und digitale Initiativen leitete.

Meine analytische Denkweise und Problemlösungskompetenz – ebenfalls aus den Selbstbewertungstabellen ersichtlich – unterstützen mich dabei, effiziente Lösungen zu entwickeln, die den Anforderungen sowohl des Geschäfts als auch der Technologie gerecht werden.

Mit meinen herausragenden Kommunikationsfähigkeiten in Deutsch und Englisch kann ich nahtlos in einem internationalen Umfeld arbeiten und die Zusammenarbeit zwischen Geschäft und IT fördern.

Ich wäre begeistert, mein fundiertes Wissen und meine vielfältigen Erfahrungen in Ihr Team einzubringen und freue mich auf ein persönliches Gespräch, um zu erörtern, wie ich Ihre Unternehmensziele optimal unterstützen kann.

Vielen Dank für die Berücksichtigung meiner Bewerbung.

Mit freundlichen Grüßen,\n
Dr. Mathew Divine
"""
st.write(cover_letter)

# Hard Skills Table and Radar Plot
st.subheader("Hard Skills Self-Assessment")

hard_skills = pd.read_csv("hard_skills.csv", index_col=None)
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
soft_skills = pd.read_csv("soft_skills.csv", index_col=None)
st.table(soft_skills)

# Plotting radar chart for Soft Skills
plot_radar(soft_skills, "Soft Skills Radar Chart")

# Resume Download Button
with open("FullResume.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(label="Download Full Resume with Comple Project List", data=pdf_bytes, file_name="FullResume.pdf", mime="application/pdf")

st.header("Contact Information")
st.markdown("""
**Dr. Mathew Divine**\n
Frankfurter Region, Deutschland\n
[LinkedIn](https://www.linkedin.com/in/dr-mathew-divine/) | [Google Scholar](https://scholar.google.de/citations?user=wGJeTZQAAAAJ&hl=en) | [Check out this GitHub Repo](https://github.com/dr-scholar/Dr-Mathew-Divine)
""")