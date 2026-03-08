import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------
# Load Model and Columns
# -----------------------------
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("model_columns.pkl", "rb") as file:
    model_columns = pickle.load(file)

st.set_page_config(page_title="Loan Default Predictor", layout="centered")

st.title("💰 Loan Default Prediction App")
st.write("Predict whether a loan will not be fully paid.")

# -----------------------------
# User Inputs
# -----------------------------
credit_policy = st.selectbox("Credit Policy (1 = Yes, 0 = No)", [1, 0])
int_rate = st.number_input("Interest Rate", min_value=0.0)
installment = st.number_input("Installment")
log_annual_inc = st.number_input("Log Annual Income")
dti = st.number_input("Debt to Income Ratio")
fico = st.number_input("FICO Score")
days_with_cr_line = st.number_input("Days with Credit Line")
revol_bal = st.number_input("Revolving Balance")
revol_util = st.number_input("Revolving Utilization (%)")
inq_last_6mths = st.number_input("Inquiries Last 6 Months")
delinq_2yrs = st.number_input("Delinquencies in 2 Years")
pub_rec = st.number_input("Public Records")

purpose = st.selectbox("Loan Purpose", [
    "credit_card",
    "debt_consolidation",
    "educational",
    "major_purchase",
    "small_business",
    "all_other",
    "home_improvement"
])

# -----------------------------
# Prepare Input Data
# -----------------------------
if st.button("Predict"):

    input_dict = {
        "credit.policy": credit_policy,
        "int.rate": int_rate,
        "installment": installment,
        "log.annual.inc": log_annual_inc,
        "dti": dti,
        "fico": fico,
        "days.with.cr.line": days_with_cr_line,
        "revol.bal": revol_bal,
        "revol.util": revol_util,
        "inq.last.6mths": inq_last_6mths,
        "delinq.2yrs": delinq_2yrs,
        "pub.rec": pub_rec,
    }

    input_df = pd.DataFrame([input_dict])

    # One-hot encode purpose
    for col in model_columns:
        if "purpose_" in col:
            input_df[col] = 0

    purpose_column = "purpose_" + purpose
    if purpose_column in model_columns:
        input_df[purpose_column] = 1

    # Add missing columns
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_columns]

    prediction = model.predict(input_df)[0]

    # Threshold classification
    prediction_class = 1 if prediction >= 0.5 else 0

    st.subheader("Prediction Result")

    st.write(f"Predicted Default Probability: {round(prediction, 3)}")

    if prediction_class == 1:
        st.error("⚠ High Risk: Loan may NOT be fully paid.")
    else:
        st.success("✅ Low Risk: Loan likely to be fully paid.")
