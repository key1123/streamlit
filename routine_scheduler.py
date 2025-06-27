"""
routine_scheduler.py

Routine Scheduler page for Neuro Buddy AI.
Allows task entry by text, image/PDF, and voice, and uses Gemma 3n for AI analysis.

How to use:
- Import and call routine_scheduler_page() from main.py.

Requires:
- gemma3n.py for AI routines (imported as needed).
"""

import streamlit as st
from gemma3n import analyze_text, analyze_pdf, analyze_image, analyze_audio

def routine_scheduler_page():
    st.title("Routine Scheduler")

    if "routine_list" not in st.session_state:
        st.session_state["routine_list"] = []

    st.subheader("Add Task (Text)")
    with st.form("text_task_form"):
        task = st.text_input("Task")
        time = st.text_input("Time (HH:MM, 24h)")
        submit = st.form_submit_button("Add Text Task")
    if submit and task and time:
        st.session_state["routine_list"].append({"task": task, "time": time, "mode": "text"})
        st.success(f"Added: {time} | {task}")

    st.subheader("Add Task (Image/PDF)")
    file = st.file_uploader("Upload Image or PDF", type=["jpg", "jpeg", "png", "bmp", "pdf"])
    pdf_image_task_time = st.text_input("Time for Image/PDF Task (HH:MM, 24h)")
    if st.button("Analyze & Add File Task"):
        if file and pdf_image_task_time:
            if file.type == "application/pdf":
                summary = analyze_pdf(file)
            else:
                summary = analyze_image(file)
            st.session_state["routine_list"].append({
                "task": summary,
                "time": pdf_image_task_time,
                "mode": "image/pdf"
            })
            st.success(f"Added: {pdf_image_task_time} | {summary[:30]}...")
        else:
            st.warning("Upload a file and enter a time.")

    st.subheader("Add Task (Voice/Audio)")
    audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])
    audio_task_time = st.text_input("Time for Audio Task (HH:MM, 24h)")
    if st.button("Analyze & Add Audio Task"):
        if audio_file and audio_task_time:
            summary = analyze_audio(audio_file)
            st.session_state["routine_list"].append({
                "task": summary,
                "time": audio_task_time,
                "mode": "audio"
            })
            st.success(f"Added: {audio_task_time} | {summary[:30]}...")
        else:
            st.warning("Upload an audio file and enter a time.")

    st.subheader("Your Routine List")
    if st.session_state["routine_list"]:
        for item in sorted(st.session_state["routine_list"], key=lambda x: x['time']):
            st.write(f"{item['time']} | {item['task']} | Mode: {item['mode']}")
    else:
        st.info("No tasks scheduled yet.")
