"""

Registration page for Neuro Buddy AI.
Handles:
- Name, phone, email entry (Step 1)
- Accommodation selection (Step 2)
- Shows summary on completion (Step 3)

How to use:
- Import and call registration_page() from main.py.
- Advances user state in st.session_state["step"].
"""

"""
registration.py

Registration page for Neuro Buddy AI.
Only handles registration/accommodation choices.

Navigation to tools is handled on the user home page.
"""

import streamlit as st

ACCOMMODATIONS = [
    "Screen reader / text-to-speech support",
    "Large text / high-contrast mode",
    "Step-by-step task breakdown",
    "Gentle reminders for transitions",
    "Calming prompts during overload",
    "Private mode",
    "Offline-only mode",
    "Trusted contact notifications",
]

def registration_page():
    st.title("Welcome to Neuro Buddy AI")
    st.markdown("Your supportive, personalized assistant for routines and wellness.")
    st.subheader("Registration")
    with st.form("reg_form"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        submit = st.form_submit_button("Register")
    if submit:
        if not name or not phone or not email:
            st.warning("Please enter your name, phone, and email.")
        elif "@" not in email or "." not in email.split("@")[-1]:
            st.warning("Please enter a valid email address.")
        elif not phone.replace("-", "").replace(" ", "").isdigit() or len(phone) < 7:
            st.warning("Please enter a valid phone number.")
        else:
            st.session_state["user"] = {"name": name, "phone": phone, "email": email}
            st.session_state["step"] = 2

    if st.session_state.get("step") == 2:
        st.title("Step 2: Pick Your Needed Accommodations")
        st.write("Select any supports you think you’ll need. You can change these anytime in settings.")
        chosen = st.multiselect("Accommodations:", ACCOMMODATIONS)
        if st.button("Finish Registration"):
            st.session_state["user"]["accommodations"] = chosen
            st.session_state["registered"] = True
            st.success("Registration complete! Go to your Home page from the sidebar to get started.")
