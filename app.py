from fastapi import FastAPI
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/financial_risk_model.pkl")

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the ERIS Risk Intelligence API"}

@app.post("/predict/")
def predict_risk(open_price: float, high_price: float, low_price: float, close_price: float):
    input_data = [[open_price, high_price, low_price, close_price]]
    prediction = model.predict(input_data)[0]
    return {"risk_prediction": prediction}

# Run API using: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
