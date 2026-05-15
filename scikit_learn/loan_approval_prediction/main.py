#C:/Users/De
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Generate Synthetic Loan Dataset
np.random.seed(42)
n_samples = 1000

data = pd.DataFrame({
    'Applicant_Income': np.random.randint(20000, 150000, n_samples),
    'Loan_Amount': np.random.randint(10000, 500000, n_samples),
    'CIBIL_Score': np.random.randint(300, 900, n_samples),
    'Education': np.random.choice(['Graduate', 'Not Graduate'], n_samples),
    'Self_Employed': np.random.choice(['Yes', 'No'], n_samples)
})

# Define standard rule logic for approval (Target Variable)
# Approved if CIBIL score is fair/high or income comfortably covers loan
condition = (data['CIBIL_Score'] > 600) | ((data['Applicant_Income'] * 3) > data['Loan_Amount'])
data['Loan_Status'] = np.where(condition, 'Approved', 'Rejected')

# 2. Data Preprocessing
le = LabelEncoder()
data['Education'] = le.fit_transform(data['Education'])
data['Self_Employed'] = le.fit_transform(data['Self_Employed'])
data['Loan_Status'] = le.fit_transform(data['Loan_Status']) # Approved: 0, Rejected: 1

# Split features and target variable
X = data.drop('Loan_Status', axis=1)
y = data['Loan_Status']

# Create training and validation sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Approved', 'Rejected']))

# 5. Visualizing Model Performance & Feature Importance
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax[0],
            xticklabels=['Approved', 'Rejected'], yticklabels=['Approved', 'Rejected'])
ax[0].set_title('Confusion Matrix')
ax[0].set_xlabel('Predicted Status')
ax[0].set_ylabel('Actual Status')

# Plot 2: Feature Importance Bar Plot
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns

sns.barplot(x=importances[indices], y=features[indices], palette='viridis', ax=ax[1])
ax[1].set_title('Feature Importance Matrix')
ax[1].set_xlabel('Relative Importance Score')

plt.tight_layout()
plt.show()
