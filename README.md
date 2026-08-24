# AI Meeting Summarizer
It is an end-to-end meeting summarizer in which we upload the audio files and then using Groq's fast whisper ASR engine the summarizer generates audio summary , key decisions , and actionable tasks via `openai/gpt-oss-120b`.

---

## Project Overview
Taking notes by hand is often slow, incomplete and also inconsistent. By using this meeting summarizer the work load decreases as you just have to record audio and it generates the post meeting workflow by:
1. Converting audio files into accurate text transcripts.
2. Finding the main recap, final decisions, and to-do lists from the meeting logs.
3. Presenting the results in an interactive web interface built with Streamlit.

---

## Tech Stack
* **Frontend UI:** Streamlit
* **ASR (Speech-to-Text) Model:** `whisper-large-v3` (via Groq API)
* **LLM Model:** `openai/gpt-oss-120b` (via Groq API)
* **Language & Runtime:** Python 3.10+
* **Environment Management:** `python-dotenv`

---

## How to run
* Web interface:- (python -m streamlit run streamlit_app.py)
* Command Line Interface (CLI):-(python app.py)

## DEMO
[Demo of running the command in VS code](https://drive.google.com/file/d/1FKZ3EMaaJd843RpnwhBZi6t9ICxfXUG8/view?usp=sharing)
[Demo of how the it takes input and generate output ](https://drive.google.com/file/d/1esr26i6qqg0odSJ3go2drTjGCvD43DAa/view?usp=sharing)


## Project Structure 
```text
meeting-summarizer/
├── .gitignore                  # Git exclusion settings (.env, cache, venv)
├── app.py                      # Core CLI processing script
├── streamlit_app.py            # Web application interface
├── MeetingSummarizerAudio1.m4a # Sample audio test file
└── README.md                   # Project documentation


