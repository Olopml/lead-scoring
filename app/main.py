from fastapi import FastAPI
from app.predict import predict_lead_score
from app.schemas import LeadData

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running"}

@app.post("/predict")
def predict(data: LeadData):
    return predict_lead_score(data)