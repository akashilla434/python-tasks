# ============================================================
# 📊 Railway Gauge Data Analysis Project (FINAL FIXED)
# ============================================================

# ============================================================
# 📦 1. Import Libraries
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folder for graphs
os.makedirs("graphs", exist_ok=True)

# ============================================================
# 📂 2. Load Dataset
# ============================================================
df = pd.read_csv("Railwaygauge_1.csv")

print("Top 5 rows:\n", df.head(), "\n")
print("Missing values:\n", df.isnull().sum(), "\n")

# ============================================================
# 🟢 SCENARIO 1: Data Cleaning
# ============================================================

# Clean column names
df.columns = df.columns.str.strip().str.replace('\ufeff', '')

# Fix Year column (IMPORTANT FIX)
df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Convert gauge columns to numeric safely
cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Fill missing values
df.fillna(0, inplace=True)

# Convert Year to int
df['Year'] = df['Year'].astype(int)

print("\nData Types:\n", df.dtypes)

# ============================================================
# 🟢 SCENARIO 2: Line Graph (Total Tracks)
# ============================================================

plt.figure()
plt.plot(df['Year'], df['Total'], marker='o')
plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Total Tracks')
plt.title('Total Tracks Over Years')

plt.tight_layout()
plt.savefig("graphs/total_over_year.png")
plt.show()

print("Observation: Total tracks show an increasing trend.\n")

# ============================================================
# 🟡 SCENARIO 3: Bar Chart (After 2000)
# ============================================================

df_bar = df[df['Year'] > 2000]

if df_bar.empty:
    print("No data after 2000")
else:
    df_bar.set_index('Year')[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].plot(kind='bar')

    plt.title("Gauge Comparison After 2000")
    plt.xlabel("Year")
    plt.ylabel("Track Length")
    plt.xticks(rotation=70)
    plt.legend()

    plt.tight_layout()
    plt.savefig("graphs/bar_chart.png")
    plt.show()

    print("Observation: Broad Gauge is dominant after 2000.\n")

# ============================================================
# 🟡 SCENARIO 4: Pie Chart
# ============================================================

totals = [
    df["Broad Gauge"].sum(),
    df["Metre Gauge"].sum(),
    df["Narrow Gauge"].sum()
]

plt.figure()
plt.pie(
    totals,
    labels=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
    autopct="%1.1f%%",
    explode=(0.1, 0, 0),
    startangle=180
)

plt.title("Gauge Contribution")
plt.savefig("graphs/pie_chart.png")
plt.show()

print("Observation: Broad Gauge contributes the most.\n")

# ============================================================
# 🔴 SCENARIO 5: Advanced Analysis
# ============================================================

# Ensure Total is correct
df['Total'] = df[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum(axis=1)

# Percentage columns
df['% Broad'] = (df['Broad Gauge'] / df['Total']) * 100
df['% Metre'] = (df['Metre Gauge'] / df['Total']) * 100
df['% Narrow'] = (df['Narrow Gauge'] / df['Total']) * 100

# Growth calculation
df['Growth'] = np.diff(df['Total'], prepend=df['Total'].iloc[0])

# -------- Line Graph (All Gauges) --------
plt.figure()

plt.plot(df['Year'], df['Broad Gauge'], label='Broad', marker='o')
plt.plot(df['Year'], df['Metre Gauge'], label='Metre', marker='o')
plt.plot(df['Year'], df['Narrow Gauge'], label='Narrow', marker='o')

plt.legend()
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Gauge Trends Over Time")

plt.tight_layout()
plt.savefig("graphs/gauge_trends.png")
plt.show()

# -------- Stacked Bar Chart --------
plt.figure()

plt.bar(df['Year'], df['Broad Gauge'], label='Broad')
plt.bar(df['Year'], df['Metre Gauge'], bottom=df['Broad Gauge'], label='Metre')
plt.bar(
    df['Year'],
    df['Narrow Gauge'],
    bottom=df['Broad Gauge'] + df['Metre Gauge'],
    label='Narrow'
)

plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Stacked Gauge Composition")
plt.legend()

plt.tight_layout()
plt.savefig("graphs/stacked_chart.png")
plt.show()

# -------- Analysis --------

# Highest growth year
max_growth_year = df.loc[df['Growth'].idxmax(), 'Year']
print("Year with highest growth:", max_growth_year)

print("\nObservation:")
print("- Broad Gauge is increasing steadily.")
print("- Metre and Narrow Gauges are declining.")

print("\nFinal Conclusion:")
print("Railways are shifting toward a single dominant gauge (Broad Gauge).")
print("Other gauges are being phased out over time.")
