import os, json, queue
from vosk import Model, KaldiRecognizer
import sounddevice as sd

# Set VOSK_MODEL_PATH env var to override default location
MODEL_PATH = os.getenv("VOSK_MODEL_PATH", "models/vosk-model-small-en-us-0.15")

def _load_model() -> Model:
    if not os.path.isdir(MODEL_PATH):
        raise RuntimeError(
            f"Vosk model not found at '{MODEL_PATH}'. "
            "Download a model (e.g., 'vosk-model-small-en-us-0.15') and extract it there, "
            "or set the VOSK_MODEL_PATH environment variable."
        )
    return Model(MODEL_PATH)

def listen_once_offline(samplerate: int = 16000) -> str | None:
    """Stream mic audio and return one utterance as text (offline via Vosk)."""
    model = _load_model()
    rec = KaldiRecognizer(model, samplerate)
    q: queue.Queue[bytes] = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(bytes(indata))

    print("🎙️ Listening (offline)… speak now.")
    try:
        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                               channels=1, callback=callback):
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    try:
                        text = json.loads(result).get("text", "")
                    except Exception:
                        text = ""
                    return text if text else None
                # else: partials are available via rec.PartialResult()
    except Exception as e:
        print(f"[Audio error] {e}")
        return None
