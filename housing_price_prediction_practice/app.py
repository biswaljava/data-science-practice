import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, mean_squared_error

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Sales Prediction App",
    page_icon="📊",
    layout="centered"
)

st.title("📈 Sales Prediction using Linear Regression")
st.write("Enter feature values to predict sales")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("linear_model.pkl")

model = load_model()

# -----------------------------
# Load Dataset (for reference)
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Housing.csv")

df = load_data()

# -----------------------------
# Feature Selection
# -----------------------------
target = "Sales"
X = df.drop(columns=[target])
y = df[target]

# Keep only numeric columns
X = X.select_dtypes(include=[np.number])

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("🧾 Input Features")

input_data = {}

for col in X.columns:
    min_val = float(X[col].min())
    max_val = float(X[col].max())
    mean_val = float(X[col].mean())

    input_data[col] = st.sidebar.slider(
        label=col,
        min_value=min_val,
        max_value=max_val,
        value=mean_val
    )

input_df = pd.DataFrame([input_data])

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Sales"):
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Predicted Sales: **{prediction:.2f}**")

# -----------------------------
# Model Evaluation (Optional)
# -----------------------------
st.divider()
st.subheader("📊 Model Performance")

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", round(r2, 4))

with col2:
    st.metric("RMSE", round(rmse, 2))

# -----------------------------
# Data Preview
# -----------------------------
with st.expander("📂 View Dataset"):
    st.dataframe(df.head())
