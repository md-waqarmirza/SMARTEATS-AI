import os
import joblib
import pandas as pd

# Find the model file in the same folder as this program
folder = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(folder, "smarteats_model_compressed.pkl")

# Load the trained model
model = joblib.load(model_path)

print("🍔 SMARTEATS-AI FOOD DELIVERY TIME PREDICTOR")
print("=" * 55)

# User inputs
age = float(input("Delivery Person Age: "))
rating = float(input("Delivery Person Rating (1-5): "))
distance = float(input("Distance (km): "))
vehicle_condition = float(input("Vehicle Condition (0-3): "))
multiple_deliveries = float(input("Multiple Deliveries (0-3): "))

# Create input using the same 22 features used during training
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

# Predict delivery time
prediction = model.predict(input_data)
estimated_time = round(prediction[0], 2)

lower_time = max(1, round(estimated_time - 3, 2))
upper_time = round(estimated_time + 3, 2)
print("\n" + "=" * 55)
print("🚴 Estimated Delivery Time:", estimated_time, "minutes")
print("⏱️ Estimated Range:", lower_time, "-", upper_time, "minutes")
print("=" * 55)
print("Thank you for using SMARTEATS-AI!")