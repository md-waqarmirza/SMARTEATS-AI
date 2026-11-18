import streamlit as st
import joblib
import pandas as pd
import os

# Load model
folder = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(folder, "smarteats_model_compressed.pkl")
model = joblib.load(model_path)

# Page settings
st.set_page_config(
    page_title="SMARTEATS-AI",
    page_icon="🍔",
    layout="centered"
)

# Title
st.title("🍔 SMARTEATS-AI")
st.subheader("Food Delivery Time Prediction")

st.write(
    "Enter the delivery details below to estimate the food delivery time."
)

# Input fields
age = st.number_input(
    "Delivery Person Age",
    min_value=18,
    max_value=60,
    value=25
)

rating = st.number_input(
    "Delivery Person Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.5,
    step=0.1
)

distance = st.number_input(
    "Distance (km)",
    min_value=0.1,
    max_value=50.0,
    value=5.0,
    step=0.1
)

vehicle_condition = st.number_input(
    "Vehicle Condition",
    min_value=0,
    max_value=3,
    value=2
)

multiple_deliveries = st.number_input(
    "Multiple Deliveries",
    min_value=0,
    max_value=3,
    value=1
)

# Prediction button
if st.button("🚴 Predict Delivery Time"):

    sample = {
        "Delivery_person_ID": 0,
        "Delivery_person_Age": age,
        "Delivery_person_Ratings": rating,
        "Restaurant_latitude": 0,
        "Restaurant_longitude": 0,
        "Delivery_location_latitude": 0,
        "Delivery_location_longitude": 0,
        "Time_Orderd": 720,
        "Time_Order_picked": 730,
        "Weather_conditions": 0,
        "Road_traffic_density": 1,
        "Vehicle_condition": vehicle_condition,
        "Type_of_order": 0,
        "Type_of_vehicle": 0,
        "multiple_deliveries": multiple_deliveries,
        "Festival": 0,
        "City": 0,
        "distance_km": distance,
        "delivery_speed": 1,
        "Order_Day": 15,
        "Order_Month": 9,
        "Order_Weekday": 1
    }

    input_data = pd.DataFrame([sample])

    prediction = model.predict(input_data)[0]

    estimated_time = round(prediction, 2)
    lower_time = max(1, round(estimated_time - 3, 2))
    upper_time = round(estimated_time + 3, 2)

    st.success(
        f"🚴 Estimated Delivery Time: {estimated_time} minutes"
    )

    st.info(
        f"⏱️ Estimated Range: {lower_time} - {upper_time} minutes"
    )

    st.write("Thank you for using **SMARTEATS-AI!** 🍔")
