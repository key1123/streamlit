
"""
main.py

Modular Streamlit app for Neuro Buddy AI, with Gemma 3n analysis and Sensory Tools.
How to use:
- Place this and all module files in the same directory.
- Run `ollama run gemma` in a terminal before starting.
- Start app: streamlit run main.py

Navigation:
- Registration required first (forced).
- After registration, navigation is via buttons on the User Home page.

Each page is modular; expand as needed!
"""

import streamlit as st
from registration import registration_page
from routine_scheduler import routine_scheduler_page
from user_homepage import user_homepage
from sensory_tools import sensory_tools_page  # <-- Make sure sensory_tools.py exists

# Only show Registration and Home in sidebar for clarity
SIDEBAR_PAGES = {
    "Registration": registration_page,
    "User Home": user_homepage,
}

# Internal routing for all pages (not all are visible in sidebar)
ALL_PAGES = {
    "Registration": registration_page,
    "User Home": user_homepage,
    "Routine Scheduler": routine_scheduler_page,
    "Sensory Tools": sensory_tools_page,
}

def main():
    st.set_page_config(page_title="Neuro Buddy AI", layout="centered")

    # Always require registration first
    if not st.session_state.get("registered"):
        st.session_state["page"] = "Registration"
    elif "page" not in st.session_state:
        st.session_state["page"] = "User Home"

    st.sidebar.title("Neuro Buddy AI")
    st.sidebar.info("Use sidebar to return to Registration or Home at any time.")

    # Sidebar navigation (Registration/Home only)
    sidebar_selection = st.sidebar.radio("Go to:", list(SIDEBAR_PAGES.keys()))
    if sidebar_selection != st.session_state.get("page"):
        st.session_state["page"] = sidebar_selection

    # Page router: show current page (set by sidebar or by navigation buttons)
    current_page = st.session_state.get("page", "Registration")
    if current_page in ALL_PAGES:
        ALL_PAGES[current_page]()
    else:
        st.error(f"Page '{current_page}' not found.")

if __name__ == "__main__":
    main()
