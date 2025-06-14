# Heart Disease Detection

This repository contains a simple web-based application for predicting the risk of heart disease based on user input. The app uses a machine learning model to analyze data provided by the user and assess the likelihood of heart disease.

## Files in This Repository

1. **data.csv**: A dataset containing relevant medical data that the application uses for prediction. This data helps train the model to make accurate heart disease risk predictions.

2. **app.py**: The backend of the application, implemented in Python using Flask. This script loads the machine learning model and provides an API endpoint (`/predict`) to which the frontend sends user input data for prediction. The endpoint returns a high or low risk prediction based on the model's output.

3. **index.html**: The frontend of the application, which contains a form for users to input their health metrics (e.g., age, cholesterol level, blood pressure). Once the form is submitted, the data is sent to the backend API, and the predicted risk level is displayed on the webpage.

## Usage

1. **Set up the Environment**:
   - Install the required Python packages:
     ```bash
     pip install flask
     ```
   - Additional dependencies may be required based on the machine learning model used.

2. **Run the Application**:
   - Start the Flask server by running:
     ```bash
     python app.py
     ```
   - This should start the server at `http://127.0.0.1:5000/`.

3. **Access the Application**:
   - Open `index.html` in a web browser or visit `http://127.0.0.1:5000/`.
   - Input the required health metrics and click "Predict" to receive a heart disease risk assessment.

## Features

- **Responsive UI**: The frontend design is mobile-friendly and easy to use.
- **Real-time Prediction**: The model predicts heart disease risk instantly after data submission.
- **Error Handling**: Handles errors gracefully, with user-friendly messages in case of prediction issues.

## License

This project is open-source and licensed under the MIT License.
