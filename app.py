import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.set_page_config(page_title="Water Potability Predictor", page_icon="💧")
st.title("💧 Water Potability Predictor")
st.write("Enter water quality values to check if water is drinkable.")

ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=200.0)
solids = st.number_input("Solids (TDS)", min_value=0.0, value=20000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=330.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=65.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

if st.button("Predict"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ Water is POTABLE - Safe to drink")
    else:
        st.error("❌ Water is NOT POTABLE - Not safe to drink")