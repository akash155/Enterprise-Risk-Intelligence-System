import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Ensure the 'models' directory exists
os.makedirs("models", exist_ok=True)

# Load processed dataset
dataset_path = "data/processed/financial_risk_normalized.csv"

# Check if the dataset exists
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"❌ Dataset not found: {dataset_path}. Run preprocess.py first!")

df = pd.read_csv(dataset_path)

# Expected columns
required_cols = ["Open", "High", "Low", "Close"]
if not all(col in df.columns for col in required_cols):
    raise KeyError(f"❌ Dataset missing required columns: {required_cols}. Found columns: {df.columns.tolist()}")

# Features (X) and Target (Y) - Assuming 'Close' is the target variable
X = df[["Open", "High", "Low"]]
Y = df["Close"].apply(lambda x: 1 if x > 0.5 else 0)  # Example: Binary classification (Adjust as needed)

# Split into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# Predict & Evaluate
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"✅ Model Training Complete! Accuracy: {accuracy:.2f}")

# Save the model
model_path = "models/financial_risk_model.pkl"
joblib.dump(model, model_path)
print(f"✅ Model saved at {model_path}")
