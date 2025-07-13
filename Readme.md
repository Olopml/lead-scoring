# 🧠 Lead Scoring API

This project provides an API to score and predict B2B lead conversion based on company data. Ideal for CRMs, web forms, and sales pipelines.

## 🔍 What it does
- Predicts the probability that a lead will convert
- Returns a probability score and boolean prediction

## 🚀 Stack
- **FastAPI** – For the REST API
- **scikit-learn** – For training the machine learning pipeline
- **Joblib** – For model serialization

## 🛠️ Example Input
```json
{
  "email": "john@startup.io",
  "sector": "Tech",
  "country": "USA",
  "company_size": 35,
  "website_visits": 14
}
```

## 📤 Example Output
```json
{
  "lead_score": 0.742,
  "converted_prediction": true
}
```

## 🧪 Run Locally
```bash
# Train the model
notebooks/training.ipynb

# Start the API
uvicorn app.main:app --reload
```

## 🐳 Run with Docker
```bash
docker build -t lead-scoring-api .
docker run -p 8000:8000 lead-scoring-api
```

## 📁 Project Structure
```
.
├── app/                # FastAPI app
├── training/           # Model training script
├── model/              # Serialized model
├── data/               # Input CSV
├── requirements.txt
├── Dockerfile
└── README.md
```

## 📬 Endpoint
`POST /predict` – Returns the lead score and conversion prediction.

---
© 2025 · Made by [Olopml](https://github.com/Olopml)