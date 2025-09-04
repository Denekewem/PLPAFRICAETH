import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data from CSV
# -----------------------------
#df = pd.read_csv("sales_data.csv")
url = "https://raw.githubusercontent.com/Denekewem/PLPAFRICAETH/main/sales_data.csv"

df = pd.read_csv(url, header=None)

# First row is actually the header -> split it
df = df[0].str.split(",", expand=True)

# Assign proper column names
df.columns = ["Month", "Sales", "Expenses"]

# Drop the first row if it's the header row
if df.loc[0, "Month"].strip() == "Month":
    df = df.drop(0).reset_index(drop=True)

# Convert numeric columns
df["Sales"] = pd.to_numeric(df["Sales"])
df["Expenses"] = pd.to_numeric(df["Expenses"])

print("=== Fixed Dataset Preview ===")
print(df.head())
print("\nColumns:", df.columns)

# -----------------------------
# 2. Basic Analysis
# -----------------------------
print("\n=== Summary Statistics ===")
print(df.describe())

# Total sales & expenses
total_sales = df["Sales"].sum()
total_expenses = df["Expenses"].sum()
profit = total_sales - total_expenses

print(f"\n💰 Total Sales: {total_sales}")
print(f"💸 Total Expenses: {total_expenses}")
print(f"📊 Profit: {profit}")

# -----------------------------
# 3. Visualization
# -----------------------------

# Add Profit column to DataFrame
df["Profit"] = df["Sales"] - df["Expenses"]

# Line chart for Sales & Expenses
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o", label="Sales")
plt.plot(df["Month"], df["Expenses"], marker="s", label="Expenses")
plt.title("Monthly Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)
plt.show()

# Bar chart for Profit by Month
df["Profit"] = df["Sales"] - df["Expenses"]

plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Profit"], color="green")
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit ($)")
plt.show()

# Pie chart for Sales Contribution
plt.figure(figsize=(6,6))
plt.pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%", startangle=90)
plt.title("Sales Contribution by Month")
plt.show()
