# =========================================
# 🌸 Iris Flower Prediction Project
# Using 2 Algorithms + Graphs
# =========================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# =========================================
# Load Dataset
# =========================================

data = pd.read_csv("Iris.csv")

# Show First 5 Rows
print(data.head())

# =========================================
# Input and Output
# =========================================

X = data.drop(["Species", "Id"], axis=1)
y = data["Species"]

# =========================================
# Split Dataset
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================
# Algorithm 1 : KNN
# =========================================

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

knn_acc = accuracy_score(y_test, knn_pred)

print("\nKNN Accuracy:", knn_acc)

# =========================================
# Algorithm 2 : Decision Tree
# =========================================

dt = DecisionTreeClassifier()

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

dt_acc = accuracy_score(y_test, dt_pred)

print("Decision Tree Accuracy:", dt_acc)

# =========================================
# GRAPH 1 : Accuracy Comparison
# =========================================

algorithms = ["KNN", "Decision Tree"]
accuracy = [knn_acc, dt_acc]

plt.bar(algorithms, accuracy)

plt.xlabel("Algorithms")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison Graph")


plt.show()

# =========================================
# GRAPH 2 : Flower Count
# =========================================

data["Species"].value_counts().plot(kind="bar")

plt.xlabel("Flower Type")
plt.ylabel("Count")
plt.title("Iris Flower Count Graph")


plt.show()

# =========================================
# GRAPH 3 : Scatter Plot
# =========================================

plt.scatter(
    data["SepalLengthCm"],
    data["PetalLengthCm"]
)

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal vs Petal Length")


plt.show()
