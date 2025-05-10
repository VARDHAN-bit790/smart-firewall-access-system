import speech_recognition as sr
import os

VOICE_FOLDER = "voice_data"
TRIGGER_WORD = "vinu"  # You can customize this

def recognize_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("[INFO] Listening for voice verification...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio)
            print(f"[INFO] Recognized Speech: {recognized_text}")

            if TRIGGER_WORD.lower() in recognized_text.lower():
                return True, recognized_text
            else:
                return False, recognized_text

        except sr.UnknownValueError:
            return False, "Could not understand the voice."
        except sr.RequestError:
            return False, "Speech recognition service error."