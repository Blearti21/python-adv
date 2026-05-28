import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# =========================================================
# 1. Average temperature for the entire dataset
# =========================================================
overall_avg_temp = df["Temperature"].mean()

print(f"\n1. Overall Average Temperature: {overall_avg_temp:.2f}°C")


# =========================================================
# 2. Average temperature for each month
# =========================================================
df["Month"] = df["Date"].dt.month_name()

monthly_avg_temp = df.groupby("Month")["Temperature"].mean()

print("\n2. Average Temperature for Each Month:")
print(monthly_avg_temp.round(2))


# =========================================================
# 3. Hottest and Coldest Days
# =========================================================

# Hottest day
hottest_day = df.loc[df["Temperature"].idxmax()]

# Coldest day
coldest_day = df.loc[df["Temperature"].idxmin()]

print("\n3. Hottest Day:")
print(hottest_day)

print("\n3. Coldest Day:")
print(coldest_day)


# =========================================================
# 4. Seasonal Average Temperature
# =========================================================

# Function to assign seasons
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

# Create Season column
df["Season"] = df["Date"].dt.month.apply(get_season)

# Calculate seasonal averages
seasonal_avg_temp = df.groupby("Season")["Temperature"].mean()

print("\n4. Seasonal Average Temperatures:")
print(seasonal_avg_temp.round(2))