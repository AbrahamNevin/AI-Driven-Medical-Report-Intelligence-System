import json
import re
from pathlib import Path
import nltk
from nltk.tokenize import sent_tokenize


PROCESSED_DIR = Path("data/processed")

MEDICAL_CONDITIONS = [
    "diabetes",
    "hypertension",
    "asthma",
    "heart disease",
    "cardiovascular disease"
]

SYMPTOMS = [
    "chest pain",
    "chest discomfort",
    "fatigue",
    "shortness of breath",
    "dizziness"
]

RISK_INDICATORS = [
    "high blood glucose",
    "elevated blood glucose",
    "high bp",
    "elevated bp",
    "smoking history"
]


def extract_entities(text: str) -> dict:
    sentences = sent_tokenize(text)

    found_conditions = set()
    found_symptoms = set()
    found_risks = set()

    for sentence in sentences:
        s = sentence.lower()

        for cond in MEDICAL_CONDITIONS:
            if re.search(rf"\b{re.escape(cond)}\b", s):
                found_conditions.add(cond)

        for sym in SYMPTOMS:
            if re.search(rf"\b{re.escape(sym)}\b", s):
                found_symptoms.add(sym)

        for risk in RISK_INDICATORS:
            if re.search(rf"\b{re.escape(risk)}\b", s):
                found_risks.add(risk)

    return {
        "conditions": sorted(found_conditions),
        "symptoms": sorted(found_symptoms),
        "risk_indicators": sorted(found_risks)
    }


def process_extracted_entities():
    files = list(PROCESSED_DIR.glob("*.txt"))

    if not files:
        print("No processed reports found.")
        return

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        entities = extract_entities(text)

        output_path = PROCESSED_DIR / f"{file_path.stem}_entities.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(entities, f, indent=2)

        print(f"Extracted entities from: {file_path.name}")


if __name__ == "__main__":
    process_extracted_entities()
