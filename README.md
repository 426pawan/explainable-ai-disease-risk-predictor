# 🧠 Explainable AI Disease Risk Predictor

**Live Demo**: 🌐 [Visit the App](https://explainable-ai-disease-risk-predictor.onrender.com)

This project is a machine learning-powered heart disease risk prediction system built with a focus on **explainability**. It not only predicts the likelihood of heart disease but also provides **SHAP (SHapley Additive exPlanations)** visualizations to make model decisions transparent and trustworthy for users and healthcare professionals.

---

## 🚀 Project Overview

| Feature         | Description                                      |
|----------------|--------------------------------------------------|
| 💻 **Frontend** | HTML, CSS, JavaScript (Flask-rendered templates) |
| 🔮 **Backend**  | Flask (Python Web Framework)                     |
| 🤖 **Model**    | Random Forest Classifier (Accuracy: **85.33%**) |
| 🧠 **XAI**      | SHAP Waterfall plots (Local feature explanations) |
| 🚨 **AI Chat**  | GPT-3.5 powered explanation assistant (OpenAI API) |
| 🌐 **Hosting**  | Render (Free Tier)                               |

---

## 🎯 Key Objectives

- ✅ Predict heart disease risk from user inputs
- ✅ Present model confidence with probabilities
- ✅ Offer actionable health recommendations
- ✅ Use **Explainable AI (XAI)** to explain each prediction
- ✅ Include an AI chatbot for natural-language Q&A (optional)
- ✅ Build a clean, responsive, interactive UI

---

## 📊 Model Details

- **Dataset**: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Target Variable**: `target` (0 = Healthy, 1 = Heart Disease)
- **Best Model**: Random Forest Classifier
- **Evaluation Metrics**:
  - Accuracy: **85.33%**
  - Cross-validation: 5-fold

---

## 🧠 Explainability with SHAP

We use SHAP to make individual predictions **interpretable**:

- A **SHAP Waterfall Plot** is generated for every prediction.
- Users can see how features like `age`, `chol`, `thalach`, `cp`, etc. influenced the model.
- Top 5 features are summarized in simple language using GPT.

> Example:
> - 😹 `cp` and `chol` increased the risk
> - 👟 `exang` reduced the risk

---

## 🛸️ AI-Powered Explanation (Optional)

- Uses **OpenAI GPT-3.5** to convert SHAP outputs into **human-friendly explanations**.
- Provides a **fallback explanation** when OpenAI is unavailable or quota is exceeded.
- A future enhancement includes a **chatbox assistant** on the result page to answer health-related questions interactively.

---

## 💡 How to Use the App

1. Visit 👉 [Live App](https://explainable-ai-disease-risk-predictor.onrender.com)
2. Fill out fields like age, sex, BP, cholesterol, etc.
3. Click **Check Risk**
4. See:
   - ✅ Prediction (High/Low Risk)
   - 📈 Confidence level (Probability)
   - 🧠 SHAP visual explanation
   - 💬 AI-generated feature summary
   - 🦥 Health Recommendations

---

## 📁 Project Structure

```
Explainable AI Disease Risk Predictor/
├── app.py
├── shap_utils.py
├── testapikey.py
├── model/
│   ├── best_model.pkl
│   └── scaler.pkl
├── notebook/
│   └── model_development.ipynb
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── resStyle.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── requirements.txt
└── README.md
```

---

## 💻 Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/explainable-ai-disease-risk-predictor.git
cd explainable-ai-disease-risk-predictor

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up OpenAI key
# Create a `.env` file and add:
# OPENAI_API_KEY=your-key-here

# Run the app
python app.py
```

---

## 🛠️ Technologies Used

- Python 3.12
- Flask
- Scikit-learn
- Pandas & NumPy
- SHAP (Explainability)
- OpenAI GPT-3.5 (for user-friendly explanations)
- HTML5 + CSS3 + JS

---

## 👨‍💻 Author

**Pawan Kumar**  
🎓 Computer Science Student  
📍 India

---

## ⭐ Feedback & Contributions

- Found this useful? 🌟 Give it a star!
- Have suggestions or want to contribute? Feel free to open a PR or issue.
