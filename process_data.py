import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSV files
csv_files = list(data_path.glob("*.csv"))

dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Combine into one DataFrame
data = pd.concat(dfs, ignore_index=True)

# Normalise product names
data["product"] = data["product"].str.strip().str.lower()

# Keep only Pink Morsels
data = data[data["product"] == "pink morsel"]

# Clean price column: remove $ and convert to float
data["price"] = (
    data["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

# Ensure quantity is numeric
data["quantity"] = data["quantity"].astype(int)

# Create sales column correctly
data["sales"] = data["quantity"] * data["price"]

# Keep only required columns
final_data = data[["sales", "date", "region"]]

# Save output
final_data.to_csv("output.csv", index=False)

print("✅ Data processing complete. output.csv created.")
