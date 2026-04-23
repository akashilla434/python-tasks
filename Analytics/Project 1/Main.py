import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
#1. Load the dataset into a Pandas DataFrame.
df=pd.read_csv("Railwaygauge_1.csv")
#2.display the first 5 rows and column names.
print("top 5 Rows are\n",df.head(),'\n')
#3.. Check for missing values and replace them with 0.
# mising values check for column
print("missing values are\n",df.isnull().sum(),'\n')
#returns
missing_row=df[df.isnull().any(axis=1)]
print(missing_row)
#replaceing missing values with 0

print(df)
#4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
df["Broad Gauge"]=pd.to_numeric(df["Broad Gauge"])
df["Metre Gauge"]=pd.to_numeric(df["Metre Gauge"])
df["Narrow Gauge"]=pd.to_numeric(df["Narrow Gauge"])
df["Total"]=pd.to_numeric(df["Total"])
print(df.info())
"""
#=======================================================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""

#2.1 Extract Year and Total columns.
df=pd.read_csv("railwaygauge_1.csv")
print(df[['Total','Year']])

#2.2 Plot a line graph showing Total tracks over years.
plt.plot(df['Year'],df['Total'])
plt.xticks(rotation=70)

#2.3 Add: Title X and Y labels
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Total vs Years')
plt.savefig("total_over_year.png")

#2.4 Identify whether the trend is increasing or decreasing.
plt.show()
"""

#=====================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
import os
"""
df = pd.read_csv("railwaygauge_1.csv")
df.columns = df.columns.str.strip().str.replace('\ufeff','')

# Show columns
print("Columns:", df.columns)
year_col = df.columns[0]

# Convert Year
df[year_col] = pd.to_numeric(df[year_col].astype(str).str[:4], errors='coerce')

# 1. Filter after 2000
df = df[df[year_col] > 2000]

# Check empty
if df.empty:
    print("No data after 2000")
else:
    # 2. Select columns
    df = df[[year_col, "Broad Gauge", "Metre Gauge", "Narrow Gauge"]]

    # 3. Plot grouped bar chart
    df.set_index(year_col).plot(kind='bar')

    # 4. Labels
    plt.title("Comparison of Railway Gauges After 2000")
    plt.xlabel("Year")
    plt.ylabel("Track Length")
    plt.legend()

    # Save graph
    os.makedirs("Graphs", exist_ok=True)
    plt.savefig("Graphs/Broad_Metre_Narrow_bar.png")

    plt.show()

    # 5. Dominating gauge
    total = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()
    print("Dominating gauge:", total.idxmax())


    """

#==============================================================================================



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
df=pd.read_csv("Railwaygauge_1.csv")
df[["Broad Gauge","Metre Gauge","Narrow Gauge"]]
s_total=pd.Series({"BGT":df["Broad Gauge"].sum(),
                      "MGT":df["Metre Gauge"].sum(),
                      "NGT":df["Narrow Gauge"].sum()})
#print(s_total)
plt.pie(s_total,labels=["Broad Gauge","Metre Gauge","Narrow Gauge"],
        autopct="%1.1f%%",explode=(0.1,0,0),startangle=180)
plt.title("percentage contribution")
plt.show()
print("Broad Gauge contributes the most to the total railway network among all gauge types.")

"""
#======================================================================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
df=pd.read_csv('Railwaygauge_1.csv')
df['total']=df[['Broad Gauge','Metre Gauge','Narrow Gauge']].sum(axis=1)
# Create percentage columns
df['% Broad'] = (df['Broad Gauge'] / df['Total']) * 100
df['% Metre'] = (df['Metre Gauge'] / df['Total']) * 100
df['% Narrow'] = (df['Narrow Gauge'] / df['Total']) * 100

# Calculate yearly growth using NumPy
df['Growth'] = np.diff(df['Total'], prepend=df['Total'].iloc[0])

# Line graph for all gauges
plt.plot(df['Year'], df['Broad Gauge'], label='Broad', marker = 'o')
plt.plot(df['Year'], df['Metre Gauge'], label='Metre', marker = 'o')
plt.plot(df['Year'], df['Narrow Gauge'], label='Narrow', marker = 'o')

plt.legend()
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Line graph Gauge Trends Over Time")

plt.tight_layout()
plt.savefig("graphs/gauge_trends.png")
plt.show()

# Stacked bar chart
plt.bar(d['Year'], df['Broad Gauge'], label='Broad')
plt.bar(d['Year'], df['Metre Gauge'], bottom=d['Broad Gauge'], label='Metre')
plt.bar(d['Year'], df['Narrow Gauge'], bottom=d['Broad Gauge'] + d['Metre Gauge'], label='Narrow')

plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Stacked bar graph Gauge Composition")
plt.legend()

plt.tight_layout()
plt.savefig("graphs/stacked_chart.png")
plt.show()

# Identify highest growth
print("Year with highest growth:")
print(d.loc[d['Growth'].idxmax()])
"""
#-----------------------------End of the file------------------------------------------------------------
