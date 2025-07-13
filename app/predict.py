import joblib
import pandas as pd
from app.schemas import LeadData

model = joblib.load("model/lead_scoring_model.joblib")

def predict_lead_score(data: LeadData):
    df = pd.DataFrame([data.dict()])
    df["email_domain"] = df["email"].apply(lambda x: x.split("@")[1])
    df.drop(columns=["email"], inplace=True)
    score = model.predict_proba(df)[0][1]
    prediction = score > 0.5
    return {"lead_score": round(score, 3), "converted_prediction": prediction}