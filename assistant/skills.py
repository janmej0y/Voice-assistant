import datetime
import webbrowser
import wikipedia
import os
import subprocess
import random
import platform
import pyjokes
import requests
import webbrowser
from .websites import websites

def open_website(command: str):
    for key, url in websites.items():
        if key in command.lower():
            webbrowser.open(url)
            return f"Opening {key}"
    return "Sorry, I don't know that website yet."

def process_command(cmd: str) -> str:
    text = cmd.lower()

    # --- Greetings / Small Talk ---
    if "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"

    elif "how are you" in text:
        return "I'm doing great, thank you! What about you?"

    elif "who are you" in text:
        return "I am your personal voice assistant, created with Python."

    # --- Time & Date ---
    elif "time" in text:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    elif "date" in text:
        return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"

    # --- Wikipedia ---
    elif "wikipedia" in text:
        try:
            topic = text.replace("wikipedia", "").strip()
            if topic:
                summary = wikipedia.summary(topic, sentences=2)
                return summary
            else:
                return "Please say a topic to search on Wikipedia."
        except Exception:
            return "Sorry, I could not fetch information from Wikipedia."

    

    # --- Jokes ---
    elif "joke" in text:
        return pyjokes.get_joke()

    # --- Quotes ---
    elif "quote" in text:
        quotes = [
            "The best way to predict the future is to invent it.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Dream big and dare to fail."
        ]
        return random.choice(quotes)

    # --- Music Player ---
    elif "play music" in text:
        music_dir = "C:\\Users\\Public\\Music"  # Change to your music folder
        try:
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                return f"Playing {song}"
            else:
                return "No songs found in your music folder."
        except:
            return "I couldn't find your music folder."

    # --- Notes ---
    elif "make a note" in text or "write a note" in text:
        with open("notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {cmd}\n")
        return "I have saved that note."

    elif "show notes" in text:
        try:
            with open("notes.txt", "r") as f:
                return f.read()
        except:
            return "You don't have any saved notes."

    # --- Reminders ---
    elif "remind me" in text:
        with open("reminders.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {cmd}\n")
        return "Reminder saved!"

    elif "show reminders" in text:
        try:
            with open("reminders.txt", "r") as f:
                return f.read()
        except:
            return "You don't have any reminders."

    # --- System Commands ---
    elif "open notepad" in text:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    elif "open calculator" in text:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    elif "open file explorer" in text or "open explorer" in text:
        subprocess.Popen("explorer")
        return "Opening File Explorer."

    elif "open chrome" in text:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            subprocess.Popen(chrome_path)
            return "Opening Google Chrome."
        else:
            return "Google Chrome is not installed in the default path."

    elif "open vs code" in text or "open code" in text:
        subprocess.Popen("code")
        return "Opening Visual Studio Code."

    elif "shutdown computer" in text:
        if platform.system() == "Windows":
            os.system("shutdown /s /t 5")
        return "Shutting down your computer in 5 seconds."

    elif "restart computer" in text:
        if platform.system() == "Windows":
            os.system("shutdown /r /t 5")
        return "Restarting your computer in 5 seconds."

    elif "open command prompt" in text or "open cmd" in text:
        subprocess.Popen("cmd")
        return "Opening Command Prompt."

    elif "open control panel" in text:
        subprocess.Popen("control")
        return "Opening Control Panel."

    elif "open task manager" in text:
        subprocess.Popen("taskmgr")
        return "Opening Task Manager."

    # --- Social Media & Web ---
    elif "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "open facebook" in text:
        webbrowser.open("https://www.facebook.com")
        return "Opening Facebook."
    elif "open instagram" in text:
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram."
    elif "open twitter" in text or "open x" in text:
        webbrowser.open("https://twitter.com")
        return "Opening Twitter."
    elif "open whatsapp" in text:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp Web."
    elif "open linkedin" in text:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn."
    elif "open reddit" in text:
        webbrowser.open("https://www.reddit.com")
        return "Opening Reddit."
    elif "open telegram" in text:
        webbrowser.open("https://web.telegram.org")
        return "Opening Telegram."
    elif "open snapchat" in text:
        webbrowser.open("https://www.snapchat.com")
        return "Opening Snapchat."
    elif "open pinterest" in text:
        webbrowser.open("https://www.pinterest.com")
        return "Opening Pinterest."
    elif "open github" in text:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    # --- Google Search Fallback ---
    elif "search" in text:
        query = text.replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching Google for {query}."
        else:
            return "Please tell me what to search."

    # --- Fallback ---
    else:
        return f"You said: {cmd}. I don't know that command yet."
# Alias so main.py works
handle_command = process_command
