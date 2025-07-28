import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY not found in .env file.")
    exit()

openai.api_key = api_key

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ],
        max_tokens=50
    )

    print("API key is valid!")
    print("Response:", response['choices'][0]['message']['content'])

except Exception as e:
    print("API call failed:")
    print(e)