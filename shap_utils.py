import shap
import matplotlib.pyplot as plt
import uuid
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_shap_plot(model, scaled_input, feature_names, predicted_class, output_dir="static/images"):
    print("SHAP: Starting explanation generation...")

    try:
        explainer = shap.Explainer(model)
        shap_values = explainer(scaled_input)
        print("SHAP values computed")

        sample_index = 0

        if len(shap_values.values.shape) == 3:
            class_index = list(model.classes_).index(predicted_class)
            single_expl = shap_values[sample_index, :, class_index]
        else:
            single_expl = shap_values[sample_index]

        print("Extracted correct SHAP values shape")

        plot_id = str(uuid.uuid4())[:8]
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        shap_path = os.path.join(output_dir, f"shap_{plot_id}.png")

        plt.figure()
        shap.plots.waterfall(single_expl, show=False)
        plt.savefig(shap_path, bbox_inches="tight")
        plt.close()
        print(f"SHAP plot saved to: {shap_path}")

        shap_vals = single_expl.values
        sorted_features = sorted(zip(feature_names, shap_vals), key=lambda x: abs(x[1]), reverse=True)[:5]

        prompt = "Explain the following model prediction to a user in simple language:\n"
        for feat, val in sorted_features:
            impact = "increased" if val > 0 else "decreased"
            prompt += f"- {feat} {impact} the risk of heart disease.\n"

        fallback = [f"{f} {'increased' if v > 0 else 'decreased'} the model's prediction." for f, v in sorted_features]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant who explains machine learning decisions in plain English to users."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.6,
                max_tokens=150
            )
            gpt_summary = response.choices[0].message.content.strip()
            print("🧠 AI-generated explanation successful")
            return shap_path, [gpt_summary]

        except Exception as e:
            print(f"OpenAI API call failed: {e}")
            fallback.append("Could not generate natural language explanation due to a technical issue.")
            return shap_path, fallback

    except Exception as err:
        print(f"SHAP processing error: {err}")
        return None, [f"(SHAP explanation failed: {err})"]
