# 🎙️ Python Voice Assistant  

A simple **voice assistant in Python** that can perform various tasks like telling the time, checking the weather, searching Wikipedia, opening apps, managing notes/reminders, playing music, and browsing the web.  

---

## 🚀 Features  

- ✅ **Greetings & Small Talk** – Responds to basic phrases like *hello*, *how are you*, *who are you*.  
- ✅ **Time & Date** – Tells the current system time and date.  
- ✅ **Weather Updates** – Fetches real-time weather using the [OpenWeatherMap API](https://openweathermap.org/).  
- ✅ **Wikipedia Search** – Gives a quick summary of any topic from Wikipedia.  
- ✅ **Jokes & Quotes** – Shares random jokes (via `pyjokes`) and motivational quotes.  
- ✅ **Music Player** – Plays random songs from your music folder.  
- ✅ **Notes & Reminders** – Save and read back notes/reminders.  
- ✅ **System Commands** – Open apps like **Notepad, Calculator, VS Code, Chrome, Explorer, CMD, Task Manager, Control Panel**, or even **shutdown/restart** your PC.  
- ✅ **Web Access & Social Media** – Opens sites like YouTube, Facebook, Instagram, WhatsApp Web, LinkedIn, GitHub, etc.  
- ✅ **Google Search** – Falls back to Google Search if no command matches.  

---

## 🛠️ Requirements  

Make sure you have **Python 3.8+** installed.  

### 🔹 Install Dependencies  

You can install everything at once:  

```bash
pip install -r requirements.txt
pip install requests wikipedia pyjokes SpeechRecognition pyttsx3
pip install pipwin
pipwin install pyaudio
pip install -r requirements_offline.txt

