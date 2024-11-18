import streamlit as st
import re


class SignUpFormComponent:
    """Component to handle a waitlist sign-up form, including display toggling and validation."""

    def __init__(self):
        # Initialize session state keys for form control and success tracking
        if "show_form" not in st.session_state:
            st.session_state["show_form"] = False
        if "form_submitted" not in st.session_state:
            st.session_state["form_submitted"] = False

    @staticmethod
    def is_valid_email(email):
        """Validates email format using regex."""
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w{2,3}$"
        return re.match(email_regex, email) is not None

    def display(self):
        """Display the sign-up form if visible, handle submission, and toggle visibility."""

        # Show the button to display form if form has not been submitted
        if not st.session_state["show_form"] and not st.session_state["form_submitted"]:
            if st.button("Sign Up to Waiting List!"):
                st.session_state["show_form"] = True
                st.rerun()

        # Display the form when "show_form" is True
        if st.session_state["show_form"]:
            with st.form("waitlist_form"):
                name = st.text_input("Name", placeholder="Enter your full name")
                email = st.text_input("Email", placeholder="Enter your email address")
                message = st.text_area("Message", placeholder="Any additional comments or requests?")

                # Submit button within the form
                submitted = st.form_submit_button("Submit")

                if submitted:
                    # Validation checks
                    if not name:
                        st.error("Name is a required field.")
                    elif not email or not self.is_valid_email(email):
                        st.error("Please enter a valid email address.")
                    else:
                        # On successful submission, show success message and hide form
                        st.success("Thank you! You have successfully signed up for the waitlist.")
                        st.session_state["form_submitted"] = True
                        st.session_state["show_form"] = False
                        st.rerun()  # Refresh to hide the form after submission

        # Reset the form after submission, allowing users to re-sign up if needed
        if st.session_state["form_submitted"]:
            if st.button("Thanks for Submitting"):
                st.session_state["form_submitted"] = False
                st.rerun()
                