"""
gui_handle.py

Central app navigation and main homepage.
- Launches the registration wizard on startup.
- Shows a personalized homepage after registration.
- User can open the routine scheduler GUI from here.

How this code works:
- MainApp is a Tk root window, but starts out hidden.
- RegistrationWizard is run first; on complete, home is shown.
- User info and chosen accommodations are shown on the homepage.
- "Go to Routine Scheduler" opens a Toplevel window.
"""

import streamlit as st
from routine_scheduler import routine_scheduler_page

def home_page():
    user = st.session_state.get("user", {})
    st.header(f"Hello, {user.get('name','')}!")
    st.write("Welcome to Neuro Buddy AI. Here’s your info:")
    st.write(f"**Phone:** {user.get('phone','')}")
    st.write(f"**Email:** {user.get('email','')}")
    st.write("**Accommodations:**")
    for acc in user.get("accommodations", []):
        st.write(f"- {acc}")
    if st.button("Go to Routine Scheduler"):
        st.session_state["page"] = "routine_scheduler"
