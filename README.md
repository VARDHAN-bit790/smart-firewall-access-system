# 🔐 Biometric Authentication Desktop App (Face + Voice)

A smart desktop firewall application built using Python that authenticates users through both face and voice biometrics. If either the face or voice does not match the enrolled profile, access is denied.

## 🚀 Features

- ✅ **Face Recognition** using DeepFace  
- 🎤 **Voice Recognition** using Resemblyzer  
- 💻 **Interactive GUI** with modern, glowing effects  
- 🧠 **AI-based matching** with similarity scoring  
- 🔐 **Smart Firewall** that grants access only on successful verification  

## 📁 Directory Structure

biometric-auth-app/
│
├── app.py # Main app with GUI
├── biometric_check.py # Face and voice recognition logic
├── face_data/ # Folder containing enrolled face images
├── voice_data/ # Folder for enrolled and temporary voice samples
├── assets/ # (Optional) Images, icons, logos for GUI
├── styles.css # CSS file for GUI effects
├── requirements.txt # Required Python packages
└── README.md # This file


## 🛠️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/biometric-auth-app.git
cd biometric-auth-app
2. Install Required Packages
Create a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install all dependencies:

pip install -r requirements.txt
3. Run the Application

python app.py
📸 Enroll Face and Voice
Save your face image (e.g., vardhan.jpg) into the face_data/ directory.

For voice enrollment, follow the on-screen instructions when prompted.

🧪 Libraries Used
DeepFace – for facial recognition

Resemblyzer – for voice matching

OpenCV – for camera feed

Tkinter – for GUI interface

SoundDevice, SciPy – for audio input/output

NumPy, Pillow, Pathlib – for data handling and UI

📌 Notes
Ensure webcam and microphone are properly connected and accessible.

The similarity threshold for voice authentication is 0.75 (can be tuned).

System is intended for local desktop authentication only.

💡 Future Enhancements
User-friendly enrollment UI

Fingerprint or iris scan integration

Admin panel for access logs

Support for multiple user profiles
