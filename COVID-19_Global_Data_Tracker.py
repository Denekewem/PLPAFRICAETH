import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load JHU daily report
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv"
df = pd.read_csv(url)

print("=== Raw Dataset Preview ===")
print(df.head())
print("\nColumns:", df.columns)

# 2️⃣ Keep only relevant columns
df = df[["Country_Region", "Confirmed", "Deaths", "Recovered", "Active"]]

# 3️⃣ Group by country (since some countries have multiple rows by state/province)
df_grouped = df.groupby("Country_Region").sum().reset_index()

print("\n=== Grouped Dataset Preview ===")
print(df_grouped.head())

# 4️⃣ Plot Top 10 countries by confirmed cases
top10_cases = df_grouped.sort_values(by="Confirmed", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top10_cases["Country_Region"], top10_cases["Confirmed"], color="orange")
plt.xticks(rotation=45)
plt.title("Top 10 Countries by Confirmed Cases (01-01-2021)")
plt.ylabel("Confirmed Cases")
plt.show()

# 5️⃣ Calculate fatality rate per country
df_grouped["FatalityRate"] = (df_grouped["Deaths"] / df_grouped["Confirmed"]) * 100

print("\n=== Fatality Rates Sample ===")
print(df_grouped[["Country_Region", "FatalityRate"]].head())
