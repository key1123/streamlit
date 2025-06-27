"""
gemma3n.py

Gemma 3n model utility for text, PDF, image, and audio analysis.
You must have Ollama running locally with 'ollama run gemma'.

How to use:
- Import and call analyze_text, analyze_pdf, analyze_image, or analyze_audio from this file.
"""

import requests
from PIL import Image
import fitz  # PyMuPDF

def call_gemma(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma", "prompt": prompt}
        )
        if response.status_code == 200:
            rjson = response.json()
            return rjson.get("response") or "[No response]"
        return f"[Gemma 3n error: {response.status_code}]"
    except Exception as e:
        return f"[Gemma 3n error: {e}]"

def analyze_text(text):
    prompt = f"Summarize or analyze this routine/task for accessibility: {text}"
    return call_gemma(prompt)

def analyze_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        if doc.page_count > 0:
            page = doc.load_page(0)
            text = page.get_text()
        prompt = f"Summarize this PDF content for a routine/task: {text}"
        return call_gemma(prompt)
    except Exception as e:
        return f"[PDF error: {e}]"

def analyze_image(file):
    try:
        image = Image.open(file)
        prompt = "Describe the contents of this image for accessibility."
        # Optionally, you can convert image to base64 if your model supports images
        # For now, ask user to enter details or use OCR separately if needed.
        return "[Image analysis placeholder: integrate with image LLM or OCR if needed]"
    except Exception as e:
        return f"[Image error: {e}]"

def analyze_audio(file):
    # For now, placeholder—if you add speech-to-text, plug in here
    return "[Audio analysis placeholder: integrate with STT and Gemma 3n as needed]"
