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

## 🏗️ System Architecture

Raw Reports (TXT/PDF)
↓
Preprocessing
↓
Entity Extraction (NLP)
↓
Feature Engineering
↓
Risk Classification (ML)
↓
Explainability (SHAP)
↓
LLM-based Summary


Each stage is isolated, testable, and replaceable.

---


---

## ⚙️ Installation & Setup

### 1️ Clone the repository
```bash
git clone https://github.com/AbrahamNevin/AI-Driven-Medical-Report-Intelligence-System.git
cd medical-report-ai

### Create virtual environment
python -m venv venv
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Running the Pipeline
python src/preprocess.py

###Preprocessing
python src/preprocess.py
###Entity Extraction
python src/entity_extraction.py

###Train ML Model
python -m src.train_model

###Explainability
python -m src.explainability

###LLM Summary (fallback works without API key)
python -m src.llm_summary