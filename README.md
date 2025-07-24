# 🧠 Explainable AI Disease Risk Predictor

**Live Demo**: 🌐 [Visit the App](https://explainable-ai-disease-risk-predictor.onrender.com)

This project is a machine learning-powered heart disease risk prediction system built with a focus on **explainability**. It not only predicts the likelihood of heart disease but also provides **SHAP (SHapley Additive exPlanations)** visualizations to make model decisions transparent and trustworthy for users and healthcare professionals.

---

## 🚀 Project Overview

| Feature | Description |
|--------|-------------|
| 💻 **Frontend** | HTML + CSS (Flask-rendered templates) |
| 🔮 **Backend** | Flask (Python web framework) |
| 📊 **Model** | Random Forest Classifier (Best accuracy: **85.33%**) |
| 📈 **Explainability** | SHAP Waterfall plots for feature impact |
| 🌐 **Hosting** | Render (Free tier) |

---

## 🎯 Objectives

- ✅ Predict heart disease risk from user inputs
- ✅ Present model confidence via probabilities
- ✅ Provide actionable health advice
- ✅ Use **Explainable AI (XAI)** to visualize predictions
- ✅ Build a clean, responsive and interactive web interface

---

## 🧪 Model Details

- **Dataset Used**: UCI Heart Disease Dataset
- **Target Variable**: `target` (0 = Healthy, 1 = Heart Disease)
- **Best Model**: `Random Forest Classifier`
- **Evaluation Metrics**:
  - Accuracy: **85.33%**
  - Cross-validation: 5-fold

---

## 🧠 Explainability with SHAP

We used SHAP to understand which features contributed to the prediction. On the result page, users can view a **waterfall plot** that shows the feature-level contribution for that specific prediction.

> Example:
> - 🚹 High cholesterol and low max heart rate increase risk
> - 👟 Exercise-induced angina reduces risk

---

## 💡 How to Use the Live App

1. Go to: 👉 [https://explainable-ai-disease-risk-predictor.onrender.com](https://explainable-ai-disease-risk-predictor.onrender.com)
2. Enter details like age, sex, blood pressure, cholesterol, etc.
3. Click **Check Risk**
4. View:
   - 🧾 Prediction (Low Risk / High Risk)
   - 📊 Model Confidence (Probability)
   - 🧠 SHAP Explanation (Why the model thinks so)
   - 💡 Health Recommendations

---

## 📁 Project Structure

Explainable AI Disease Risk Predictor/
├── app.py

├── shap_utils.py

├── model/

│ ├── best_model.pkl

│ └── scaler.pkl

├── notebook/

│ └── model_development.ipynb

├── templates/

│ ├── index.html

│ └── result.html

├── static/

│ ├── css/

│ │ └── style.css

│ └── images/

├── requirements.txt

└── README.md


---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/yourusername/explainable-ai-disease-risk-predictor.git
cd explainable-ai-disease-risk-predictor

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

🔧 Technologies Used
- Python 3.12
- Flask
- Scikit-learn
- Pandas, NumPy
- SHAP

✨ Author
Pawan Kumar
🎓 Computer Science Student
📍 India

⭐ If you found this helpful, consider giving a star to the repo and sharing it with your peers.
