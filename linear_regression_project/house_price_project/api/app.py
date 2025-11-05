# api/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd


app = FastAPI(
    title="House Price Prediction API",
    description="A FastAPI-based ML model for predicting house prices using Linear Regression",
    version="1.0"
)

# Load training model
model = joblib.load("D:\\PythonProjects\\Dataframe\\linear_regression_project\\house_price_project\\house_price_model.pkl")

# Dummy feature scaler setup (must match training features)
scaler = StandardScaler()

# We'll fit it using same structure (values don't matter, just shape)
dummy_data = pd.DataFrame( {
    'Area (sqrt)': [2, 3, 3, 4],
    'Bedrooms': [2, 3, 3, 4],
    'Age (years)': [5, 8, 10, 12],
    'Distance (km)': [5, 8, 10, 12]
})

scaler.fit(dummy_data)

# Define request schema
class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    age: int
    distance: float

@app.get("/")
def root():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    data = np.array([[features.area, features.bedrooms, features.age, features.distance]])
    data_scaled = scaler.transform(pd.DataFrame(data, columns=dummy_data.columns))
    prediction = model.predict(data_scaled)
    return {"predicted_price (rs in lakhs)": round(float(prediction[0]), 2)}