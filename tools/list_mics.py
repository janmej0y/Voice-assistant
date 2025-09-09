import speech_recognition as sr

if __name__ == "__main__":
    names = sr.Microphone.list_microphone_names()
    for i, name in enumerate(names):
        print(f"{i}: {name}")
    if not names:
        print("No microphones found. Check your audio settings and drivers.")
