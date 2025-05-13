# 📝 AI-Powered Grammar & Spell Checker

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00BFFF?style=for-the-badge&logo=groq&logoColor=white)


### 📖 Check out my blog: [Click Here ](https://medium.com/@msusimran20/ai-powered-grammar-spell-checker-c9fb4d33975f)

## 🚀 Try It Out  
🔗 **Live Demo:** [Click Here](https://ai-powered-grammar-spell-checker-hyndfylzmob5tn4wffyjap.streamlit.app/)


## 🚀 Overview
This project is an AI-powered grammar and spell checker that utilizes **Groq's LLM (Large Language Model)** to correct spelling, grammar, and context errors in both **English and Hindi**. The application is built using **Streamlit** for an interactive user experience.

---
## ✨ Features
- ✅ Supports **English** and **Hindi**
- 🔍 AI-driven **Grammar & Spell Correction**
- 🎨 **User-friendly UI** with a dark theme
- ⚡ **Instant Results** with a single click
- 🏠 Built with **Streamlit** for easy deployment

---
## 🌟 Why **Mixtral-8x7b-32768**?
This project uses **Groq's Mixtral-8x7b-32768** model, an advanced mixture of experts model that balances **speed, accuracy, and efficiency**. It was chosen because:
- ✅ **High Accuracy:** It effectively detects and corrects grammatical errors while preserving context.
- ⚡ **Optimized Performance:** Provides quick responses, making it ideal for real-time applications.
- 💡 **Better Context Understanding:** Unlike smaller models, Mixtral-8x7b-32768 excels at maintaining sentence coherence and nuance.
- 📚 **Scalability:** Can handle complex and lengthy text inputs efficiently.

---
## 🌍 How This Project Works
1. The user enters text that needs correction.
2. The app sends the text to **Groq's LLM API**, which processes the input using advanced language models.
3. The LLM analyzes the text for grammar, spelling, and contextual errors.
4. The corrected text is then returned and displayed to the user.

### 🧠 How LLM Works in This Project
- **Text Input:** User provides raw text in English or Hindi.
- **System Prompt:** The LLM is instructed to act as a grammar and spell checker.
- **Processing:** The model detects errors and improves sentence structure while keeping the original meaning intact.
- **Output:** A refined and corrected version of the input is returned.

---
## 📝 System Prompt Used
The model is instructed with a carefully designed **system prompt** to ensure accurate and context-aware corrections. The prompts used are:

### **English Prompt**
```plaintext
You are a highly advanced grammar and spell checker for English. Correct the following text while maintaining its meaning. Ensure proper grammar, sentence structure, and context-aware spelling corrections.
```

### **Hindi Prompt**
```plaintext
आप एक उच्च स्तरीय व्याकरण और वर्तनी सुधारक हैं, जो हिंदी भाषा के लिए बनाया गया है। दिए गए पाठ को सही करें, व्याकरण, वाक्य संरचना और संदर्भ के अनुसार वर्तनी को ठीक करें, जबकि मूल अर्थ को बनाए रखें।
```

### 🔄 Why These Prompts Are Used
- ✅ **Ensures Precision:** The prompts explicitly ask the LLM to focus on correcting grammar and spelling while maintaining context.
- 🌐 **Supports Multiple Languages:** The `{language}` placeholder allows dynamic adaptation for English and Hindi.
- 💠 **Preserves Meaning:** The instruction ensures that the original intent of the text remains intact.
- 🎯 **Optimized for LLM Processing:** It minimizes ambiguity, making the model’s responses more predictable and reliable.

---
## 🛠️ Installation
### 🔹 Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 🔹 Setup
```bash
# Clone this repository
git clone https://github.com/SimranShaikh20/grammar-checker.git
cd grammar-checker

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---
## 🌌 API Integration
This project uses **Groq LLM API** for text correction. 

### 🔹 API Endpoint
```plaintext
POST https://api.groq.com/openai/v1/chat/completions
```

### 🔹 Example API Request
```python
import requests

API_KEY = "your_groq_api_key"
text_to_correct = "Thiss is an exemple of baad grammr."
language = "English"

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

payload = {
    "model": "mixtral-8x7b-32768",
    "messages": [
        {"role": "system", "content": f"You are a highly advanced grammar and spell checker for {language}. Correct the following text while maintaining its meaning."},
        {"role": "user", "content": f"Correct this text: {text_to_correct}"}
    ],
    "temperature": 0.2,
    "max_tokens": 500
}

response = requests.post(url, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

---
## 🎨 UI Customization
This project includes **custom CSS styling** for a modern UI:
- 🌑 **Dark mode** background
- 🌟 **Multicolored gradient buttons**
- 🌍 **Styled text inputs** with improved readability
- 🛠️ **Custom sidebar** with a sleek layout

---
## 🔮 Future Enhancements
- 🚃 **Voice Input Support**
- 📚 **Multi-language Support** (Spanish, French, etc.)
- 🖊 **Auto-correction while typing**
- 🌐 **Deploy as a Web App**

---


## 🔄 Workflow

```mermaid
sequenceDiagram
    participant User
    participant Streamlit
    participant GroqAPI
    participant MixtralLLM
    
    User->>Streamlit: Enters text + selects language
    Streamlit->>GroqAPI: Sends correction request
    GroqAPI->>MixtralLLM: Processes with system prompt
    MixtralLLM->>GroqAPI: Returns corrected text
    GroqAPI->>Streamlit: Receives response
    Streamlit->>User: Displays corrected text

```

## 🐟 License
This project is licensed under the **MIT License**.

---
## 🎯 Author
**Simran Shaikh**

🚀 Made with ❤️ by **Simran** 