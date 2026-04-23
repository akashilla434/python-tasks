import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales=np.array([100, 150, 200, 250, 300])
months= ["Jan", "Feb", "Mar", "Apr", "May"]
df = pd.DataFrame({"month":months,"sales":sales})
print(df)
plt.figure(figsize=(6,4))
plt.plot(df["month"],df["sales"],marker="o")
plt.title("monthly salary trend")
plt.xlabel("months")
plt.ylabel("sales")
plt.savefig("monthly sales line.jpeg")
plt.show()

