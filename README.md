# 📊 Customer Churn Prediction System

A machine learning-powered Streamlit application that predicts customer churn risk and provides actionable recommendations to improve customer retention.

---

## 🎯 Overview

This application uses a trained classification model to analyze customer data and predict whether a customer is likely to churn (leave the company). It provides:

- **Real-time predictions** with probability scores
- **Visual probability gauge** to understand churn risk
- **Smart recommendations** based on customer profile
- **Interactive user interface** for easy data input

---

## ✨ Features

### Core Functionality
- **Single Customer Prediction** - Predict churn for one customer at a time
- **Interactive Form** - Easy-to-use interface for data input
- **Real-time Analysis** - Instant prediction results with probability scores
- **Visual Dashboard** - Gauge chart showing churn probability
- **Smart Recommendations** - Context-aware suggestions to reduce churn

### User Interface
- Clean, organized layout with 3 columns
- Categorized input sections (Demographics, Services, Billing, Charges)
- Color-coded results (Red for high risk, Green for low risk)
- Interactive Plotly visualizations
- Helpful tooltips for each input field

---

## 📊 Dataset Information

The model is trained on customer data with **19 features**:

### Demographics (4 features)
- `gender` - Customer gender (Male/Female)
- `SeniorCitizen` - Whether customer is a senior citizen (Yes/No)
- `Partner` - Whether customer has a partner (Yes/No)
- `Dependents` - Whether customer has dependents (Yes/No)

### Services (8 features)
- `PhoneService` - Phone service subscription (Yes/No)
- `MultipleLines` - Multiple phone lines (Yes/No)
- `InternetService` - Type of internet service (None/DSL/Fiber optic)
- `OnlineSecurity` - Online security subscription (Yes/No)
- `OnlineBackup` - Online backup subscription (Yes/No)
- `DeviceProtection` - Device protection subscription (Yes/No)
- `TechSupport` - Tech support subscription (Yes/No)
- `StreamingTV` - TV streaming service (Yes/No)
- `StreamingMovies` - Movie streaming service (Yes/No)

### Contract & Billing (5 features)
- `Contract` - Contract type (Month-to-month/One year/Two year)
- `PaperlessBilling` - Paperless billing enabled (Yes/No)
- `PaymentMethod` - Payment method (Electronic check/Mailed check/Bank transfer/Credit card)
- `tenure` - Number of months customer has been with company (0-72)

### Charges (2 features)
- `MonthlyCharges` - Monthly subscription charge ($0-120)
- `TotalCharges` - Total charges to date ($0-10,000)

### Target Variable
- `Churn` - Whether customer churned (Yes/No)

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone or download the project**
   ```bash
   cd your-project-directory
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file is present**
   - Place `customer_churn_model.pkl` in the project directory

5. **Run the application**
   ```bash
   streamlit run churn_app_fixed_final.py
   ```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📖 Usage

### Basic Workflow

1. **Fill in Customer Information**
   - Select or input values for all 19 features
   - Use the organized sections: Demographics, Services, Contract & Billing, Charges
   - Hover over field labels for helpful descriptions

2. **Click "Predict Churn Risk"**
   - The model analyzes the input data
   - Results appear instantly below

3. **Review Results**
   - **Status Box**: Shows if customer is HIGH or LOW churn risk
   - **Probability Score**: Shows exact percentage (0-100%)
   - **Gauge Chart**: Visual representation of churn probability
   - **Recommendations**: Specific actions to reduce churn

### Example Prediction

**Input:**
- Customer: Female, Senior Citizen
- Services: Fiber optic internet, No tech support
- Contract: Month-to-month
- Monthly Charges: $95
- Tenure: 3 months

**Output:**
- ⚠️ **HIGH CHURN RISK** (87.5%)
- Recommendations:
  - Offer long-term contract with incentives
  - Review pricing; consider loyalty discounts
  - Improve onboarding and customer support
  - Encourage tech support subscription

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── churn_app.py                      # Main Streamlit application
├── customer_churn_model.pkl          # Trained ML model (joblib format)
├── customer_churn_model.ipynb        # Trained ML model 
├── Telco-Customer-Churn.csv          # Dataset
├── requirements.txt                  # Python dependencies
├── README.md                          

```

---

## 🤖 Model Details

### Model Type
- **Algorithm**: Random Forest Classification Model
- **Framework**: scikit-learn
- **Format**: Pickle (.pkl) / Joblib

### Input/Output
- **Input**: 19 numeric features (0/1 for categorical, continuous for numerical)
- **Output**: Binary prediction (0 = No Churn, 1 = Churn)
- **Probability**: Confidence score (0.0 - 1.0)

### Feature Requirements
- All features must be numeric
- Categorical features encoded as: 0=No/False, 1=Yes/True
- Ranges respected:
  - Tenure: 0-72 months
  - Monthly Charges: 0-120 USD
  - Total Charges: 0-10,000 USD

