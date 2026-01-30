import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        font-size: 20px;
        font-weight: bold;
    }
    .churn-risk {
        background-color: #ffcccc;
        color: #8b0000;
    }
    .no-churn-risk {
        background-color: #ccffcc;
        color: #006600;
    }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        with open('customer_churn_model.pkl', 'rb') as f:
            return joblib.load(f)
    except FileNotFoundError:
        st.error("❌ Model file 'customer_churn_model.pkl' not found.")
        st.stop()

model = load_model()

# Feature descriptions
FEATURE_DESCRIPTIONS = {
    'gender': 'Customer gender',
    'SeniorCitizen': 'Whether customer is a senior citizen',
    'Partner': 'Whether customer has a partner',
    'Dependents': 'Whether customer has dependents',
    'tenure': 'Number of months customer has been with company',
    'PhoneService': 'Whether customer has phone service',
    'MultipleLines': 'Whether customer has multiple lines',
    'InternetService': 'Type of internet service',
    'OnlineSecurity': 'Whether customer has online security',
    'OnlineBackup': 'Whether customer has online backup',
    'DeviceProtection': 'Whether customer has device protection',
    'TechSupport': 'Whether customer has tech support',
    'StreamingTV': 'Whether customer has TV streaming',
    'StreamingMovies': 'Whether customer has movie streaming',
    'Contract': 'Contract type',
    'PaperlessBilling': 'Whether customer uses paperless billing',
    'PaymentMethod': 'Payment method',
    'MonthlyCharges': 'Monthly charges in dollars',
    'TotalCharges': 'Total charges in dollars'
}

# Main title
st.title("📊 Customer Churn Prediction System")
st.markdown("---")

st.header("Single Customer Prediction")

col1, col2, col3 = st.columns(3)

input_data = {}

# Column 1: Demographics
with col1:
    st.subheader("Demographics")
    input_data['gender'] = st.selectbox("Gender", ['Male', 'Female'], help=FEATURE_DESCRIPTIONS['gender'])
    input_data['SeniorCitizen'] = st.selectbox("Senior Citizen", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['SeniorCitizen'])
    input_data['Partner'] = st.selectbox("Has Partner", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['Partner'])
    input_data['Dependents'] = st.selectbox("Has Dependents", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['Dependents'])

# Column 2: Services
with col2:
    st.subheader("Services")
    input_data['PhoneService'] = st.selectbox("Phone Service", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['PhoneService'])
    input_data['MultipleLines'] = st.selectbox("Multiple Lines", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['MultipleLines'])
    input_data['InternetService'] = st.selectbox("Internet Service", ['None', 'DSL', 'Fiber optic'], help=FEATURE_DESCRIPTIONS['InternetService'])
    input_data['OnlineSecurity'] = st.selectbox("Online Security", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['OnlineSecurity'])
    input_data['OnlineBackup'] = st.selectbox("Online Backup", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['OnlineBackup'])

# Column 3: Additional Options
with col3:
    st.subheader("Additional Options")
    input_data['DeviceProtection'] = st.selectbox("Device Protection", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['DeviceProtection'])
    input_data['TechSupport'] = st.selectbox("Tech Support", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['TechSupport'])
    input_data['StreamingTV'] = st.selectbox("TV Streaming", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['StreamingTV'])
    input_data['StreamingMovies'] = st.selectbox("Movie Streaming", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['StreamingMovies'])

# Contract and billing
st.subheader("Contract & Billing")
col4, col5, col6, col7 = st.columns(4)

with col4:
    input_data['Contract'] = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'], help=FEATURE_DESCRIPTIONS['Contract'])

with col5:
    input_data['PaperlessBilling'] = st.selectbox("Paperless Billing", ['No', 'Yes'], help=FEATURE_DESCRIPTIONS['PaperlessBilling'])

with col6:
    input_data['PaymentMethod'] = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], help=FEATURE_DESCRIPTIONS['PaymentMethod'])

with col7:
    input_data['tenure'] = st.slider("Tenure (months)", 0, 72, 12, help=FEATURE_DESCRIPTIONS['tenure'])

