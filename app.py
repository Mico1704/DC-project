
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Title of the Streamlit app
st.title("Heart Disease Prediction")

# User input for model features
st.header("Enter the patient data:")
age = st.number_input("Age", min_value=0, max_value=120, value=25, step=1)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
chol = st.number_input("Cholesterol Level", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [1, 0])
restecg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2, value=0)
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [1, 0])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", min_value=0, max_value=2, value=1)
ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4, value=0)
thal = st.number_input("Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect)", min_value=0, max_value=2, value=1)

# Button for prediction
if st.button("Predict"):
    # Load the trained model (for this example, it's a simple LogisticRegression with training in the same script)
    # Normally, you'd load a pre-trained model from a file using joblib or pickle.
    
    # Placeholder data for example purposes
    data = pd.DataFrame({
        'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps],
        'chol': [chol], 'fbs': [fbs], 'restecg': [restecg],
        'thalach': [thalach], 'exang': [exang], 'oldpeak': [oldpeak],
        'slope': [slope], 'ca': [ca], 'thal': [thal]
    })
    
    # Train a simple model for demonstration purposes
    # You may replace this with loading your own trained model
    df = pd.read_csv('data.csv') # Replace with actual data path
    X = df.drop(columns='target')
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Prediction
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.success("The patient is likely to have heart disease.")
    else:
        st.success("The patient is unlikely to have heart disease.")
