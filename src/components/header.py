# src/components/header_component.py
import streamlit as st


class HeaderComponent:
    """Component to display the header for the profile page."""

    def __init__(self, name="Dr. Mathew Divine", title="Expert in Data Analytics", subtitle="AI Strategy", image_path="src/assets/images/head_shot_round.png"):
        self.name = name
        self.title = title
        self.subtitle = subtitle
        self.image_path = image_path

    def display(self):
        col1, col2 = st.columns([7, 5])
        with col1:
            st.markdown(
                f"""
                <div class="centered">
                    <div>
                        <h1 class="title-h1">{self.name}</h1>
                        <h2>{self.title}</h2>
                        <h2>&</h2>
                        <h2>{self.subtitle}</h2>
                    </div>
                </div>
                """, unsafe_allow_html=True
            )
        with col2:
            st.image(self.image_path, use_container_width=True)
        st.markdown("---")
