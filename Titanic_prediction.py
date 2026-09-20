import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load CSV file
df = pd.read_csv("Titanic-Dataset-selected-columns.csv")

print("CSV file loaded successfully!")
print(df.head())

# Select columns
data = df[[
    "Survived",
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]].copy()

# Fill missing Age values
data["Age"] = data["Age"].fillna(data["Age"].median())

# Convert Sex to numbers
encoder = LabelEncoder()
data["Sex"] = encoder.fit_transform(data["Sex"])

# Input and output
X = data.drop("Survived", axis=1)
y = data["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Test a new passenger
new_passenger = [[3, 0, 25, 0, 0, 7.25]]

prediction = model.predict(new_passenger)

print("\nPrediction:")

if prediction[0] == 1:
    print("Passenger is predicted to SURVIVE")
else:
    print("Passenger is predicted NOT to survive")