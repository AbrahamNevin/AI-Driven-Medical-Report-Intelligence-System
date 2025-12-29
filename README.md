# 🧠 AI-Driven Medical Report Intelligence System

An end-to-end AI system that ingests unstructured medical reports, extracts clinically relevant information using NLP, predicts patient risk using classical machine learning, explains model decisions with SHAP, and generates human-readable summaries using Large Language Models (LLMs).

---

## 🚀 Project Overview

Medical reports are often long, unstructured, and difficult to analyze quickly.  
This project transforms raw medical reports (TXT/PDF) into structured insights through a modular and explainable AI pipeline.

The system is designed with **interpretability, modularity, and production-readiness** in mind — making it suitable for healthcare and fintech-style risk analysis use cases.

---

## 🧩 Key Features

- 📄 **Multi-format ingestion**: TXT and PDF medical reports
- 🧹 **Text preprocessing**: cleaning and normalization
- 🧠 **NLP entity extraction**: conditions, symptoms, risk indicators
- 📊 **Machine Learning**: risk classification using Logistic Regression
- 🔍 **Explainable AI**: SHAP-based feature contribution analysis
- 🗣️ **LLM summaries**: human-readable medical report explanations
- 🌳 **Professional Git workflow**: feature-based branching and clean merges

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AbrahamNevin/AI-Driven-Medical-Report-Intelligence-System.git
cd medical-report-ai
```
2️⃣ Create virtual environment
```bash
Copy code
python -m venv venv
venv\Scripts\activate
```
3️⃣ Install dependencies
```bash
Copy code
pip install -r requirements.txt
```
▶️ Running the Pipeline
Run each stage independently:

Preprocessing
```bash
Copy code
python src/preprocess.py
```
Entity Extraction
```bash
Copy code
python src/entity_extraction.py
```
Train ML Model
```bash
Copy code
python -m src.train_model
```
Explainability
```bash
Copy code
python -m src.explainability
```
LLM Summary (fallback works without API key)
```bash
Copy code
python -m src.llm_summary
```
🔍 Explainability with SHAP
The system uses SHAP (SHapley Additive Explanations) to explain model predictions by quantifying how each feature contributes to the final risk score.



Fully optional

Safe fallback if no API key is provided

Secrets handled via .env

Example summary:

“The patient shows elevated risk due to the presence of cardiovascular risk indicators and reported symptoms.”

🧠 Design Principles
Explainability-first

No black-box decisions

Modular & extensible

Ethically aligned AI usage

Production-style code structure

📌 Future Enhancements
Use real labeled datasets

Add severity-weighted features

Introduce time-series analysis

Deploy via FastAPI

Extend entity extraction with domain-specific models.

👤 Author
Nevin Abraham
Computer Science & Engineering
AI | Machine Learning | Data Analytics

yaml
Copy code

---

# 🧠 Why this README is strong

This README shows:
- **problem understanding**
- **engineering discipline**
- **AI ethics awareness**
- **production mindset**
- **excellent communication**

This alone can **carry interviews**.

---

# ✅ Final steps (2 minutes)

1️⃣ Paste this into `README.md`  
2️⃣ Commit:
```bash
git add README.md
git commit -m "Add comprehensive project README"
git push