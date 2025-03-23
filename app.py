import streamlit as st
import pickle
import time
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Medical Diagnosis App", page_icon="⚕️", layout="wide")
# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Custom Sidebar Styling
sidebar_style = """
<style>
[data-testid="stSidebar"] {
    background-color: #262730; /* Dark blue background */
    color: white; /* White text */
}

[data-testid="stSidebar"] .stButton>button {
    background-color: #2DD4BF; /* Teal button */
    color: white;
    border-radius: 4px;
    padding: 10px 24px;
    border: none;
    font-size: 16px;
    transition: background-color 0.3s ease;
}

[data-testid="stSidebar"] .stButton>button:hover {
    background-color: #1E3A8A; /* Dark blue on hover */
}

[data-testid="stSidebar"] .stSelectbox>div>div>select {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 4px;
    padding: 10px;
    border: 1px solid #ccc;
    color: #1E3A8A; /* Dark blue text */
}

[data-testid="stSidebar"] .stSelectbox>div>div>select:focus {
    border-color: #2DD4BF; /* Teal border on focus */
}
</style>
"""
st.markdown(sidebar_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://retinalscreenings.com/wp-content/uploads/2022/02/AdobeStock_317687329-scaled.jpeg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.8);
}}

.stButton>button {{
    background-color: #1E3A8A;
    color: white;
    padding: 10px 24px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
}}

.stButton>button:hover {{
    background-color: #2DD4BF;
}}

.stTextInput>div>div>input, .stNumberInput>div>div>input {{
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 4px;
    padding: 10px;
    border: 1px solid #ccc;
    transition: border-color 0.3s ease;
}}

.stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {{
    border-color: #1E3A8A;
}}

.stSelectbox>div>div>select {{
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 4px;
    padding: 10px;
    border: 1px solid #ccc;
    transition: border-color 0.3s ease;
}}

.stSelectbox>div>div>select:focus {{
    border-color: #1E3A8A;
}}

.stTitle {{
    color: white;
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}}

.stHeader {{
    color: white;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}}

.stMarkdown {{
    color: white;
    font-size: 18px;
    margin-bottom: 20px;
}}

.stSuccess {{
    color: #10B981;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 4px;
    background-color: rgba(16, 185, 129, 0.1);
    border: 1px solid #10B981;
}}

.stError {{
    color: #EF4444;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 4px;
    background-color: rgba(239, 68, 68, 0.1);
    border: 1px solid #EF4444;
}}

.stProgress {{
    margin-top: 20px;
    margin-bottom: 20px;
}}

.card {{
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Medical Diagnosis App</h1>", unsafe_allow_html=True)


# Load the saved models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    selected = option_menu(
        menu_title=None,
        options=["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction", "Lung Cancer Prediction", "Hypo-Thyroid Prediction"],
        icons=["activity", "heart-pulse", "person-walking", "lungs", "capsule"],
        default_index=0,
    )

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    st.write("Enter the following details to predict diabetes:")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
            Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
            BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
            SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
        with col2:
            Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
            BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
            DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
            Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    if st.button('Diabetes Test Result'):
        with st.spinner('Predicting...'):
            time.sleep(2)  # Simulate prediction time
            diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')
    st.write("Enter the following details to predict heart disease:")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = display_input('Age', 'Enter age of the person', 'age', 'number')
            sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
            cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
            trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
            chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
        with col2:
            fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
            restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
            thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
            exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
            oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')

    if st.button('Heart Disease Test Result'):
        with st.spinner('Predicting...'):
            time.sleep(2)  # Simulate prediction time
            heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction")
    st.write("Enter the following details to predict Parkinson's disease:")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
            fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
            flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
            Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
            Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
        with col2:
            RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
            PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
            DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
            Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
            Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')

    if st.button("Parkinson's Test Result"):
        with st.spinner('Predicting...'):
            time.sleep(2)  # Simulate prediction time
            parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB]])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
def validate_input(inputs):
    for key, value in inputs.items():
        if value is None or value == '':
            return False, f"Please enter a valid value for {key}"
    return True, ""

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer Prediction")
    st.write("Enter the following details to predict lung cancer:")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
            AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
            SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
            YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
            ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
            PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
            CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
        with col2:
            FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
            ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
            WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
            ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
            COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
            SHORTNESS_OF_BREATH = display_input('Shortness of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
            SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
            CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    if st.button("Lung Cancer Test Result"):
        inputs = {
            "Gender": GENDER,
            "Age": AGE,
            "Smoking": SMOKING,
            "Yellow Fingers": YELLOW_FINGERS,
            "Anxiety": ANXIETY,
            "Peer Pressure": PEER_PRESSURE,
            "Chronic Disease": CHRONIC_DISEASE,
            "Fatigue": FATIGUE,
            "Allergy": ALLERGY,
            "Wheezing": WHEEZING,
            "Alcohol Consuming": ALCOHOL_CONSUMING,
            "Coughing": COUGHING,
            "Shortness of Breath": SHORTNESS_OF_BREATH,
            "Swallowing Difficulty": SWALLOWING_DIFFICULTY,
            "Chest Pain": CHEST_PAIN
        }
       
        is_valid, error_message = validate_input(inputs)
        if not is_valid:
            st.error(error_message)
        else:
            with st.spinner('Predicting...'):
                time.sleep(2)  # Simulate prediction time
                # Ensure the input order matches the model's training data
                input_data = [
                    GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
                    CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING,
                    COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN
                ]
                lungs_prediction = models['lung_cancer'].predict([input_data])
                lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
                st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid Prediction")
    st.write("Enter the following details to predict hypo-thyroid disease:")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = display_input('Age', 'Enter age of the person', 'age', 'number')
            sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
            on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
            tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
        with col2:
            t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
            t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
            tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

    if st.button("Thyroid Test Result"):
        with st.spinner('Predicting...'):
            time.sleep(2)  # Simulate prediction time
            thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
            thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
            st.success(thyroid_diagnosis)