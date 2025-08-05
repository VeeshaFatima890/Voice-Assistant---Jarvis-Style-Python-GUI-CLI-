# 🎙️ Voice Assistant - Jarvis Style (Python GUI + CLI)

A lightweight, offline-capable voice assistant built using Python. Inspired by Jarvis from Iron Man, this assistant can recognize speech, speak responses, search Wikipedia, play YouTube videos, tell the time, and more.

---

## 🚀 Features

- 🎤 Voice Command Recognition (using `speech_recognition`)
- 🔊 Text-to-Speech (using `pyttsx3`)
- 🌐 Wikipedia Search
- 📺 Play YouTube Videos via Voice
- 🕒 Tell the Current Time
- 🔎 Google Search via Voice
- ❌ Exit using "bye", "exit", or "stop"
- 🖼️ Optional GUI version (Tkinter or Streamlit)

---

## 🛠️ Tech Stack

| Component       | Library Used         |
|----------------|----------------------|
| Voice Input     | `speech_recognition` |
| Voice Output    | `pyttsx3`            |
| Search          | `wikipedia`, `pywhatkit` |
| Time/Date       | `datetime`           |
| Python Version  | `>=3.8`              |

---

## 📦 Project Structure
voice_assistant_project/
├── voice_assistant.py # Core logic (CLI version)
├── jarvis_gui.py # GUI version (Tkinter/Streamlit)
├── README.md # Project overview
├── requirements.txt # Required Python packages

---

## 🖥️ How to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/voice_assistant_project.git
   cd voice_assistant_project
   python voice_assistant.py
   python jarvis_gui.py
---------------------------------------
Commands You Can Say
What's the time?

Search [topic] on Wikipedia

Play [song name] on YouTube

Search [query] on Google

Exit / Stop / Bye
---------------------------------------
Libraries
pip install SpeechRecognition pyttsx3 wikipedia pywhatkit


Developed by Veesha Fatima — Python & AI Enthusiast 💻
Built as a fun and educational voice assistant project.
---

This project is licensed under the MIT License.
Feel free to use, modify, and contribute!

Let me know if you're including GUI (e.g., `jarvis_gui.py` with Tkinter or Streamlit), and I’ll adjust the README accordingly.



