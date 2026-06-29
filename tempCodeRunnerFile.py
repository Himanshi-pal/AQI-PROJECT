import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_aqi_data.csv")

# Style
sns.set(style="whitegrid")

# Pollutant columns
pollutants = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3']

# -------------------------------
# 1. AQI Distribution
# -------------------------------
plt.figure()
sns.histplot(df['AQI'], kde=True)
plt.title("AQI Distribution")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# 2. Pollutant Distributions
# -------------------------------
df[pollutants].hist(figsize=(12,8))
plt.suptitle("Pollutant Distributions")
plt.show()

# -------------------------------
# 3. Correlation Heatmap (IMPORTANT)
# -------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df[pollutants + ['AQI']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# 4. Pollutants vs AQI (Scatter Plots)
# -------------------------------
for col in pollutants:
    temp_df = df[[col, 'AQI']].dropna()
    
    plt.figure()
    sns.scatterplot(x=temp_df[col], y=temp_df['AQI'])
    plt.title(f"{col} vs AQI")
    plt.xlabel(col)
    plt.ylabel("AQI")
    plt.show()

# -------------------------------
# 5. Boxplot (Outliers)
# -------------------------------
plt.figure(figsize=(12,6))
df[pollutants + ['AQI']].boxplot()
plt.yscale('log')  # improves visibility
plt.title("Outliers in Pollutants and AQI")
plt.show()

# -------------------------------
# 6. Monthly AQI Trend
# -------------------------------
monthly_avg = df.groupby('Month')['AQI'].mean()

plt.figure()
monthly_avg.plot(marker='o')
plt.title("Monthly Average AQI")
plt.xlabel("Month")
plt.ylabel("AQI")
plt.show()

# -------------------------------
# 7. City-wise AQI (Top 10)
# -------------------------------
top_cities = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(10)

plt.figure()
top_cities.plot(kind='bar')
plt.title("Top 10 Most Polluted Cities")
plt.xlabel("City")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.show()