### Model Performance
The model provides binary classification predictions with probability estimates, allowing users to see confidence levels for each prediction.

---

## 🔄 How It Works

### 1. Data Input
User enters customer information through interactive forms in three columns.

### 2. Data Conversion
Categorical inputs (Yes/No, Male/Female, etc.) are converted to numeric values:
- Yes/Female/True → 1
- No/Male/False → 0

### 3. Prediction
The trained model receives all 19 features and generates:
- Binary prediction (0 or 1)
- Probability for each class (0.0 - 1.0)

### 4. Visualization
Results displayed with:
- Color-coded status box (red for high risk, green for low)
- Probability percentage
- Plotly gauge chart showing risk level

### 5. Recommendations
Smart rules applied to suggest actions:
```
IF Churn = HIGH RISK:
  IF Contract = Month-to-month → Suggest long-term contract
  IF MonthlyCharges > $80 → Suggest loyalty discount
  IF Tenure < 12 months → Improve onboarding
  IF TechSupport = No → Promote tech support
  IF OnlineSecurity = No & Internet = Yes → Promote security
```

---

## 🛠️ Troubleshooting

### Error: Model file not found
**Solution:**
- Ensure `customer_churn_model.pkl` is in the same directory as the app
- Check file name spelling (case-sensitive on Linux/Mac)

### Error: Prediction fails
**Solution:**
- Verify all input fields are filled
- Check that numeric values are within valid ranges
- Ensure the model file is not corrupted

### App won't start
**Solution:**
1. Check Python version: `python --version` (should be 3.8+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Run validation script: `python validate_setup.py`

### Model loading issues
**Solutions:**
- Try the model recovery tool: `python model_recovery.py`
- Regenerate the model from training script
- Convert between pickle and joblib formats

See `TROUBLESHOOTING.md` for detailed troubleshooting guide.

---

## 📊 Recommendations Logic

The app provides context-aware recommendations based on customer profile:

| Condition | Recommendation |
|-----------|-----------------|
| Month-to-month contract | Offer long-term contract with incentives |
| Monthly charges > $80 | Review pricing; consider loyalty discounts |
| Tenure < 12 months | Improve onboarding and customer support |
| No tech support | Encourage subscription to tech support |
| No security + Has internet | Promote online security add-on |
| Low churn risk | Customer shows strong retention indicators |

---

## 🔐 Data Privacy & Security

- **No data storage**: Customer information is not saved or logged
- **Local processing**: All predictions happen locally on your machine
- **Model safety**: The model only makes predictions, no modification of data

---

## 📈 Performance Metrics

- **Prediction time**: < 100ms per customer
- **Model input**: 19 features
- **Model output**: Binary classification with probability
- **Confidence**: Probability score (0-100%)


---

## 📝 Requirements

All dependencies are listed in `requirements.txt`:

```
streamlit==1.28.1
pandas==2.1.3
numpy==1.24.3
scikit-learn==1.3.2
plotly==5.17.0
joblib==1.3.2
```

To install: `pip install -r requirements.txt`

---

## 📚 Understanding the Model Output

### Probability Interpretation
- **0-33%**: Low churn risk (Green zone)
- **33-66%**: Medium churn risk (Yellow zone)
- **66-100%**: High churn risk (Red zone)

The threshold for "HIGH RISK" classification is set at 50% probability.

---

## 🎓 Use Cases

This application can be used for:

1. **Customer Retention** - Identify at-risk customers proactively
2. **Targeted Interventions** - Focus resources on high-risk segments
3. **Service Planning** - Optimize services based on churn drivers
4. **Pricing Strategy** - Adjust pricing for retention
5. **Customer Support** - Prioritize support for at-risk customers
6. **Business Intelligence** - Understand churn patterns

---

## 💡 Tips for Best Results

1. **Accurate Data**: Ensure all input data is current and accurate
2. **Regular Updates**: Update customer information regularly
3. **Act on Recommendations**: Implement suggested actions promptly
4. **Monitor Trends**: Track prediction changes over time
5. **Validate Results**: Compare predictions with actual outcomes

---

## 📞 Support & Help

1. **Check Documentation**
   - Read README.md for overview
   - Check TROUBLESHOOTING.md for issues
   - Review QUICK_START.md for setup

2. **Validate Setup**
   - Run: `python validate_setup.py`
   - This checks all dependencies and model file

3. **Recover Model**
   - Run: `python model_recovery.py`
   - Choose option 5 for auto-recovery

4. **Review Code Comments**
   - The app code is well-commented
   - Understand the prediction workflow

---

## 📜 License

This project is provided as-is for internal business use.

---

**Made by Priya Gupta for Customer Retention**
