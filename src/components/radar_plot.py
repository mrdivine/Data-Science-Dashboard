from typing import List, Dict
import textwrap


class RadarChartComponent:
    """A component for displaying a radar chart based on skills from JSON data."""

    def __init__(self, data: List[Dict], title: str):
        """
        Initialize the radar chart component with data and title.

        Parameters:
            data (List[Dict]): Data containing 'requirement_name' and 'self_assessment_score' fields.
            title (str): Title of the radar chart.
        """
        self.data = data
        self.title = title

    def display(self):
        """Displays the radar chart in Streamlit."""
        # Extract skill names (requirement_name) and ratings (self_assessment_score)
        categories = [item['requirement_name'] for item in self.data]
        values = [float(item['self_assessment_score']) for item in self.data]

        # Append the first value to close the radar chart loop
        categories += [categories[0]]
        values += [values[0]]

        # Create the radar chart with Scatterpolar
        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Self-Assessment Score'
        ))

        # Update layout for aesthetics and clarity
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10],  # Set rating range from 0 to 10
                    tickfont=dict(color="black")
                )
            ),
            title=self.title,
            showlegend=False
        )

        # Display the radar chart in Streamlit
        st.plotly_chart(fig)

import streamlit as st
import plotly.graph_objects as go
from typing import List, Dict

class DetailedRequirementsComponent:
    """A component for displaying detailed requirements with hoverable examples."""

    def __init__(self, data: List[Dict], title: str):
        """
        Initialize the component with data and a title.

        Parameters:
            data (List[Dict]): List of dictionaries with requirement details.
            title (str): Title of the component display.
        """
        self.data = data
        self.title = title

    def display(self):
        """Displays requirements with hoverable examples and scores."""
        st.header(self.title)

        categories = [item['requirement_name'] for item in self.data]
        values = [float(item['self_assessment_score']) for item in self.data]
        hover_texts = [
            f"<b>Examples:</b><br>{'<br>'.join(item['examples'])}"
             for item in self.data
        ]
        def wrap_text(text, max_width=30):
            """Wraps text at the specified width for multiline display."""
            return "<br>".join(textwrap.wrap(text, width=max_width))

        wrapped_categories = [wrap_text(item['requirement_name']) for item in self.data]

        # Helper function to wrap text with line breaks


        def display_radar_chart():
            #st.subheader("Radar Chart")
            # Radar chart with hover text on each requirement
            fig = go.Figure(data=go.Scatterpolar(
                r=values,
                theta=wrapped_categories,
                fill='toself',
                text=hover_texts,
                hoverinfo="text",
                name='Self-Assessment'
            ))

            # Update layout with smaller font and adjusted text angle
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 10],
                        tickfont=dict(color="black")
                    ),
                    angularaxis=dict(
                        tickfont=dict(size=10),  # Reduce font size
                        rotation=45  # Rotate text to fit better around circle
                    )
                ),
                title="",#"Requirements Self-Assessment",
                title_x=0.5,
                showlegend=False
            )
            
            # Display the radar chart in Streamlit
            st.plotly_chart(fig)



        display_radar_chart()

        # Display each requirement in detail with rationale and scores
        for item in self.data:
            st.markdown(f"### {item['requirement_name']} ({item['requirement_type']})")
            st.markdown(f"**Self-Assessment Score**: {item['self_assessment_score']}/10")
            st.markdown(f"**Rationale**: {item['rationale']}")
            if item.get("examples"):
                st.markdown("**Examples**:")
                for example in item["examples"]:
                    st.markdown(f"- {example}")
            st.markdown("---")  # Divider between requirements
