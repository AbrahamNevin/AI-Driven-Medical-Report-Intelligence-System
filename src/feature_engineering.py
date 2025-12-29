import json
from pathlib import Path
import pandas as pd

PROCESSED_DIR = Path("data/processed")


def load_feature_dataframe():
    entity_files = list(PROCESSED_DIR.glob("*_entities.json"))

    records = []

    for file_path in entity_files:
        with open(file_path, "r", encoding="utf-8") as f:
            entities = json.load(f)

        record = {
            "num_conditions": len(entities.get("conditions", [])),
            "num_symptoms": len(entities.get("symptoms", [])),
            "num_risk_indicators": len(entities.get("risk_indicators", [])),
            "high_risk": 1 if len(entities.get("risk_indicators", [])) > 0 else 0
        }

        records.append(record)

    return pd.DataFrame(records)


if __name__ == "__main__":
    df = load_feature_dataframe()
    print(df)
