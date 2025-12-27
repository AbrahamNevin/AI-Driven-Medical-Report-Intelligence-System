import re
from pathlib import Path
from pypdf import PdfReader


RAW_DIR = Path("data/raw_reports")
PROCESSED_DIR = Path("data/processed")


def clean_text(text: str) -> str:
    """
    Cleans raw medical report text.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def read_txt(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def read_pdf(file_path: Path) -> str:
    reader = PdfReader(file_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def process_reports():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    files = list(RAW_DIR.glob("*"))

    if not files:
        print("No reports found in data/raw_reports/")
        return

    for file_path in files:
        if file_path.suffix == ".txt":
            raw_text = read_txt(file_path)
        elif file_path.suffix == ".pdf":
            raw_text = read_pdf(file_path)
        else:
            print(f"Skipping unsupported file: {file_path.name}")
            continue

        cleaned_text = clean_text(raw_text)

        output_path = PROCESSED_DIR / f"{file_path.stem}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(f"Processed: {file_path.name}")


if __name__ == "__main__":
    process_reports()
