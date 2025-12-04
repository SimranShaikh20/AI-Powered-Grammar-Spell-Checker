# api_handler.py - Handles interaction with LLM API
import requests

def get_correction(text, language="English"):
    """Sends text to LLM API and returns corrected output."""
    API_KEY = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": f"You are a highly advanced grammar and spell checker for {language}. Correct the following text while maintaining its meaning."},
            {"role": "user", "content": f"Correct this text: {text}"}
        ],
        "temperature": 0.2,
        "max_tokens": 500
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
