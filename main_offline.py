from assistant.stt_vosk import listen_once_offline
from assistant.tts import speak
from assistant.skills import process_command

def main():
    speak("Offline mode. I'm listening. Say quit to exit.")
    while True:
        text = listen_once_offline()
        if not text:
            print("No speech detected. Try again.")
            continue
        print(f"You said: {text}")
        reply = process_command(text)
        if reply == "__EXIT__":
            speak("Goodbye!")
            break
        speak(reply)

if __name__ == "__main__":
    main()
