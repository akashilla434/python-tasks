# ============================================================
# 📊 Project Title: ign.csv
# Analyze ra
# ============================================================
# ============================================================
# 📦 1. Import Required Libraries
# ===========================================================
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
# ======================================================================
  # 🟢 SCENARIO 1: Data Loading & Preprocessing
# ========================================================================
#. Load the dataset using Pandas.
"""
1. Display:
   ○ First 5 rows (head())
   ○ Last 5 rows (tail())
   ○ Shape of dataset
2. Remove the unnecessary column:
   ○ "Unnamed: 0" (index column)
3. Check for missing values in:
   ○ score, genre, platform
4. Handle missing values:
   ○ Fill numeric column score with mean
   ○ Fill categorical column genre with mode
5. Ensure correct data types:
   ○ score → float
   ○ release_year, release_month, release_day → integer
"""
df = pd.read_csv('ign.csv')
print("First 5 rows:")
print(df.head())    
print("\nLast 5 rows:")
print(df.tail())
print("\nShape of dataset (Rows, Columns):")
print(df.shape)     
df.drop(columns=['Unnamed: 0'], inplace=True)
print("\nMissing values in key columns:")
print(df[['score', 'genre', 'platform']].isnull().sum())
df['score'] = df['score'].fillna(df['score'].mean())
df['genre'] = df['genre'].fillna(df['genre'].mode(0))
df['score'] = df['score'].astype(float)
df['release_year'] = df['release_year'].astype(int)
df['release_month'] = df['release_month'].astype(int)
df['release_day'] = df['release_day'].astype(int)
print("\nFinal data types:")
print(df.dtypes)

"""

#===============================================================================
  #🟢 SCENARIO 2: Line Graph (Total Tracks)
#=====================================================================================
#1. Group data by release_year.
#2. Calculate average score per year using Pandas.
#3. Convert results into NumPy arrays.
#4. Plot a line graph:
        ○ X-axis → release_year
        ○ Y-axis → average score
#5. Add:
        ○ Title: "Average Game Score Over Years"
        ○ Axis labels
#6. Save the graph: plt.savefig("avg_score_trend.png")
"""
grp=df.groupby('release_year')
avg=grp['score'].mean()
print(avg)
years_arr = avg.index.to_numpy()
scores_arr = avg.to_numpy()
print("Years Array:\n", years_arr)
print("Scores Array:\n", scores_arr)
plt.clf()
plt.plot(years_arr,scores_arr,marker='o')
plt.title('Average Game Score Over Years')
plt.xlabel('Release Year')
plt.ylabel('Average Score')
plt.tight_layout()
plt.savefig('Graph/avg_score_trend.png')

"""
# ===============================================================================
# 🟡 SCENARIO 3: Filtering + Bar Chart + Save 
# ================================================================================
#1. Group data by release_year.
#2. Calculate average score per year using Pandas.
#3. Convert results into NumPy arrays.
#4. Plot a line graph:
    ○ X-axis → release_year
    ○ Y-axis → average score
#5. Add:
    ○ Title: "Average Game Score Over Years"
    ○ Axis labels
#6. Save the graph: plt.savefig("avg_score_trend.png")
Filtering + Bar Chart + Save

# Filtering dataset where score > 7
filtered_data = data[data['score'] > 7]
print("------------------------------------------------------------------------------")

# Count number of high-rated games per platform
top_rated_games = filtered_data.groupby('platform')['title'].count()
print(top_rated_games)
print("------------------------------------------------------------------------------")

# Select top 10 platforms based on count
top_10 = top_rated_games.sort_values(ascending=False).head(10)
print(top_10)
print("------------------------------------------------------------------------------")

# Convert to NumPy arrays
platforms = top_10.index.to_numpy()
counts = top_10.values
print(platforms)
print(counts)

# Plotting bar chart
plt.figure()
plt.bar(platforms, counts)
plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()
# Save before show
#plt.savefig("graph/top_platforms_bar.png")
#plt.show()
# =============================================================================
# 🟡 SCENARIO 4: Aggregation + Pie Chart + Save 
# =============================================================================
#1. Count the number of games per genre.
#2. Select top 5 genres using Pandas.
#3. Prepare labels and values.
#4. Plot a pie chart:
    ○ Labels → genre
    ○ Values → count
#5. Add percentage labels (autopct).
Save the graph: plt.savefig("genre_distribution.png")
  """
gen_count=df['genre'].value_counts()
print(gen_count)
top_5=gen_count.head()
print(top_5)
labels=top_5.index
values=top_5.values
plt.clf()
plt.pie(values,labels=labels,autopct="%1.1f%%")
plt.title('genre_distribution')
plt.tight_layout()
plt.savefig("Graph/genre_distribution.png")
plt.show()
"""

# ================================================================================
# 🔴 SCENARIO 5: Advanced analysis+multiple graph
# =================================================================================
#You are asked to perform a detailed analysis of review patterns. 
#part 1: Feature Engineering 
#1. Create a new column: 
    ○ score_category: 
        score >= 9 → "Excellent" 
        7 <= score < 9 → "Good" 
        < 7 → "Average" 
#2. Convert editors_choice: 
     ○ Y → 1, N → 0
     Part 2: NumPy Analysis 
#3. Use NumPy to: 
    ○ Calculate yearly score growth using np.diff() on average yearly scores 
Part 3: Visualizations 
Line Graph 
#4. Plot trend of: 
    ○ Average score per release_year 
Stacked Bar Chart 
#5. Show count of: 
    ○ score_category per release_year 
Histogram 
#6. Plot distribution of: 
    ○ score
"""

os.makedirs("Graph", exist_ok=True)
df = pd.read_csv("ign.csv")
df["score_category"] = np.where(df["score"] >= 9, "Excellent",
                        np.where(df["score"] >= 7, "Good", "Average"))
df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0})
yearly_scores = df.groupby("release_year")["score"].mean()
years = yearly_scores.index.values
avg_scores = yearly_scores.values
score_growth = np.diff(avg_scores)
print("Yearly Score Growth:", score_growth)
plt.figure()
plt.plot(years, avg_scores, marker='o')
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid()
plt.savefig("Graph/score_trend.png")
plt.show()
category_counts = df.groupby(["release_year", "score_category"]).size().unstack().fillna(0)
category_counts.plot(kind="bar", stacked=True)
plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.savefig("Graph/score_category_stacked.png")
plt.show()
plt.figure()
plt.hist(df["score"], bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("Graph/score_distribution.png")
plt.show()

# -------------------------------
# 👉 Part 5: Insights
# -------------------------------

# Highest score year
max_year = yearly_scores.idxmax()
print("Year with highest average score:", max_year)

# Trend check
if avg_scores[-1] > avg_scores[0]:
    print("Scores increased over time")
else:
    print("Scores did not increase over time")

# Editors choice vs score
correlation = df["editors_choice"].corr(df["score"])
print("Correlation between editor's choice and score:", correlation)

#=======================endof the file=======================================
