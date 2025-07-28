from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import os
from dotenv import load_dotenv
import openai
from shap_utils import generate_shap_plot

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

model = joblib.load('model/best_model.pkl')
scaler = joblib.load('model/scaler.pkl')

def generate_natural_language_explanation(shap_explanations):
    try:
        prompt = (
            "Explain the following SHAP feature contributions for a heart disease prediction "
            "in a user-friendly way:\n\n" + "\n".join(shap_explanations) +
            "\n\nMake the explanation easy to understand for a non-technical user."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Could not generate natural language explanation: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        keys = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        form_data = [int(request.form[k]) if k != 'oldpeak' else float(request.form[k]) for k in keys]
        input_df = pd.DataFrame([form_data], columns=keys)
        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]
        try:
            probability = model.predict_proba(scaled_input)[0]
            class_index = list(model.classes_).index(prediction)
            prob = round(probability[class_index] * 100, 2)
        except Exception:
            prob = "Unavailable"

        try:
            shap_plot_path, shap_explanations = generate_shap_plot(model, scaled_input, input_df.columns, prediction)
            natural_explanation = generate_natural_language_explanation(shap_explanations)
            shap_path_for_html = shap_plot_path.replace("\\", "/").split("static/")[-1]
        except Exception as shap_err:
            shap_path_for_html = None
            shap_explanations = [f"Could not generate SHAP explanation: {shap_err}"]
            natural_explanation = None

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

        return render_template(
            'result.html',
            prediction=prediction,
            prob=prob,
            result_msg=result_msg,
            tips=tips,
            shap_plot=shap_path_for_html,
            shap_explanations=shap_explanations,
            natural_explanation=natural_explanation
        )

    except Exception as e:
        return f"Error occurred: {str(e)}", 400




from flask import jsonify

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")
        if not user_message:
            return jsonify({"reply": "Please enter a message."})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant knowledgeable in heart health and medical AI predictions."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=200,
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Could not respond: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)