from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)

model = joblib.load('model/best_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        if not (1 <= age <= 120): raise ValueError("Invalid age")

        sex = int(request.form['sex'])
        if sex not in [0, 1]: raise ValueError("Invalid sex")

        cp = int(request.form['cp'])
        if cp not in [0, 1, 2, 3]: raise ValueError("Invalid chest pain type")

        trestbps = int(request.form['trestbps'])
        if not (80 <= trestbps <= 250): raise ValueError("Invalid blood pressure")

        chol = int(request.form['chol'])
        if not (100 <= chol <= 600): raise ValueError("Invalid cholesterol")

        fbs = int(request.form['fbs'])
        if fbs not in [0, 1]: raise ValueError("Invalid fasting blood sugar")

        restecg = int(request.form['restecg'])
        if restecg not in [0, 1]: raise ValueError("Invalid ECG")

        thalch = int(request.form['thalch'])
        if not (60 <= thalch <= 250): raise ValueError("Invalid max heart rate")

        exang = int(request.form['exang'])
        if exang not in [0, 1]: raise ValueError("Invalid angina")

        oldpeak = float(request.form['oldpeak'])
        if not (0 <= oldpeak <= 6): raise ValueError("Invalid ST depression")

        slope = int(request.form['slope'])
        if slope not in [0, 1, 2]: raise ValueError("Invalid slope")

        ca = int(request.form['ca'])
        if not (0 <= ca <= 3): raise ValueError("Invalid number of vessels")

        thal = int(request.form['thal'])
        if thal not in [1, 2, 3]: raise ValueError("Invalid thalassemia type")

        input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs,
                                    restecg, thalch, exang, oldpeak, slope, ca, thal]],
                                  columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                                           'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)[0]
        probability = model.predict_proba(scaled_input)[0]

        if prediction == 1:
            result_msg = "⚠️ You may be at risk of heart disease."
            tips = (
                "💡 Recommendation: Please consult a cardiologist and begin a heart-healthy routine: "
                "exercise regularly, follow a balanced diet, quit smoking, and manage stress. "
                "🔗 <a href='https://www.cdc.gov/heartdisease/prevention.htm' target='_blank'>Learn more</a>"
            )
        else:
            result_msg = "✅ You are likely healthy with no sign of heart disease."
            tips = (
                "💡 Keep up your healthy habits: regular physical activity, nutritious food, and routine check-ups. "
                "🔗 <a href='https://www.heart.org/en/healthy-living' target='_blank'>Learn more</a>"
            )

        return render_template('result.html',
                               prediction=prediction,
                               prob=round(probability[prediction] * 100, 2),
                               result_msg=result_msg,
                               tips=tips)

    except Exception as e:
        return f"Error occurred: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)