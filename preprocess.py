import pandas as pd
import os

# Load raw dataset (Update this path based on where your actual data is)
raw_data_path = "financial_risk_data.csv"
processed_data_path = "data/processed/financial_risk_normalized.csv"

# Ensure 'data/processed' directory exists
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv(raw_data_path)

# Check actual column names
print("✅ Raw dataset columns:", df.columns.tolist())

# Rename columns if necessary
column_mapping = {
    "open_price": "Open",
    "high_price": "High",
    "low_price": "Low",
    "close_price": "Close"
}
df.rename(columns=column_mapping, inplace=True)

# Keep only relevant columns
required_cols = ["Open", "High", "Low", "Close"]
df = df[required_cols]

# Normalize the data (optional)
df = (df - df.min()) / (df.max() - df.min())

# Save processed dataset
df.to_csv(processed_data_path, index=False)

print(f"✅ Processed dataset saved at {processed_data_path}")
