import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load data
data = pd.read_csv("Superstore.csv", encoding="latin1")
data = data[['Sales', 'Quantity', 'Discount', 'Profit']]
data.dropna(inplace=True)

# Features & target
X = data[['Sales', 'Quantity', 'Discount']]
y = data['Profit']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2 Score:", r2)

# Save everything
joblib.dump({
    "model": model,
    "rmse": rmse,
    "r2": r2,
    "X_test": X_test,
    "y_test": y_test,
    "y_pred": y_pred
}, "superstore_model.pkl")

print("✅ Model saved as superstore_model.pkl")
