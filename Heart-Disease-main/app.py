import streamlit as st
import pandas as pd
import joblib

model = joblib.load("heart_model.pkl")

st.title("Heart Disease Prediction")

st.write("Enter patient details:")

# Example inputs (adjust according to your dataset columns)
age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
cp = st.number_input("Chest Pain Type")
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.number_input("Resting ECG")
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope")
ca = st.number_input("CA")
thal = st.number_input("Thal")

if st.button("Predict"):
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs,
                                restecg, thalach, exang, oldpeak,
                                slope, ca, thal]],
                              columns=model.feature_names_in_)
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease")