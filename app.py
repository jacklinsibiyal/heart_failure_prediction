from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a function to preprocess the input
def preprocess_input(data):
    # Directly use the selected option values as they are
    data['Sex'] = 1 if data['Sex'] == 'Male' else 0  # Male is 1, Female is 0

    # Convert 'FastingBS' to numerical format
    data['FastingBS'] = 1 if data['FastingBS'].lower() == 'yes' else 0  # Yes = 1, No = 0

    # Convert 'ExerciseAngina' to numerical format
    data['ExerciseAngina'] = 1 if data['ExerciseAngina'].lower() == 'yes' else 0  # Yes = 1, No = 0

    # Map 'ChestPainType' to numerical values
    chest_pain_map = {
        'ATA': 1,  # Typical Angina
        'NAP': 2,  # Non-Anginal Pain
        'ASY': 0,  # Asymptomatic
        'TA': 3    # Atypical Angina
    }
    data['ChestPainType'] = chest_pain_map[data['ChestPainType']]

    # Map 'RestingECG' to numerical values
    resting_ecg_map = {
        'Normal': 0,
        'ST': 1,
        'LVH': 2
    }
    data['RestingECG'] = resting_ecg_map[data['RestingECG']]

    # Map 'ST_Slope' to numerical values
    st_slope_map = {
        'Up': 2,
        'Flat': 1,
        'Down': 0
    }
    data['ST_Slope'] = st_slope_map[data['ST_Slope']]

    # Set default values for empty fields and convert to the correct types
    data['Age'] = int(data.get('Age', 50)) if data.get('Age') else 50
    data['RestingBP'] = float(data.get('RestingBP', 80)) if data.get('RestingBP') else 80
    data['Cholesterol'] = float(data.get('Cholesterol', 200)) if data.get('Cholesterol') else 200
    data['MaxHR'] = float(data.get('MaxHR', 120)) if data.get('MaxHR') else 120
    data['Oldpeak'] = float(data.get('Oldpeak', 0)) if data.get('Oldpeak') else 0

    # Return processed data as a NumPy array for prediction
    return np.array([[data['Age'], data['Sex'], data['ChestPainType'], data['RestingBP'], data['Cholesterol'],
                      data['FastingBS'], data['RestingECG'], data['MaxHR'], data['ExerciseAngina'],
                      data['Oldpeak'], data['ST_Slope']]])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'Age': request.form.get('Age', ''),
        'Sex': request.form.get('Sex', ''),
        'ChestPainType': request.form.get('ChestPainType', ''),
        'RestingBP': request.form.get('RestingBP', ''),
        'Cholesterol': request.form.get('Cholesterol', ''),
        'FastingBS': request.form.get('FastingBS', ''),
        'RestingECG': request.form.get('RestingECG', ''),
        'MaxHR': request.form.get('MaxHR', ''),
        'ExerciseAngina': request.form.get('ExerciseAngina', ''),
        'Oldpeak': request.form.get('Oldpeak', ''),
        'ST_Slope': request.form.get('ST_Slope', '')
    }

    # Preprocess the input
    input_data = preprocess_input(data)
    
    # Make prediction
    prediction_proba = model.predict_proba(input_data)
    heart_failure_prob = prediction_proba[0][1] * 100  # Get probability of heart failure
    
    return render_template('result.html', probability=heart_failure_prob)

if __name__ == '__main__':
    app.run(debug=True, port=5001)