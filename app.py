import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


# Load the trained model
model = joblib.load('water_potability_model.pkl')
scaler = StandardScaler()  # Make sure to use the same scaler you used during training

# Streamlit UI for input
st.title("Water Potability Prediction")

st.write("Please enter the water quality parameters:")

ph = st.slider("pH", 0.0, 14.0, 7.0)  # Default is 7.0
hardness = st.slider("Hardness", 50, 500, 150)
solids = st.slider("Solids", 1000, 50000, 10000)
chloramines = st.slider("Chloramines", 0.0, 5.0, 2.0)
sulfate = st.slider("Sulfate", 50, 500, 250)
conductivity = st.slider("Conductivity", 100, 10000, 3000)
organic_carbon = st.slider("Organic Carbon", 0.0, 20.0, 5.0)
trihalomethanes = st.slider("Trihalomethanes", 0.0, 0.2, 0.05)
turbidity = st.slider("Turbidity", 1.0, 10.0, 2.0)

# Combine inputs into a DataFrame
input_data = pd.DataFrame({
    'ph': [ph],
    'Hardness': [hardness],
    'Solids': [solids],
    'Chloramines': [chloramines],
    'Sulfate': [sulfate],
    'Conductivity': [conductivity],
    'Organic_carbon': [organic_carbon],
    'Trihalomethanes': [trihalomethanes],
    'Turbidity': [turbidity]
})

# Scale the input data (use the same scaler you applied during training)
input_data_scaled = scaler.transform(input_data)

# Make predictions
prediction = model.predict(input_data_scaled)
probability = model.predict_proba(input_data_scaled)[:, 1]  # Probability of class 1 (Potable)

# Display the result
if prediction == 1:
    st.write(f"**Prediction**: The water is **Potable**")
else:
    st.write(f"**Prediction**: The water is **Not Potable**")

st.write(f"**Probability of Potability**: {probability[0]:.2f}")
