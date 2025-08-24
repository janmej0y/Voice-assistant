import speech_recognition as sr

# If you have multiple microphones, set a specific device index here.
# To discover indexes, run: python tools/list_mics.py
DEVICE_INDEX = None  # e.g., 0 or 1

def listen_once(timeout: float = 5.0, phrase_time_limit: float = 8.0) -> str | None:
    """Listen from the default mic once and return recognized text (or None).

    Uses Google's free web API via SpeechRecognition. Requires internet.
    Raises RuntimeError if the API is unreachable.
    """
    r = sr.Recognizer()
    if DEVICE_INDEX is None:
        source = sr.Microphone()
    else:
        source = sr.Microphone(device_index=DEVICE_INDEX)

    with source as mic:
        print("🎙️ Listening...")
        r.adjust_for_ambient_noise(mic, duration=0.6)
        try:
            audio = r.listen(mic, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return None

    try:
        # You can change language if needed, e.g., 'en-IN' for Indian English.
        text = r.recognize_google(audio, language='en-IN')
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        raise RuntimeError(f"Speech API error: {e}")
