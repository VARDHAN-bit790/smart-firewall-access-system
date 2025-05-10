import tkinter as tk
from tkinter import ttk
import threading
import time
import biometric  # Assuming this is the file that contains the biometric verification functions

# Create the main application window
root = tk.Tk()
root.title("Smart Access Firewall")
root.geometry("600x400")
root.config(bg="#282828")

# ==== STYLE AND EFFECTS ====

# Apply glow effect on the title label
def apply_glow(label):
    def toggle_glow():
        if label["fg"] == "#eee":
            label.config(fg="#fff")
        else:
            label.config(fg="#eee")
        root.after(500, toggle_glow)  # Toggle glow effect every 500ms
    toggle_glow()

# Apply fade effect on result labels
def fade_out(label, interval=1000):
    label.config(fg="gray")
    root.after(interval, fade_in, label)

def fade_in(label, interval=1000):
    label.config(fg="blue")
    root.after(interval, fade_out, label)

# ==== GUI ELEMENTS ====

# Title label with glow effect
title_label = tk.Label(root, text="Smart Access Firewall", font=("Helvetica Neue", 24, "bold"), fg="#eee", bg="#282828")
title_label.pack(pady=20)
apply_glow(title_label)

# Frame for buttons and status
frame = tk.Frame(root, bg="#282828")
frame.pack(pady=20)

# Verification result label with fade effect
result_label = tk.Label(root, text=" ", font=("Arial", 14, "italic"), fg="blue", bg="#282828")
result_label.pack(pady=20)
fade_in(result_label)

# Status label for step indication
status_label = tk.Label(root, text="Waiting for action...", font=("Arial", 12), fg="lightgray", bg="#282828")
status_label.pack(pady=10)

# Progress bar for feedback
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress.pack(pady=10)

# ==== BUTTONS ====

def start_verification():
    # Reset the result label and show progress
    result_label.config(text="Verifying Face and Voice...")
    status_label.config(text="Starting Face Verification...")
    progress.start()

    # Face Verification
    if biometric.recognize_face():
        result_label.config(text="Face Verified. Proceeding to Voice Check...")
        status_label.config(text="Face Verified. Proceeding to Voice Check...")

        # Voice Verification
        if biometric.verify_voice():
            result_label.config(text="✅ FINAL STATUS: ACCESS GRANTED")
            status_label.config(text="Access Granted! Welcome!")
        else:
            result_label.config(text="❌ FINAL STATUS: ACCESS DENIED (Voice mismatch)")
            status_label.config(text="Voice mismatch! Access Denied.")
    else:
        result_label.config(text="❌ FINAL STATUS: ACCESS DENIED (Face not recognized)")
        status_label.config(text="Face not recognized! Access Denied.")

    progress.stop()

# Create a button to start the biometric verification
verify_button = tk.Button(frame, text="Start Verification", command=lambda: threading.Thread(target=start_verification).start(), 
                           font=("Arial", 12), fg="#fff", bg="#007BFF", relief="solid", padx=20, pady=10)
verify_button.grid(row=0, column=0, padx=20)

# Add a quit button
quit_button = tk.Button(frame, text="Quit", command=root.quit, font=("Arial", 12), fg="#fff", bg="#FF4136", relief="solid", padx=20, pady=10)
quit_button.grid(row=0, column=1, padx=20)

# ==== MAIN LOOP ====

if __name__ == "__main__":
    root.mainloop()
