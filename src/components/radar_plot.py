import streamlit as st
import plotly.graph_objects as go
import pandas as pd


class RadarChartComponent:
    """A component for displaying a radar chart based on skill names and ratings."""

    def __init__(self, data: pd.DataFrame, title: str):
        """
        Initialize the radar chart component with data and title.

        Parameters:
            data (pd.DataFrame): Data containing 'skill_name' and 'rating' columns.
            title (str): Title of the radar chart.
        """
        self.data = data
        self.title = title

    def display(self):
        """Displays the radar chart in Streamlit."""
        # Remove duplicates based on 'skill_name'
        data = self.data.drop_duplicates(subset='skill_name')

        # Extract skill names and ratings
        categories = data['skill_name'].tolist()
        values = data['rating'].astype(float).tolist()  # Ensure ratings are floats for plotting

        # Append the first value to close the radar chart loop
        categories += [categories[0]]
        values += [values[0]]

        # Create the radar chart with Scatterpolar
        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Proficiency'
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