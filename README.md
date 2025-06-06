# **Phishing URL Detector 🚨🔍**

*A simple, yet effective command-line project that identifies phishing URLs using a machine learning model trained on custom URL-based features. It leverages a Random Forest Classifier to distinguish between malicious (phishing) and benign URLs based on 30 handcrafted characteristics of each URL.*

---

## 📂 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Model Details](#model-details)
5. [Potential Enhancements](#potential-enhancements)

---

## Project Overview

This repository implements a phishing URL detection system. Each URL is parsed to extract a set of 30 numeric and boolean features (e.g., length of URL, count of special characters, presence of IP addresses, suspicious tokens such as **"login"** or **"verify"**). A Random Forest Classifier is trained on labeled examples to predict whether a given URL is phishing or safe.

---

## Features

1. **URL Length**: Total number of characters.
2. **Hostname Length**: Characters in the domain portion.
3. **Count of Dots**: Number of `.` in the URL.
4. **Count of Hyphens**: Number of `-` characters.
5. **Count of `@` Symbols**
6. **Count of Query Parameters**: Number of `?` occurrences.
7. **Presence of IP Address**: Boolean flag if URL uses an IPv4/IPv6 literal.
8. **Count of Suspicious Substrings**: Keywords like *login*, *secure*, *update*, *verify*, etc.
9. **Count of Digits**: Total numeric characters.
10. **Count of Special Characters**: Non‑alphanumeric symbols.
11–30. **Additional Heuristics**: Ratios (digits/length), presence of multiple subdomains, TLD length, use of HTTP vs HTTPS, and more.

---

## Requirements

- **Python** 3.8+
- **pandas**
- **scikit-learn**
- **joblib**

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Model Details

- **Algorithm**: Random Forest Classifier (`n_estimators=100`, `random_state=42`)
- **Input Features**: 30 handcrafted numeric/boolean URL attributes
- **Training Split**: 80% train, 20% test by default
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score (see `train_detector.py` for details)

---

## Potential Enhancements

- **Ensemble Methods**: Combine with Gradient Boosting or Neural Networks.
- **Deep Learning**: Character-level CNNs or LSTM on raw URL strings.
- **Real-Time Fetching**: Integrate WHOIS or SSL certificate checks.
- **Dashboard**: Build a web UI to batch test URLs and visualize alerts.
- **Additional Features**: Domain age, WHOIS registration details, Alexa rank.

---

**Happy phishing detection! 🕵️‍♂️🔒**

