import os
import re
from pathlib import Path


RAW_DIR = Path("data/raw_reports")
PROCESSED_DIR = Path("data/processed")


def clean_text(text: str) -> str:
    """
    Cleans raw medical report text.
    - Lowercases text
    - Removes special characters
    - Normalizes whitespace
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def process_reports():
    """
    Reads all .txt files from raw_reports,
    cleans them, and saves cleaned versions.
    """
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    report_files = list(RAW_DIR.glob("*.txt"))

    if not report_files:
        print("No reports found in data/raw_reports/")
        return

    for report_path in report_files:
        with open(report_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        output_path = PROCESSED_DIR / report_path.name
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(f"Processed: {report_path.name}")


if __name__ == "__main__":
    process_reports()
