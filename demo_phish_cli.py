import sys
import joblib
from features import extract_features


MODEL_PATH = "models/phishing_detector_model.pkl"

def load_model(path=MODEL_PATH):
    """Load the phishing detector model with joblib."""
    return joblib.load(path)

def predict(model, url: str):
    """Extract features, run model, return label+confidence."""
    feats = extract_features(url)
    X = [feats]
    pred = model.predict(X)[0]
    conf = model.predict_proba(X)[0][pred]
    label = "⚠️ Phishing" if pred == 1 else "✅ Legitimate"
    return label, conf

def main():
    if len(sys.argv) != 2:
        print("Usage: python demo_phish_cli.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    model = load_model()
    label, conf = predict(model, url)
    print(f"URL:        {url}")
    print(f"Prediction: {label}")
    print(f"Confidence: {conf:.2%}")

if __name__ == "__main__":
    main()
