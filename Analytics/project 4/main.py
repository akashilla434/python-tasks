import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------------
# SCENARIO 1:Data Loading & Basic Cleaning
# ---------------------------------------------------------------------------------
#1. Load the dataset using Pandas. 
#2. Display: 
#○ Column names 
#3. Check for missing values in: 
#○ bedrooms 
#○ bathrooms 
#○ sqft_living 
#○ price 
#4. Fill missing values: 
#○ bedrooms → use mode 
#○ bathrooms → use mean 
#○ sqft_living → use mean 
#○ price → use mean 
#○ bedrooms 
#○ bathrooms 
#○ sqft_living 
#○ price 
df = pd.read_csv("house_sales.csv")
print("First 5 Rows:")
print(df.head())
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values Before Filling:")
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())
df["bedrooms"].fillna(df["bedrooms"].mode()[0], inplace=True)
df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True)
df["sqft_living"].fillna(df["sqft_living"].mean(), inplace=True)
df["price"].fillna(df["price"].mean(), inplace=True)
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bathrooms"] = pd.to_numeric(df["bathrooms"], errors="coerce")
df["sqft_living"] = pd.to_numeric(df["sqft_living"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
print("\nMissing Values After Filling:")
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())

##--------------------------------------------------------------------------------
## SCENARIO 2:Line Graph + Save
##-----------------------------------------------------------------------------------
##1. Select:
##○ id
##○ price
##2. Take the first 10 rows only.
##3. Convert price into a NumPy array.
##4. Plot a line graph:
## ○ X-axis → index (0–9)
# #○ Y-axis → Price
##5 Add:
# #○ Title
# #○ X-label
##○ Y-label
##6. Save the graph: plt.savefig("house_prices_line.png")
df=pd.read_csv('House_sales.csv')
df_subset = df[['id', 'price']].head(10)
price_array = df_subset['price'].to_numpy()
plt.plot(price_array, marker='o') # Automatically uses index 0-9 for X-axis
plt.title("House Prices (First 10 Records)")
plt.xlabel("Index (0–9)")
plt.ylabel("Price")
plt.savefig("graph/house_prices_line.png")
plt.show()
# -------------------------------------------------------------------------------
# SCENARIO 3:  Filtering + Bar Chart + Save
# -------------------------------------------------------------------------------
#1. Filter houses where: 
#○ price > 1000000 
#2. Count number of houses per: 
#○ bedrooms 
#3. Select top bedroom categories. 
#4. Convert results to NumPy arrays. 
#5. Plot a bar chart: 
#○ X-axis → Bedrooms 
#○ Y-axis → Count 
#6. Rotate labels if needed. 
#7. Save graph: plt.savefig("expensive_houses_bar.png")
df = pd.read_csv("house_sales.csv")
print("Current Folder:", os.getcwd())
print("Files:", os.listdir())
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bedrooms"] = df["bedrooms"].round().astype(int)
expensive_houses = df[df["price"] > 300000]
print("Total expensive houses:", len(expensive_houses))
bedroom_counts = expensive_houses["bedrooms"].value_counts()
top_bedrooms = bedroom_counts.head(5)
print("\nTop Bedroom Categories:")
print(top_bedrooms)
plt.figure(figsize=(8,5))
plt.bar(top_bedrooms.index, top_bedrooms.values)
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")
plt.xticks(rotation=0)
plt.savefig("graph/expensive_houses_bar_correct.png")
plt.show()
# -----------------------------------------------------------------------------------
# SCENARIO 4: Pie Chart (Bedroom Distribution) + Save 
# -----------------------------------------------------------------------------------
#1. Count number of houses by: 
#○ bedrooms 
#2. Select top 5 bedroom categories. 
#3. Prepare: 
#○ Labels 
#4. Plot a pie chart. 
#5. Add percentage labels. 
#6. Save graph: plt.savefig("bedroom_distribution.png")
# Load the dataset
df = pd.read_csv("house_sales.csv")
bedroom_counts = df['bedrooms'].value_counts()
top_5_bedrooms = bedroom_counts.head(5)
labels = [f"{int(b)} Bedrooms" for b in top_5_bedrooms.index]
values = top_5_bedrooms.values
plt.figure(figsize=(10, 7))
plt.pie(values, labels=labels,autopct='%1.1f%%')
plt.title('Distribution of Houses by Top 5 Bedroom Categories')
plt.axis('equal')  
plt.savefig("graph/bedroom_distribution.png")
print("Pie chart successfully generated and saved as 'bedroom_distribution.png'")

# ------------------------------------------------------------------------------------
# SCENARIO 5: Advanced Analysis + Multiple Graphs 
# ------------------------------------------------------------------------------

#Part 1: Feature Creation 
#Create a new column: 
#Price Category 
#● price >= 1000000 → "Luxury" 
#● 500000 – 999999 → "Mid Range" 
#● < 500000 → "Affordable" 
#Part 2: NumPy Usage 
#1. Convert price column to a NumPy array. 
#2. Calculate price differences using: np.diff()
#Part 3: Visualizations 
#Line Graph 
#Plot price trend for all houses. 
#Stacked Bar Chart 
#Show count of Price Category per Bedrooms. 
#Histogram 
#Plot distribution of: 
#● price 
#Part 4: Save All Graphs 
#plt.savefig("price_trend.png") 
#plt.savefig("price_category_stacked.png") 
#plt.savefig("price_histogram.png") 
#Part 5: Insights 
#Answer these: 
#1. Which bedroom category has the most expensive houses? 
#2. Which price category is most common? 
#3. What is the distribution pattern of house prices? 
#○ Right-skewed? 
#○ Normal?
#○ Concentrated in a lower price range?
df = pd.read_csv("house_sales.csv")
def categorize_price(price):
    if price >= 1000000:
        return "Luxury"
    elif price >= 500000:
        return "Mid Range"
    else:
        return "Affordable"
df["price_category"] = df["price"].apply(categorize_price)
print("\nPrice Category Counts:")
print(df["price_category"].value_counts())
price_array = df["price"].dropna().to_numpy()
price_diff = np.diff(price_array)
print("\nFirst 10 Price Differences:")
print(price_diff[:10])
plt.figure(figsize=(10,5))
plt.plot(price_array[:100], marker='o', color="green")
plt.title("House Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("graph/price_trend.png")
plt.show()
stack_data = df.groupby(["bedrooms", "price_category"]).size().unstack(fill_value=0)
stack_data = stack_data.sort_index().head(5)
stack_data.plot(kind='bar', figsize=(10,6))
plt.title("Price Category Distribution by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("graph/price_category_stacked.png")
plt.show()
plt.figure(figsize=(10,5))
upper_limit = df["price"].quantile(0.95)
filtered_prices = df[df["price"] <= upper_limit]["price"]
plt.hist(filtered_prices, bins=30, color="gold")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()
plt.savefig("graph/price_histogram.png")
plt.show()
print("\n===== FINAL INSIGHTS =====")
luxury = df[df["price_category"] == "Luxury"]
top_bedroom = luxury["bedrooms"].value_counts().idxmax()
print("1. Bedroom category with most luxury houses:", top_bedroom)
common_category = df["price_category"].value_counts().idxmax()
print("2. Most common price category:", common_category)
print("3. Price distribution is right-skewed.")
print("\n ALL TASKS COMPLETED SUCCESSFULLY!")
print(" All graphs saved in:", save_path)
#---------------------------------------------------------------------------------------
#-----------------------------the end---------------------------------------------------



