"""
Simple AI-assisted healthcare algorithm demo (educational only)

This script trains a tiny logistic model on synthetic data to estimate
cardiovascular risk from a few inputs. It prompts the user for values,
predicts a probability, returns a risk category, and produces an "AI"
explanation (stub) and a small HTML report the user can screenshot.

DISCLAIMER: For educational/demo purposes only. Not for clinical use.
"""

import os
import json
import math
from typing import Dict, Tuple
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib

MODEL_PATH = "health_model.joblib"
np.random.seed(42)


def generate_synthetic_data(n=2000) -> Tuple[np.ndarray, np.ndarray]:
    """Create synthetic patient dataset and binarized outcome.

    Features: age, bmi, systolic_bp, cholesterol, smoking(0/1), diabetes(0/1)
    Outcome: synthetic CV event probability via logistic function of features
    """
    age = np.random.randint(30, 85, size=n)
    bmi = np.random.normal(27, 5, size=n)
    systolic = np.random.normal(130, 15, size=n)
    chol = np.random.normal(200, 30, size=n)
    smoking = np.random.binomial(1, 0.2, size=n)
    diabetes = np.random.binomial(1, 0.15, size=n)

    X = np.vstack([age, bmi, systolic, chol, smoking, diabetes]).T

    # Create a ground-truth score using chosen weights
    # weights chosen to roughly reflect risk contributions (demo only)
    w = np.array([0.04, 0.06, 0.03, 0.02, 0.8, 0.9])
    intercept = -10.5
    linear = X.dot(w) + intercept
    prob = 1 / (1 + np.exp(-linear))

    y = (prob > 0.2).astype(int)  # threshold to create binary label
    return X, y


