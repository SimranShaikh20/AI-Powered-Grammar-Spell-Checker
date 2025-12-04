import requests

def get_correction(text, language="English"):
    API_KEY = "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"
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": f"You are a grammar and spell checker for {language}."},
            {"role": "user", "content": text}
        ],
        "max_tokens": 300,
        "temperature": 0.2
    }
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("ERROR:", response.text)  # helpful debugging
        return None

    data = response.json()
    return data["choices"][0]["message"]["content"]
