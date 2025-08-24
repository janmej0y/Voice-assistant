import pyttsx3

_engine = None

def _ensure_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        # You can tweak speaking rate and volume here
        _engine.setProperty('rate', 180)  # words per minute
        _engine.setProperty('volume', 1.0)  # 0.0 to 1.0

def speak(text: str) -> None:
    """Speak the given text out loud."""
    _ensure_engine()
    _engine.say(text)
    _engine.runAndWait()
