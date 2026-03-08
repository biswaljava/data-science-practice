import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# -----------------------------
# Load trained model
# -----------------------------
bundle = joblib.load("superstore_model.pkl")
model = bundle["model"]
rmse = bundle["rmse"]
r2 = bundle["r2"]
X_test = bundle["X_test"]
y_test = bundle["y_test"]
y_pred = bundle["y_pred"]

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Superstore Profit Predictor",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# Custom Styling (Tailwind-ish)
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: #e5e7eb;
    }
    .stButton button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: bold;
    }
    .metric-box {
        background: #020617;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# UI Header
# -----------------------------
st.title("📈 Superstore Profit Prediction")
st.write("Predict **Profit** using Sales, Quantity & Discount")

st.divider()

# -----------------------------
# Model Accuracy
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("📉 RMSE", f"{rmse:.2f}")

with col2:
    st.metric("📊 R² Score", f"{r2:.3f}")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------
sales = st.number_input("💰 Sales", min_value=0.0, value=500.0)
quantity = st.number_input("📦 Quantity", min_value=1, value=2)
discount = st.slider("🏷️ Discount", 0.0, 1.0, 0.1)

if st.button("Predict Profit"):
    input_data = np.array([[sales, quantity, discount]])
    prediction = model.predict(input_data)[0]

    st.success(f"💵 Predicted Profit: ₹ {prediction:.2f}")

# -----------------------------
# Charts
# -----------------------------
st.divider()
st.subheader("📊 Model Performance")

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.set_xlabel("Actual Profit")
ax.set_ylabel("Predicted Profit")
ax.set_title("Actual vs Predicted Profit")

st.pyplot(fig)
