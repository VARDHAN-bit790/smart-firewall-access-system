import cv2
import os
import numpy as np
from deepface import DeepFace
from resemblyzer import VoiceEncoder, preprocess_wav
import sounddevice as sd
import scipy.io.wavfile
from pathlib import Path
from PIL import Image

# ==== FACE VERIFICATION ====

def recognize_face():
    face_folder = "face_data"
    webcam = cv2.VideoCapture(0)
    print("[INFO] Face verification started...")

    result = False
    while True:
        ret, frame = webcam.read()
        if not ret:
            break
        cv2.imshow("Face Verification - Press 'q' to Quit", frame)

        for filename in os.listdir(face_folder):
            known_face_path = os.path.join(face_folder, filename)
            try:
                result_face = DeepFace.verify(frame, known_face_path, enforce_detection=False)
                if result_face['verified']:
                    print(f"[✔] Face Verified: {filename.split('.')[0]}")
                    result = True
                    break
            except Exception as e:
                print(f"[!] Face verification error: {e}")

        if result or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()
    return result

# ==== VOICE VERIFICATION ====

voice_dir = Path("voice_data")
enrolled_voice_path = voice_dir / "enrolled_voice.wav"
temp_voice_path = voice_dir / "temp_voice.wav"
voice_dir.mkdir(exist_ok=True)
encoder = VoiceEncoder()

def record_voice(path, message):
    print(message)
    fs = 16000
    duration = 5
    recording = sd.rec(int(fs * duration), samplerate=fs, channels=1)
    sd.wait()
    scipy.io.wavfile.write(path, fs, recording)

def verify_voice():
    if not enrolled_voice_path.exists():
        print("[x] No enrolled voice found. Please run enrollment first.")
        return False

    record_voice(temp_voice_path, "[🎤] Speak for voice verification...")
    try:
        enrolled = preprocess_wav(enrolled_voice_path)
        test = preprocess_wav(temp_voice_path)

        embed_enrolled = encoder.embed_utterance(enrolled)
        embed_test = encoder.embed_utterance(test)

        similarity = np.dot(embed_enrolled, embed_test)
        print(f"[🧠] Voice Similarity Score: {similarity:.2f}")

        return similarity > 0.75
    except Exception as e:
        print(f"[!] Voice verification error: {e}")
        return False

# ==== VOICE ENROLLMENT ====

def enroll_voice():
    print("[🎙️] Please speak to enroll your voice...")
    record_voice(enrolled_voice_path, "[🎙️] Speak to enroll your voice...")
    print("[✅] Voice enrolled and saved.")
    return True

