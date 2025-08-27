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
        # Add responsive CSS
        st.markdown("""
            <style>
            @media (max-width: 640px) {
                .responsive-container {
                    flex-direction: column-reverse !important;
                    gap: 1rem !important;
                }
                .profile-image {
                    max-width: 200px !important;
                    margin: 0 auto !important;
                }
                .title-h1 {
                    font-size: 1.8rem !important;
                }
                h2 {
                    font-size: 1.2rem !important;
                }
            }
            .responsive-container {
                display: flex;
                align-items: center;
                gap: 2rem;
            }
            .profile-content {
                flex: 1;
            }
            .profile-image {
                flex: 0 0 auto;
                max-width: 300px;
            }
            </style>
        """, unsafe_allow_html=True)

        # Create responsive container
        st.markdown(
            f"""
            <div class="responsive-container">
                <div class="profile-content">
                    <h1 class="title-h1">{self.name}</h1>
                    <h2>{self.title}</h2>
                    <h2>&</h2>
                    <h2>{self.subtitle}</h2>
                </div>
                <div class="profile-image">
                    <img src="data:image/png;base64,{self._get_image_as_base64()}" style="width: 100%; height: auto;">
                </div>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("---")

    def _get_image_as_base64(self):
        """Convert image to base64 string for inline HTML display."""
        import base64
        try:
            with open(self.image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except Exception as e:
            st.error(f"Error loading image: {str(e)}")
            return ""
