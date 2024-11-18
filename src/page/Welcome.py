import streamlit as st
import webbrowser

from components.button import ContactButtonComponent
from components.assessment_input import AssessmentInput
from components.contact import ContactInfoComponent
from components.header import HeaderComponent


def setup_layout():
    #st.set_page_config(page_title="Dr. Mathew Divine: Expert Data Analysis & AI Strategy", layout="centered")
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
    # Add your introduction text using st.markdown
    st.markdown("""
    👋 **Hi, I’m Dr. Mathew Divine**  
      
    I am an Expert in **Data Analytics & AI Strategy**, and I'm offering you my **15+ years** of experience in **data integration** and **AI-driven innovation** to **accelerate your business growth** and **enhance your market competitiveness**. I design and deploy **AI solutions in the Cloud** or lead teams to do so. My work  🚀 **drives efficiency**, 🤖 **automates workflows**, and 💡 **delivers strategic insights**. From **Petobyte Scale Data Pipelines** to **RAG systems** for pharmaceutical compliance, I’ve done it all. 

    ✨ **Try the Assessment Tool below** to see my **efficiency-driven approach** in action, or let’s chat about how I can bring **tailored AI solutions** to your business!  
        
    """)

    button_html = """
    <style>
        .custom-button {
            display: inline-block;
            padding: 12px 20px;
            font-size: 16px;
            color: white;
            background-color: #333333;
            text-align: center;
            text-decoration: none;
            border-radius: 8px;
            border: 1px solid #dcdcdc;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .custom-button:hover {
            background-color: #166aa2;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
        }
    </style>

    <a href="https://cal.com/dr-mathew-divine/15min" target="_blank" class="custom-button">💬 Book your Free Strategy Session today!</a>
    """

    # Display the button using st.markdown
    st.markdown(button_html, unsafe_allow_html=True)

    st.markdown("""
    ---
    """)





def welcome():
    setup_layout()
    HeaderComponent().display()
    display_site_info()
    st.title("🛠 Job Profile Assessment Tool️")
    st.markdown("""---""")
    st.write("""
        ### Instructions:
        Assess Dr. Mathew Divine against your job profile and see if he is the right fit for your project. 
        1. Paste your job profile into the text area below.
        2. Click "Generate Assessment".
        3. A unique link to view your custom assessment will be provided.
    """)
    AssessmentInput().display()
    st.markdown("""
    ---
    """)
    ContactInfoComponent().display()

if __name__ == "__main__":
    welcome()
