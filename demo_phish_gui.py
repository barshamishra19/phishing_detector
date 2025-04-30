import joblib  
import tkinter as tk
from tkinter import messagebox
from features import extract_features

MODEL_PATH = "models/phishing_detector_model.pkl"

def load_model(path=MODEL_PATH):
    """Load the phishing detector model with joblib."""
    return joblib.load(path)

def on_check():
    url = entry.get().strip()
    if not url:
        return messagebox.showwarning("Input needed", "Please enter a URL.")
    feats = extract_features(url)
    pred = model.predict([feats])[0]
    conf = model.predict_proba([feats])[0][pred]
    label = "⚠️ Phishing" if pred == 1 else "✅ Legitimate"
    messagebox.showinfo("Result", f"{label}\nConfidence: {conf:.2%}")

# Load model once
model = load_model()

# Build GUI
root = tk.Tk()
root.title("Phishing Detector Demo")
tk.Label(root, text="Enter a URL:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)
tk.Button(root, text="Check URL", command=on_check).pack(pady=(0, 10))
root.mainloop()