def train_or_load_model(force_retrain=False) -> LogisticRegression:
    if os.path.exists(MODEL_PATH) and not force_retrain:
        try:
            model = joblib.load(MODEL_PATH)
            return model
        except Exception:
            pass

    X, y = generate_synthetic_data(n=2500)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(solver="lbfgs", max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict_proba(X_test)[:, 1]
    try:
        auc = roc_auc_score(y_test, preds)
    except Exception:
        auc = float('nan')
    joblib.dump(model, MODEL_PATH)
    print(f"Model trained and saved to {MODEL_PATH} (AUC={auc:.3f})")
    return model


def risk_category(prob: float) -> str:
    if prob < 0.1:
        return "Low"
    elif prob < 0.2:
        return "Moderate"
    elif prob < 0.35:
        return "High"
    else:
        return "Very high"


def ai_explain_stub(features: Dict[str, float], prob: float) -> str:
    """Return a human-friendly explanation and suggestions (mock AI).

    In a real integration this function would call an LLM with a secure prompt
    and return its response.
    """
    lines = []
    lines.append("AI Explanation (simulated):")
    lines.append(f"Estimated cardiovascular risk: {prob*100:.1f}% ({risk_category(prob)})")

    # feature contributions (simple approximation)
    contrib = []
    contrib.append(("Age", (features["age"] - 50) * 0.04))
    contrib.append(("BMI", (features["bmi"] - 25) * 0.06))
    contrib.append(("Systolic BP", (features["systolic_bp"] - 120) * 0.03))
    contrib.append(("Cholesterol", (features["cholesterol"] - 180) * 0.02))
    contrib.append(("Smoking", 0.8 if features.get("smoking", 0) else 0.0))
    contrib.append(("Diabetes", 0.9 if features.get("diabetes", 0) else 0.0))

    contrib_sorted = sorted(contrib, key=lambda x: abs(x[1]), reverse=True)
    lines.append("Top factors contributing to risk:")
    for name, val in contrib_sorted[:3]:
        sign = "increases" if val > 0 else "decreases"
        lines.append(f"- {name}: {sign} risk (approx contribution {val:.2f})")

    # Simple suggestions
    suggestions = []
    if features.get("smoking"):
        suggestions.append("Consider smoking cessation programs.")
    if features.get("diabetes"):
        suggestions.append("Work with a clinician to optimize diabetes control.")
    if features.get("bmi") and features["bmi"] > 27:
        suggestions.append("Lifestyle changes: diet and regular exercise to reduce BMI.")
    if features.get("systolic_bp") and features["systolic_bp"] > 140:
        suggestions.append("Blood pressure management (consult healthcare provider).")

    if suggestions:
        lines.append("Suggested next steps:")
        for s in suggestions:
            lines.append(f"- {s}")
    else:
        lines.append("Suggested next steps: Maintain healthy lifestyle; regular check-ups.")

    lines.append("\nNote: This is a simulated AI explanation. Always consult a clinician for medical advice.")

    return "\n".join(lines)


def prompt_user_inputs() -> Dict[str, float]:
    print("Enter patient information (press Enter to accept suggested defaults in brackets):")
    def ask_float(prompt, default=None, min_v=None, max_v=None):
        while True:
            raw = input(f"{prompt} [{default}]: ").strip()
            if raw == "" and default is not None:
                return default
            try:
                val = float(raw)
                if min_v is not None and val < min_v:
                    print(f"Value must be >= {min_v}")
                    continue
                if max_v is not None and val > max_v:
                    print(f"Value must be <= {max_v}")
                    continue
                return val
            except ValueError:
                print("Please enter a numeric value.")

    age = ask_float("Age (years)", default=55, min_v=18, max_v=120)
    bmi = ask_float("BMI (kg/m^2)", default=28.0, min_v=10, max_v=60)
    systolic = ask_float("Systolic blood pressure (mmHg)", default=135, min_v=80, max_v=250)
    chol = ask_float("Total cholesterol (mg/dL)", default=210, min_v=100, max_v=400)

    # binary inputs
    def ask_yesno(prompt, default=False):
        while True:
            raw = input(f"{prompt} [{'Y' if default else 'N'}]:").strip().lower()
            if raw == "" and default is not None:
                return 1 if default else 0
            if raw in ("y", "yes", "1"):
                return 1
            if raw in ("n", "no", "0"):
                return 0
            print("Enter Y or N.")

    smoking = ask_yesno("Current smoker? (Y/N)", default=False)
    diabetes = ask_yesno("Diabetes diagnosis? (Y/N)", default=False)

    return {
        "age": age,
        "bmi": bmi,
        "systolic_bp": systolic,
        "cholesterol": chol,
        "smoking": smoking,
        "diabetes": diabetes,
    }


def render_html_report(features: Dict[str, float], prob: float, explanation: str, out_path: str = "health_report.html") -> None:
    html = f"""<!doctype html>
<html lang='en'>
<head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Health Risk Report</title>
<style>body{{font-family:Arial,Helvetica,sans-serif;padding:20px;background:#f6f8fb}}.card{{max-width:760px;margin:0 auto;background:#fff;padding:20px;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,0.08)}}h1{{color:#333}}pre{{white-space:pre-wrap;font-family:inherit}}</style>
</head>
<body>
<div class='card'>
<h1>Simulated Health Risk Report</h1>
<p><strong>Estimated risk:</strong> {prob*100:.1f}% ({risk_category(prob)})</p>
<h2>Input values</h2>
<ul>
<li>Age: {features['age']}</li>
<li>BMI: {features['bmi']}</li>
<li>Systolic BP: {features['systolic_bp']}</li>
<li>Cholesterol: {features['cholesterol']}</li>
<li>Smoking: {'Yes' if features.get('smoking') else 'No'}</li>
<li>Diabetes: {'Yes' if features.get('diabetes') else 'No'}</li>
</ul>
<h2>AI Explanation</h2>
<pre>{explanation}</pre>
<p><em>Disclaimer: For educational use only. Not medical advice.</em></p>
</div>
</body>
</html>"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML report saved to {out_path}")


def main():
    print("=== AI-Assisted Health Risk Demo (educational only) ===")
    model = train_or_load_model()

    features = prompt_user_inputs()
    x = np.array([[features['age'], features['bmi'], features['systolic_bp'], features['cholesterol'], features['smoking'], features['diabetes']]])

    prob = float(model.predict_proba(x)[:, 1][0])
    explanation = ai_explain_stub(features, prob)

    print("\n--- Result ---")
    print(f"Estimated risk: {prob*100:.1f}% ({risk_category(prob)})")
    print("\nExplanation:\n")
    print(explanation)

    render_html_report(features, prob, explanation)


if __name__ == '__main__':
    main()
