
"""
user_homepage.py

User's home page after registration.

Contains buttons for navigating to main tools.
"""

import streamlit as st

def user_homepage():
    user = st.session_state.get("user", {})
    st.title(f"Welcome, {user.get('name', 'User')}!")
    st.write("Choose a tool to get started:")

    if st.button("Routine Scheduler"):   # <-- key removed
        st.session_state["page"] = "Routine Scheduler"
        return

    if st.button("Sensory Overload Detection & Calming Tools"):  # <-- key removed
        st.session_state["page"] = "Sensory Tools"
        return
