import streamlit as st
import pandas as pd
import joblib

# Project Title
st.title("Water Potability Prediction")

# Load the saved model
try:
    model = joblib.load('water_potability_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'water_potability_model.pkl' is in the same directory.")
    st.stop()

# Streamlit user inputs
ph = st.slider("pH", 4.0, 10.0, 7.0)
hardness = st.slider("Hardness", 100.0, 300.0, 150.0)
solids = st.slider("Solids", 300.0, 50000.0, 10000.0)
chloramines = st.slider("Chloramines", 3.0, 10.0, 5.0)
sulfate = st.slider("Sulfate", 200.0, 400.0, 250.0)
conductivity = st.slider("Conductivity", 100.0, 700.0, 300.0)
organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 5.0)
trihalomethanes = st.slider("Trihalomethanes", 20.0, 120.2, 25.05)
turbidity = st.slider("Turbidity", 1.0, 8.0, 2.0)

# Create input dataframe
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

# Display input data
st.write("### Input Data")
st.write(input_data)

# Make predictions
try:
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]
except Exception as e:
    st.error(f"Error making predictions: {e}")
    st.stop()

# Display results
st.write("### Prediction Results")
if prediction[0] == 1:
    st.success(f"**Prediction**: The water is **Potable**")
else:
    st.error(f"**Prediction**: The water is **Not Potable**")

st.write(f"**Probability of Potability**: {probability[0]:.2f}")

# Debugging Output (Optional - for Developers)
if st.checkbox("Show Debugging Information"):
    st.write("### Debugging Information")
    st.write(f"Prediction: {prediction}")
    st.write(f"Probability: {probability}")
