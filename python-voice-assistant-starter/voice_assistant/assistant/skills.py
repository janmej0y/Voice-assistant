import datetime
import webbrowser
import wikipedia

def handle_command(cmd: str) -> str:
    """Very simple command router. Extend as you like."""
    text = cmd.lower().strip()

    # Exit intents
    if any(x in text for x in ("quit", "exit", "stop", "goodbye", "bye")):
        return "__EXIT__"

    # Time & date
    if "time" in text:
        now = datetime.datetime.now()
        return now.strftime("It's %I:%M %p.")

    if "date" in text or "day" in text:
        today = datetime.datetime.now()
        return today.strftime("Today is %A, %B %d, %Y.")

    # Open websites
    if text.startswith("open "):
        target = text.split("open ", 1)[1].strip()
        mapping = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
        }
        url = mapping.get(target, f"https://www.google.com/search?q={target}")
        webbrowser.open(url)
        return f"Opening {target}."

    # Wikipedia quick summaries
    if "wikipedia" in text or text.startswith("who is") or text.startswith("what is"):
        topic = (
            text.replace("search wikipedia for", "")
                .replace("wikipedia", "")
                .replace("who is", "")
                .replace("what is", "")
                .strip()
        )
        try:
            wikipedia.set_lang("en")
            summary = wikipedia.summary(topic or text, sentences=2, auto_suggest=True, redirect=True)
            return summary
        except Exception:
            return f"Sorry, I couldn't fetch a Wikipedia summary for '{topic or text}'."

    # Default fallback
    return f"You said: {cmd}"


# Simple loop to test it
if __name__ == "__main__":
    print("Voice Assistant (type 'quit' to exit)")
    while True:
        command = input(">>> ")
        response = handle_command(command)
        if response == "__EXIT__":
            print("Goodbye!")
            break
        print(response)
