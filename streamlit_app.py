import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.set_page_config(page_title="AI Meeting Summarizer", page_icon="🎙️")
st.title("🎙️ AI Meeting Summarizer")
st.write("Upload your meeting audio to generate transcripts, decisions, and action items.")

uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "m4a", "wav"])

if uploaded_file is not None:
    st.audio(uploaded_file)
    
    if st.button("Generate Summary", type="primary"):
        # Save temporary file for API access
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            with st.spinner("1/2 Transcribing audio with Whisper..."):
                with open(temp_path, "rb") as file:
                    transcription = client.audio.transcriptions.create(
                        file=(file.name, file.read()),
                        model="whisper-large-v3",
                    )
                transcript = transcription.text

            with st.spinner("2/2 Extracting key decisions and action items..."):
                prompt = f"""
                Analyze the following meeting transcript. Provide:
                1. Executive Summary
                2. Key Decisions Made
                3. Action Items (formatted as: - [ ] **Owner**: Task - Deadline)

                Transcript:
                {transcript}
                """
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[{"role": "user", "content": prompt}],
                )
                summary = response.choices[0].message.content

            st.success("Processing complete!")
            
            st.subheader("📋 Executive Summary & Action Items")
            st.markdown(summary)
            
            with st.expander("View Full Raw Transcript"):
                st.write(transcript)

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)