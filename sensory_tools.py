"""
sensory_tools.py

Sensory Overload Detection & Calming Tools page.
Lets the user analyze surroundings via text, image, audio, or (optionally) video,
using Gemma 3n for feedback and calming suggestions.

How to use:
- Import and call sensory_tools_page() from main.py.
"""

import streamlit as st
from PIL import Image
from gemma3n import call_gemma

def sensory_tools_page():
    st.title("Sensory Overload Detection & Calming Tools")
    st.write(
        "Upload or describe your surroundings. Neuro Buddy AI will use Gemma 3n to help you identify possible sensory triggers and suggest calming strategies."
    )

    st.subheader("Describe your current environment (Text)")
    with st.form("text_env_form"):
        description = st.text_area("Describe what you see, hear, or feel")
        submit = st.form_submit_button("Analyze Text")
    if submit and description:
        with st.spinner("Analyzing with Gemma 3n..."):
            prompt = (
                "You are a helpful assistant. A user describes their current environment."
                " Analyze it for possible sensory overload triggers (e.g., light, sound, crowding, screens, smells) and suggest calming tips:"
                f"\n\nUser description: {description}"
            )
            ai_result = call_gemma(prompt)
        st.success("Gemma 3n Suggestions:")
        st.write(ai_result)

    st.subheader("Upload an Image (Photo of Your Surroundings)")
    image_file = st.file_uploader("Image", type=["jpg", "jpeg", "png"])
    image_analysis = ""
    if image_file:
        img = Image.open(image_file)
        st.image(img, caption="Your Uploaded Environment", use_column_width=True)
        if st.button("Analyze Image"):
            prompt = (
                "You are a helpful assistant. This is a photo of a user's environment."
                " Imagine and describe possible sensory overload triggers in the image, and suggest calming strategies:"
            )
            # For real image LLM, you'd send the image; here, ask the user to describe OR just use placeholder
            image_analysis = call_gemma(prompt + "\n\n[Image content analysis placeholder]")
            st.success("Gemma 3n Image Suggestions:")
            st.write(image_analysis)

    st.subheader("Upload an Audio File (Sounds of Your Surroundings)")
    audio_file = st.file_uploader("Audio (WAV/MP3, short recording)", type=["wav", "mp3"])
    if audio_file and st.button("Analyze Audio"):
        # This is a placeholder, since actual audio-to-text is not built in here
        prompt = (
            "You are a helpful assistant. The user has uploaded an audio clip of their surroundings."
            " Based on the sound (which may include voices, traffic, appliances, etc), imagine and suggest what might cause sensory overload and give calming tips."
        )
        ai_audio = call_gemma(prompt + "\n\n[Audio content analysis placeholder]")
        st.success("Gemma 3n Audio Suggestions:")
        st.write(ai_audio)

    st.subheader("Upload a Video (Optional, Experimental)")
    video_file = st.file_uploader("Video (MP4, first frame only)", type=["mp4"])
    if video_file and st.button("Analyze Video (First Frame)"):
        # Note: Streamlit doesn't support video frame extraction natively;
        # for real apps use OpenCV, here just a placeholder prompt.
        prompt = (
            "You are a helpful assistant. The user uploaded a video of their environment."
            " Based on the first video frame, describe possible sensory triggers and give calming advice."
        )
        ai_video = call_gemma(prompt + "\n\n[Video content analysis placeholder]")
        st.success("Gemma 3n Video Suggestions:")
        st.write(ai_video)

    # Info if no input
    if not (description or image_file or audio_file or video_file):
        st.info("You can describe your environment, or upload an image, audio, or video for analysis.")