# Numerical features
st.subheader("Charges")
col8, col9 = st.columns(2)

with col8:
    input_data['MonthlyCharges'] = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=120.0, value=65.0, step=0.5, help=FEATURE_DESCRIPTIONS['MonthlyCharges'])

with col9:
    input_data['TotalCharges'] = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0, step=10.0, help=FEATURE_DESCRIPTIONS['TotalCharges'])

# Convert inputs to model format
if st.button("🔮 Predict Churn Risk", type="primary", use_container_width=True):
    # Convert categorical to numerical
    converted_data = {
        'gender': 1 if input_data['gender'] == 'Female' else 0,
        'SeniorCitizen': 1 if input_data['SeniorCitizen'] == 'Yes' else 0,
        'Partner': 1 if input_data['Partner'] == 'Yes' else 0,
        'Dependents': 1 if input_data['Dependents'] == 'Yes' else 0,
        'tenure': input_data['tenure'],
        'PhoneService': 1 if input_data['PhoneService'] == 'Yes' else 0,
        'MultipleLines': 1 if input_data['MultipleLines'] == 'Yes' else 0,
        'InternetService': ['None', 'DSL', 'Fiber optic'].index(input_data['InternetService']),
        'OnlineSecurity': 1 if input_data['OnlineSecurity'] == 'Yes' else 0,
        'OnlineBackup': 1 if input_data['OnlineBackup'] == 'Yes' else 0,
        'DeviceProtection': 1 if input_data['DeviceProtection'] == 'Yes' else 0,
        'TechSupport': 1 if input_data['TechSupport'] == 'Yes' else 0,
        'StreamingTV': 1 if input_data['StreamingTV'] == 'Yes' else 0,
        'StreamingMovies': 1 if input_data['StreamingMovies'] == 'Yes' else 0,
        'Contract': ['Month-to-month', 'One year', 'Two year'].index(input_data['Contract']),
        'PaperlessBilling': 1 if input_data['PaperlessBilling'] == 'Yes' else 0,
        'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'].index(input_data['PaymentMethod']),
        'MonthlyCharges': input_data['MonthlyCharges'],
        'TotalCharges': input_data['TotalCharges']
    }
    
    # Prepare features
    X = pd.DataFrame([converted_data])
    
    try:
        # Make prediction
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]
        
        # Display results
        st.markdown("---")
        st.subheader("🎯 Prediction Results")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            if prediction == 1:
                st.markdown(f"<div class='prediction-box churn-risk'>⚠️ HIGH CHURN RISK<br/>Probability: {probability[1]*100:.2f}%</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='prediction-box no-churn-risk'>✅ LOW CHURN RISK<br/>Probability: {probability[0]*100:.2f}%</div>", unsafe_allow_html=True)
        
        with col_res2:
            # Probability gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=probability[1]*100,
                title={'text': "Churn Probability (%)"},
                delta={'reference': 50},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 33], 'color': "lightgreen"},
                        {'range': [33, 66], 'color': "lightyellow"},
                        {'range': [66, 100], 'color': "lightcoral"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 70
                    }
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        st.subheader("💡 Recommendations")
        recommendations = []
        
        if prediction == 1:
            if input_data['Contract'] == 'Month-to-month':
                recommendations.append("🔗 Consider offering a long-term contract with incentives")
            if input_data['MonthlyCharges'] > 80:
                recommendations.append("💰 Review pricing; consider loyalty discounts")
            if input_data['tenure'] < 12:
                recommendations.append("🎯 Improve onboarding and customer support")
            if input_data['TechSupport'] == 'No':
                recommendations.append("🛠️ Encourage subscription to Tech Support services")
            if input_data['OnlineSecurity'] == 'No' and input_data['InternetService'] != 'None':
                recommendations.append("🔒 Promote Online Security add-on")
        
        if not recommendations:
            recommendations.append("✨ Customer shows strong retention indicators")
        
        for rec in recommendations:
            st.write(rec)
    
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Made by Priya Gupta (using Scikit-learn and sStreamlit</div>", unsafe_allow_html=True)