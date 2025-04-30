import sys #For getting command-line arguments (the URL).
import joblib #For loading the model (which was probably saved using joblib.dump()).
from features import extract_features #converts a URL into a list of features.




MODEL_PATH = "models/phishing_detector_model.pkl"

def load_model(path=MODEL_PATH):
    """Load the phishing detector model with joblib."""
    return joblib.load(path)

"""This function does the actual prediction using the model.

It returns both the label and the model’s confidence (as a probability between 0 and 1)."""

def predict(model, url: str):
    """Extract features, run model, return label+confidence."""
    feats = extract_features(url)
    X = [feats]
    pred = model.predict(X)[0]
    conf = model.predict_proba(X)[0][pred]
    label = "⚠️ Phishing" if pred == 1 else "✅ Legitimate"
    return label, conf




# Makes sure a URL is passed as a command-line argument.

def main():
    if len(sys.argv) != 2:
        print("Usage: python demo_phish_cli.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    model = load_model() #Loads the model and makes a prediction on the URL.
    label, conf = predict(model, url)
    print(f"URL:        {url}")
    print(f"Prediction: {label}")
    print(f"Confidence: {conf:.2%}")

if __name__ == "__main__":
    main()
