import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
products = ["Pen", "Book", "Pencil"]
sales = ([50, 80, 40])
df=pd.DataFrame({"products":products,"sales":sales})
print(df)
plt.bar(df["products"],df["sales"])
plt.title("product Sales Bar Chart")
plt.xlabel("products")
plt.ylabel("sales")
plt.show()

