from assistant.stt import listen_once
from assistant.tts import speak
from assistant.skills import process_command


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
        reply = process_command(text)

        # Handle quit/exit
        if text.lower() in ["quit", "exit", "stop", "bye"]:
            speak("Goodbye!")
            break

        # If skills.py returned a string
        if isinstance(reply, str):
            speak(reply)
        else:
            # In case process_command returned dict (e.g., open_url)
            if "message" in reply:
                speak(reply["message"])

if __name__ == "__main__":
    main()
