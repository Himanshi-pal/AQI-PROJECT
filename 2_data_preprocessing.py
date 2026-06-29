import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("city_day.csv")

# Check missing values
print(df.isnull().sum())

# Convert ALL important columns to numeric
cols = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','AQI']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove rows where AQI is missing (IMPORTANT)
df = df.dropna(subset=['AQI'])

# Fill missing values ONLY for pollutants
df[cols] = df[cols].fillna(df[cols].mean())

# Remove duplicates
df = df.drop_duplicates()

# Remove outliers (simple condition)
df = df[df['PM2.5'] < 500]

# Date processing
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Boxplot AFTER cleaning
pollutants = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','AQI']
plt.figure(figsize=(12,6))
df[pollutants].boxplot()
plt.title("Cleaned Data Boxplot (Pollutants & AQI)")
plt.show()

# Save cleaned data
df.to_csv("cleaned_aqi_data.csv", index=False)

print(df.isnull().sum())