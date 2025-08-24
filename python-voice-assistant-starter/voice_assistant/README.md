# Python Voice Assistant — Starter Project

This is a minimal, beginner-friendly voice assistant you can run in VS Code.

## What it can do
- Listen to your voice and understand basic commands (online STT via Google's free endpoint).
- Speak answers back using your system's voice (pyttsx3).
- Tell the time/date, open websites, and read brief Wikipedia summaries.

> If you prefer **offline speech recognition**, see the **Offline (Vosk) option** at the bottom.

---

## 1) Prerequisites
- Python 3.9+ installed
- VS Code + the **Python** extension by Microsoft
- A working microphone

---

## 2) Open in VS Code
1. Extract this zip somewhere like `C:\projects\voice_assistant` (Windows) or `~/projects/voice_assistant` (macOS/Linux).
2. In VS Code: **File → Open Folder…** and select the extracted `voice_assistant` folder.
3. VS Code will prompt to install the Python extension if missing—install it.

---

## 3) Create & select a virtual environment
Open the VS Code terminal (**Terminal → New Terminal**) and run:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

In VS Code, select the interpreter: **Ctrl/Cmd+Shift+P → "Python: Select Interpreter" → .venv**.

---

## 4) Install dependencies (Online STT build)
Install the common packages:
```bash
pip install -r requirements.txt
```

### Install PyAudio (microphone input) — platform-specific
PyAudio can be tricky. Use the method below for your OS:

**Windows:**
```powershell
pip install pipwin
pipwin install pyaudio
```

**macOS (with Homebrew):**
```bash
brew install portaudio
pip install pyaudio
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y portaudio19-dev
pip install pyaudio
```

If PyAudio still fails, jump to the **Offline (Vosk) option** which avoids PyAudio.

---

## 5) Run the assistant (Online STT)
From the terminal (venv activated):
```bash
python main.py
```

Say things like:
- “What’s the time?”
- “What’s the date?”
- “Open YouTube” / “Open Google” / “Open <site or topic>”
- “Search Wikipedia for Ada Lovelace”
- “Quit” / “Exit” / “Stop”

To list microphones and choose a specific one, run:
```bash
python tools/list_mics.py
```
Then set the device index in `assistant/stt.py` (see comments in that file).

---

## 6) Troubleshooting
- **No speech detected / wrong mic:** Use `tools/list_mics.py` to find the correct device index and set it in `assistant/stt.py`.
- **SpeechRecognition API error:** You need internet for the default recognizer. If you want offline, use Vosk below.
- **Audio permission (macOS):** Give Terminal/VS Code mic access in System Settings → Privacy & Security → Microphone.
- **Windows execution policy:** If activation fails in PowerShell, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once as admin.

---

## 7) Project structure
```text
voice_assistant/
├─ assistant/
│  ├─ __init__.py
│  ├─ stt.py             # Listen & transcribe (SpeechRecognition + PyAudio)
│  ├─ tts.py             # Speak (pyttsx3)
│  └─ skills.py          # Simple command handling (time, date, open, wikipedia)
├─ tools/
│  └─ list_mics.py       # Utility to list available microphone devices
├─ main.py               # Entry point for the online STT version
├─ requirements.txt      # Common deps (except PyAudio which is OS-specific)
├─ requirements_offline.txt  # Deps for the offline (Vosk) option
├─ main_offline.py       # Entry point for the offline STT version (Vosk)
└─ README.md
```

---

## 8) Offline (Vosk) option (no internet; avoids PyAudio)
1) Install offline requirements:
```bash
pip install -r requirements_offline.txt
```

2) Download a small English model (~50–60 MB). For example: `vosk-model-small-en-us-0.15` from the Vosk project page. Extract it to:
```text
voice_assistant/models/vosk-model-small-en-us-0.15
```

3) Run:
```bash
python main_offline.py
```

> Tip: The offline example streams the mic until it detects a full utterance, then returns the transcript.

---

## 9) Customize skills
Edit `assistant/skills.py` to add your own commands. You can call APIs, control smart devices, send emails, etc.

Happy building! 🎙️🤖
