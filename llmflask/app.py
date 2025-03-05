from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Groq API Key (Replace with your actual key)
API_KEY = "your_groq_api_key_here"

# Function to correct text using Groq API
def correct_text(text, language):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Define the prompt based on language selection
    system_prompt = f"You are a highly advanced grammar and spell checker for {language}. " \
                    "Correct the following text while maintaining its meaning. " \
                    "Ensure proper grammar, sentence structure, and context-aware spelling corrections."

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Correct this text: {text}"}
        ],
        "temperature": 0.2,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"📌 Error: {response.json()}"

# Home Route
@app.route("/", methods=["GET", "POST"])
def home():
    corrected_text = None
    error_message = None
    selected_language = "English"

    if request.method == "POST":
        user_input = request.form.get("text_input", "").strip()
        selected_language = request.form.get("language", "English")

        if user_input:
            corrected_text = correct_text(user_input, selected_language)
        else:
            error_message = "⚠️ Please enter some text for correction."

    return render_template("index.html", corrected_text=corrected_text, error_message=error_message, selected_language=selected_language)

if __name__ == "__main__":
    app.run(debug=True)
