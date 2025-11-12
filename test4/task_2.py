import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# -----------------------------
# Step 1: Generate Random Healthcare Dataset
# -----------------------------
np.random.seed(42)

data = {
    'Patient_ID': range(1, 11),
    'Age': np.random.randint(20, 80, size=10),
    'Blood_Pressure': [120, 140, np.nan, 130, 125, np.nan, 135, 150, 145, np.nan],
    'Cholesterol': [200, 220, 180, np.nan, 195, 210, np.nan, 205, 190, 200],
    'Heart_Rate': [72, np.nan, 80, 77, 75, 70, np.nan, 85, 78, 73]
}

df = pd.DataFrame(data)
print("🏥 Original Healthcare Dataset:\n")
print(df)

# -----------------------------
# Step 2: Handle Missing Data (Median Imputation)
# -----------------------------
df_filled = df.copy()
for col in ['Blood_Pressure', 'Cholesterol', 'Heart_Rate']:
    median_value = df_filled[col].median()
    df_filled[col].fillna(median_value, inplace=True)

print("\n✅ Dataset after Filling Missing Values with Column Medians:\n")
print(df_filled)

# -----------------------------
# Step 3: Apply Min–Max Normalization
# -----------------------------
scaler = MinMaxScaler()
numeric_cols = ['Age', 'Blood_Pressure', 'Cholesterol', 'Heart_Rate']

df_scaled = df_filled.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df_scaled[numeric_cols])

print("\n📊 Dataset after Min–Max Normalization:\n")
print(df_scaled)

# -----------------------------
# Step 4: Save Datasets as CSV (optional)
# -----------------------------
df.to_csv("original_healthcare_data.csv", index=False)
df_filled.to_csv("cleaned_healthcare_data.csv", index=False)
df_scaled.to_csv("normalized_healthcare_data.csv", index=False)

print("\n💾 Files saved:")
print(" - original_healthcare_data.csv")
print(" - cleaned_healthcare_data.csv")
print(" - normalized_healthcare_data.csv")

# -----------------------------
# Step 5: Display Comparison Summary
# -----------------------------
comparison = pd.concat(
    [df_filled[numeric_cols].head(), df_scaled[numeric_cols].head()],
    axis=1,
    keys=['Original', 'Normalized']
)

print("\n🔍 Comparison of Original vs Normalized Data (first 5 rows):\n")
print(comparison)
