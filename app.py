import streamlit as st
import pickle
import numpy as np

# Load the model
with open('D:/Kidney Disease Prediction System/kidney_disease_2.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_kidney_disease(input_data):
    input_data_as_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data_as_array)
    return prediction[0]

# Streamlit app
def main():
    st.set_page_config(page_title="Kidney Disease Prediction", page_icon="🩺", layout="centered")

    st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #f0f2f6, #cfd9df);
    }
    .title {
        text-align: center;
        color: #333333;
        font-size: 36px;
        font-weight: bold;
        padding-top: 20px;
        padding-bottom: 20px;
    }
    .input-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #008080;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #004c4c;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'><h1 style='text-align: center; color: wheat;'>🌟 Kidney Disease Prediction System 🌟</h1></div>", unsafe_allow_html=True)


    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: wheat;'>Input Parameters 🔍</h2>", unsafe_allow_html=True)
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)

    Age = st.number_input('**:white[**Age**]**', min_value=0, max_value=120, step=1)
    Blood_Pressure = st.number_input('**:white[**Blood Pressure**]**', min_value=0, max_value=200, step=1)
    Specific_Gravity = st.number_input('**Specific Gravity**', min_value=1.000, max_value=1.030, step=0.001, format="%.3f")
    Albumin = st.number_input('**Albumin**', min_value=0, max_value=5, step=1)
    Sugar = st.number_input('**Sugar**', min_value=0, max_value=5, step=1)
    
    Red_Blood_Cells = st.selectbox('**Red Blood Cells**', ['normal', 'abnormal'])
    Pus_Cell = st.selectbox('**Pus Cell**', ['normal', 'abnormal'])
    Pus_Cell_Clumps = st.selectbox('**Pus Cell Clumps**', ['notpresent', 'present'])
    Bacteria = st.selectbox('**Bacteria**', ['notpresent', 'present'])
    
    Blood_Glucose_Random = st.number_input('**Blood Glucose Random**', min_value=0.0, max_value=500.0, step=0.1)
    Blood_Urea = st.number_input('**Blood Urea**', min_value=0.0, max_value=200.0, step=0.1)
    Serum_Creatinine = st.number_input('**Serum Creatinine**', min_value=0.0, max_value=15.0, step=0.1)
    Sodium = st.number_input('**Sodium**', min_value=0.0, max_value=200.0, step=0.1)
    Potassium = st.number_input('**Potassium**', min_value=0.0, max_value=10.0, step=0.1)
    Hemoglobin = st.number_input('**Hemoglobin**', min_value=0.0, max_value=20.0, step=0.1)
    Packed_Cell_Volume = st.number_input('**Packed Cell Volume**', min_value=0.0, max_value=60.0, step=0.1)
    White_Blood_Cell_Count = st.number_input('**White Blood Cell Count**', min_value=0.0, max_value=30000.0, step=0.1)
    Red_Blood_Cell_Count = st.number_input('**Red Blood Cell Count**', min_value=0.0, max_value=10.0, step=0.1)
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: wheat;'>Health Conditions 👩‍⚕️</h2>", unsafe_allow_html=True)
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)

    Hypertension = st.selectbox('**Hypertension**', ['yes', 'no'])
    Diabetes_Mellitus = st.selectbox('**Diabetes Mellitus**', ['yes', 'no'])
    Coronary_Artery_Disease = st.selectbox('**Coronary Artery Disease**', ['yes', 'no'])
    Appetite = st.selectbox('**Appetite**', ['good', 'poor'])
    Pedal_Edema = st.selectbox('**Pedal Edema**', ['yes', 'no'])
    Anemia = st.selectbox('**Anemia**', ['yes', 'no'])

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('**Predict**', help="Click to predict kidney disease"):
        # Mapping input data
        data = [Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar, 
                Red_Blood_Cells, Pus_Cell, Pus_Cell_Clumps, Bacteria, 
                Blood_Glucose_Random, Blood_Urea, Serum_Creatinine, Sodium, 
                Potassium, Hemoglobin, Packed_Cell_Volume, White_Blood_Cell_Count, 
                Red_Blood_Cell_Count, Hypertension, Diabetes_Mellitus, 
                Coronary_Artery_Disease, Appetite, Pedal_Edema, Anemia]

        # Handling categorical values by encoding them
        encoding_maps = {
            'Red_Blood_Cells': {'normal': 0, 'abnormal': 1},
            'Pus_Cell': {'normal': 0, 'abnormal': 1},
            'Pus_Cell_Clumps': {'notpresent': 0, 'present': 1},
            'Bacteria': {'notpresent': 0, 'present': 1},
            'Hypertension': {'yes': 1, 'no': 0},
            'Diabetes_Mellitus': {'yes': 1, 'no': 0},
            'Coronary_Artery_Disease': {'yes': 1, 'no': 0},
            'Appetite': {'good': 0, 'poor': 1},
            'Pedal_Edema': {'yes': 1, 'no': 0},
            'Anemia': {'yes': 1, 'no': 0}
        }

        # Apply encoding to categorical inputs
        data[5] = encoding_maps['Red_Blood_Cells'][data[5]]
        data[6] = encoding_maps['Pus_Cell'][data[6]]
        data[7] = encoding_maps['Pus_Cell_Clumps'][data[7]]
        data[8] = encoding_maps['Bacteria'][data[8]]
        data[18] = encoding_maps['Hypertension'][data[18]]
        data[19] = encoding_maps['Diabetes_Mellitus'][data[19]]
        data[20] = encoding_maps['Coronary_Artery_Disease'][data[20]]
        data[21] = encoding_maps['Appetite'][data[21]]
        data[22] = encoding_maps['Pedal_Edema'][data[22]]
        data[23] = encoding_maps['Anemia'][data[23]]

        result = predict_kidney_disease(data)
        
        # Display the result
        if result == 0:
            st.error('🚨 The person is suffering from Chronic Kidney Disease (CKD).')
        elif result == 1:
            st.success('✅ The person is not suffering from Chronic Kidney Disease (CKD).')
        else:
            st.warning('⚠️ Unexpected prediction result.')

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
