from assistant.stt import listen_once
from assistant.tts import speak
from assistant.skills import handle_command

def main():
    speak("Hello! I'm ready. Say something after the beep. Say quit to exit.")
    while True:
        try:
            text = listen_once()
        except RuntimeError as e:
            print(f"[Speech error] {e}")
            speak("There was a problem with speech recognition.")
            continue

        if not text:
            print("Didn't catch that. Try again...")
            speak("I didn't catch that. Please repeat.")
            continue

        print(f"You said: {text}")
        reply = handle_command(text)
        if reply == "__EXIT__":
            speak("Goodbye!")
            break
        speak(reply)

if __name__ == "__main__":
    main()
