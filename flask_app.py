from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('D:/Kidney Disease Prediction System/kidney_disease_2.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_kidney_disease(input_data):
    input_data_as_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data_as_array)
    return prediction[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    input_data = [
        int(data['Age']),
        int(data['Blood_Pressure']),
        float(data['Specific_Gravity']),
        int(data['Albumin']),
        int(data['Sugar']),
        0 if data['Red_Blood_Cells'] == 'normal' else 1,
        0 if data['Pus_Cell'] == 'normal' else 1,
        0 if data['Pus_Cell_Clumps'] == 'notpresent' else 1,
        0 if data['Bacteria'] == 'notpresent' else 1,
        float(data['Blood_Glucose_Random']),
        float(data['Blood_Urea']),
        float(data['Serum_Creatinine']),
        float(data['Sodium']),
        float(data['Potassium']),
        float(data['Hemoglobin']),
        float(data['Packed_Cell_Volume']),
        float(data['White_Blood_Cell_Count']),
        float(data['Red_Blood_Cell_Count']),
        1 if data['Hypertension'] == 'yes' else 0,
        1 if data['Diabetes_Mellitus'] == 'yes' else 0,
        1 if data['Coronary_Artery_Disease'] == 'yes' else 0,
        0 if data['Appetite'] == 'good' else 1,
        1 if data['Pedal_Edema'] == 'yes' else 0,
        1 if data['Anemia'] == 'yes' else 0
    ]

    result = predict_kidney_disease(input_data)
    prediction = 'The person is not suffering from Chronic Kidney Disease (CKD).' if result == 1 else 'The person is suffering from Chronic Kidney Disease (CKD).'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
