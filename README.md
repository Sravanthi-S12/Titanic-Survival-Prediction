# 🚢 Titanic Survival Prediction

A Machine Learning project that predicts whether a Titanic passenger would survive or not based on passenger information such as passenger class, gender, age, family details, and fare.

---

## 📌 Project Overview

The Titanic Survival Prediction project uses **Python and Machine Learning** to analyze Titanic passenger data and build a **Logistic Regression** model for survival prediction.

The project includes:

- Data loading
- Data preprocessing
- Missing-value handling
- Categorical data encoding
- Train-test splitting
- Machine Learning model training
- Model evaluation
- Passenger survival prediction

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Logistic Regression | Prediction algorithm |
| Matplotlib | Data visualization |
| Seaborn | Graphs and visualization |
| VS Code | Development environment |
| GitHub | Project hosting |

---

## 📂 Project Structure

```text
Titanic-Survival-Prediction/
│
├── Titanic-Dataset-selected-columns.csv
├── titanic_prediction.py
└── README.md


---

🔄 Project Workflow

flowchart TD
    A[Titanic CSV Dataset] --> B[Load Dataset]
    B --> C[Select Required Columns]
    C --> D[Handle Missing Values]
    D --> E[Encode Gender]
    E --> F[Separate Features and Target]
    F --> G[Train-Test Split]
    G --> H[Train Logistic Regression Model]
    H --> I[Make Predictions]
    I --> J[Calculate Accuracy]
    J --> K[Predict Passenger Survival]


---

🧠 Machine Learning Process

flowchart LR
    A[Passenger Data] --> B[Preprocessing]
    B --> C[Training Data]
    B --> D[Testing Data]
    C --> E[Logistic Regression]
    D --> F[Model Evaluation]
    E --> G[Prediction]
    F --> H[Accuracy]


---

📊 Features Used

The model uses the following features:

Feature	Description

Pclass	Passenger class
Sex	Passenger gender
Age	Passenger age
SibSp	Number of siblings/spouses
Parch	Number of parents/children
Fare	Ticket fare


Target Variable

Survived

Where:

0 = Did not survive
1 = Survived

🤖 Machine Learning Algorithm

Logistic Regression

Logistic Regression is used to classify passengers into two categories:

0 → Not Survived
1 → Survived

The model learns patterns from the training data and uses them to make predictions on new passenger data.

🔧 Data Preprocessing

The dataset is prepared before training the model.

flowchart TD
    A[Raw Titanic Data] --> B[Select Features]
    B --> C[Fill Missing Age Values]
    C --> D[Convert Sex to Numeric Values]
    D --> E[Create X and y]
    E --> F[Train-Test Split]

Missing Values

Missing values in the Age column are replaced using the median age.

Encoding

Gender is converted into numerical values so that the Machine Learning model can process it.

📈 Model Evaluation

The model is evaluated using accuracy.

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

The project also generates predictions for a new passenger.

👤 Example Prediction

Example passenger:

Passenger Class: 3
Gender: Male
Age: 25
Siblings/Spouses: 0
Parents/Children: 0
Fare: 7.25

The model produces a prediction:

Passenger is predicted to SURVIVE

or

Passenger is predicted NOT to survive

> The prediction is a machine-learning output and not a historical determination of what happened to an individual passenger.

🖥️ Sample Output

CSV file loaded successfully!

   PassengerId  Survived  Pclass  ...

Model Accuracy: 0.80

Prediction:
Passenger is predicted to SURVIVE

📊 Confusion Matrix

The model can also be evaluated using a confusion matrix.

flowchart TD
    A[Model Predictions] --> B[Confusion Matrix]
    B --> C[True Positive]
    B --> D[True Negative]
    B --> E[False Positive]
    B --> F[False Negative]

The confusion matrix helps compare the model's predictions with the actual outcomes.

▶️ How to Run the Project

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_LINK

2. Open the project in VS Code

cd Titanic-Survival-Prediction

3. Install required libraries

python -m pip install pandas numpy scikit-learn matplotlib seaborn

4. Run the Python file

python titanic_prediction.py

🎯 Project Objectives

Understand Titanic passenger data

Perform basic data preprocessing

Learn categorical encoding

Train a Machine Learning classification model

Evaluate model accuracy

Make survival predictions

🚀 Future Improvements

The project can be improved by adding:

Interactive user input

Tkinter GUI

Streamlit web application

More Machine Learning algorithms

Feature engineering

Confusion matrix visualization

Survival charts

Model comparison

📚 Learning Outcomes

Through this project, I learned:

Python programming

Pandas data manipulation

Data preprocessing

Handling missing values

Label encoding

Train-test splitting

Logistic Regression

Model evaluation

Data visualization

GitHub project management

⭐ Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.

### 📌 For your GitHub

The two **Mermaid diagrams** above will normally render automatically on GitHub. You don't need to create separate image files for them.

For an even better project presentation, you can also add **screenshots of your VS Code output and prediction** under a `screenshots` folder:

```text
Titanic-Survival-Prediction/
│
├── Titanic-Dataset-selected-columns.csv
├── titanic_prediction.py
├── README.md

## 👩‍💻 Author
**Sravanthi**
#Python #MachineLearning #DataAnalysis #DataScience #Pandas #NumPy #Matplotlib #Seaborn #ScikitLearn #TitanicSurvivalPrediction #GitHub #VSCode
