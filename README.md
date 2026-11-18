# 🍔 SMARTEATS-AI

## Food Delivery Time Prediction Using Machine Learning

SMARTEATS-AI is a machine learning project that predicts the estimated delivery time of a food order based on different factors such as delivery distance, delivery partner details, traffic conditions, vehicle condition, weather, and order information.

## 🎯 Objective

The main objective of this project is to estimate food delivery time using historical delivery data and a machine learning model.

## 🤖 Machine Learning Model

The project uses:

- Random Forest Regressor
- Train-Test Split
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## 📊 Model Performance

The current model achieved approximately:

- MAE: 2.33 minutes
- RMSE: 2.91 minutes
- R² Score: 0.90

## 🔑 Main Features

The model uses information including:

- Delivery person age
- Delivery person rating
- Restaurant location
- Delivery location
- Order time
- Weather conditions
- Road traffic density
- Vehicle condition
- Type of order
- Type of vehicle
- Multiple deliveries
- Festival
- City
- Distance
- Delivery speed
- Order date information

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- VS Code

## 📁 Project Structure

```text
SMARTEATS-AI/
│
├── data/
├── smarteats_model.pkl
├── predict.py
├── requirements.txt
└── README.md