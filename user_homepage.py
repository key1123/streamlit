
"""
user_homepage.py

User's home page after registration.

Contains buttons for navigating to main tools.
"""

import streamlit as st

def user_homepage():
    user = st.session_state.get("user", {})
    st.title(f"Welcome, {user.get('name', 'User')}!")
    st.write("Your Neuro Buddy AI home. Use the buttons below to navigate:")

    st.write("**Your accommodations:**")
    for acc in user.get("accommodations", []):
        st.write(f"- {acc}")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Routine Scheduler"):
            st.session_state["page"] = "Routine Scheduler"
    with col2:
        if st.button("Sensory Overload Detection & Calming Tools"):
            st.session_state["page"] = "Sensory Tools"
