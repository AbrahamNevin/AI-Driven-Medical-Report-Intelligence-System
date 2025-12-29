import os
import json
from pathlib import Path
from dotenv import load_dotenv
import requests


load_dotenv()

PROCESSED_DIR = Path("data/processed")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"


def generate_summary(entities: dict, risk_score: float) -> str:
    """
    Generates a human-readable medical summary using an LLM.
    If no API key is present, returns a fallback summary.
    """

    if not OPENAI_API_KEY:
        return (
            "Summary unavailable (no LLM key). "
            f"Detected conditions: {', '.join(entities['conditions']) or 'None'}. "
            f"Symptoms: {', '.join(entities['symptoms']) or 'None'}. "
            f"Risk indicators: {', '.join(entities['risk_indicators']) or 'None'}. "
            f"Predicted risk score: {risk_score:.2f}."
        )

    prompt = f"""
You are a clinical decision support assistant.
Summarize the following patient report in simple, professional language.

Conditions: {entities['conditions']}
Symptoms: {entities['symptoms']}
Risk Indicators: {entities['risk_indicators']}
Predicted Risk Score: {risk_score:.2f}

Do NOT give medical advice.
Just summarize clearly.
"""

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }

    response = requests.post(
        OPENAI_API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"].strip()


def generate_summaries_for_reports():
    """
    Generates summaries for all extracted entity files.
    """
    entity_files = list(PROCESSED_DIR.glob("*_entities.json"))

    for file_path in entity_files:
        with open(file_path, "r", encoding="utf-8") as f:
            entities = json.load(f)

        # Simple heuristic risk score (placeholder)
        risk_score = 0.8 if entities["risk_indicators"] else 0.2

        summary = generate_summary(entities, risk_score)

        output_path = PROCESSED_DIR / f"{file_path.stem}_summary.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)

        print(f"Generated summary for: {file_path.name}")


if __name__ == "__main__":
    generate_summaries_for_reports()
