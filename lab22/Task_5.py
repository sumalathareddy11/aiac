import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample dataset
data = {
    "ApplicantIncome": [2500, 4000, 6000, 3500, 8000, 12000, 3000, 10000, 7000, 2000],
    "CreditScore": [600, 650, 700, 620, 720, 750, 630, 800, 680, 580],
    "LoanAmount": [100, 150, 200, 130, 250, 300, 120, 350, 180, 90],
    "LoanTerm": [12, 24, 36, 24, 48, 60, 12, 60, 36, 12],
    "EmploymentYears": [1, 3, 5, 2, 6, 10, 1, 8, 4, 0],
    "Approved": ["No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# Features and target
X = df.drop("Approved", axis=1)
y = df["Approved"]

# Train model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# -------------------------------
# User Input
# -------------------------------
print("Enter applicant details to predict loan approval:")

applicant_income = float(input("Applicant Income: "))
credit_score = float(input("Credit Score: "))
loan_amount = float(input("Loan Amount: "))
loan_term = int(input("Loan Term (months): "))
employment_years = int(input("Years of Employment: "))

# Prepare input for prediction
sample_applicant = pd.DataFrame({
    "ApplicantIncome": [applicant_income],
    "CreditScore": [credit_score],
    "LoanAmount": [loan_amount],
    "LoanTerm": [loan_term],
    "EmploymentYears": [employment_years]
})

predicted = model.predict(sample_applicant)[0]
print("\nPredicted Loan Approval:", predicted)
