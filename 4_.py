import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_aqi_data.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

pollutants = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3']

# -------------------------------
# 1. Correlation with AQI
# -------------------------------
corr = df[pollutants + ['AQI']].corr()
aqi_corr = corr['AQI'].sort_values(ascending=False)

print("\nCorrelation with AQI:\n")
print(aqi_corr)

# -------------------------------
# 2. Seasonal Analysis
# -------------------------------
def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Summer"
    elif month in [6,7,8,9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

df['Season'] = df['Month'].apply(get_season)

seasonal_avg = df.groupby('Season')['AQI'].mean()

print("\nSeasonal AQI:\n")
print(seasonal_avg)

# -------------------------------
# 3. Monthly Trend (values only)
# -------------------------------
monthly_avg = df.groupby('Month')['AQI'].mean()

print("\nMonthly AQI:\n")
print(monthly_avg)

# -------------------------------
# 4. Extreme Pollution Events
# -------------------------------
high_aqi = df[df['AQI'] > df['AQI'].quantile(0.95)]

print("\nExtreme AQI Events:\n")
print(high_aqi[['Date','City','AQI']].head())

# -------------------------------
# 5. Top Polluted Cities
# -------------------------------
top_cities = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(10)

print("\nTop Polluted Cities:\n")
print(top_cities)

# -------------------------------
# 6. AQI Summary Stats
# -------------------------------
print("\nAQI Summary:\n")
print(df['AQI'].describe())