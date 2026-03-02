import pandas as pd
import numpy as np

# Create 2 years of weekly data
dates = pd.date_range(start="2024-01-01", periods=104, freq="W")

# Generate random spend
np.random.seed(42)
google_spend = np.random.normal(5000, 1000, 104).clip(0)
facebook_spend = np.random.normal(4000, 800, 104).clip(0)
tv_spend = np.random.normal(10000, 2000, 104).clip(0)

# Create Sales with math: Revenue = Base + (Spend * ROI) + Noise
# We simulate TV having a delayed effect
revenue = 15000 + (google_spend * 1.2) + (facebook_spend * 0.8) + (tv_spend * 0.5) + np.random.normal(0, 2000, 104)

df = pd.DataFrame({
    "date": dates,
    "google_spend": google_spend,
    "facebook_spend": facebook_spend,
    "tv_spend": tv_spend,
    "revenue": revenue
})

df.to_csv("data/raw_marketing_data.csv", index=False)
print(" Data generated and saved to 'data/raw_marketing_data.csv'")
