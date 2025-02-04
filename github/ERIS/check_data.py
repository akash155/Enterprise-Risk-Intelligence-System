import pandas as pd

# Define dataset path
dataset_path = "data/processed/financial_risk_normalized.csv"

# Check if dataset exists
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"❌ Dataset not found: {dataset_path}")

# Load dataset
df = pd.read_csv(dataset_path)

# Print actual column names
print("✅ Column names in dataset:", df.columns.tolist())

# Display first few rows
print(df.head())
