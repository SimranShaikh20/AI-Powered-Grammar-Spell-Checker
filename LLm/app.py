import streamlit as st
import requests

# Custom CSS for Styling
st.markdown("""
    <style>
    /* Set Black Background */
    .stApp {
        background-color: black;
    }
    
    /* Make Title and Subtitle Text Brighter */
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
    }
    
    /* Text Input Label Color */
    label[data-testid="stTextAreaLabel"] {
        color: #ffcc00 !important;
        font-size: 16px;
        font-weight: bold;
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        background-color: #fff;
        color: black;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }

    /* Multicolored Gradient Button */
    .stButton>button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b, #ff8c00, #ff416c);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.07);
        box-shadow: 0px 0px 10px rgba(255, 165, 0, 0.8);
    }

    /* Sidebar Styling */
    .stSidebar {
        background-color: black !important;
    }

    /* Increase spacing between options */
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 20px !important;
    }

    /* Footer Styling */
    .stMarkdown p {
        color: white;
        font-size: 14px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

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

# Sidebar Navigation with spacing
st.sidebar.title("🔍 Select Language")

# Spacing before first option
st.sidebar.markdown("<br>", unsafe_allow_html=True)

selected_option = st.sidebar.radio(
    "",  # No title to avoid clutter
    ["English Grammar Check", "Hindi Grammar Check"],
)

# Spacing after selection
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

# Title based on selection
if selected_option == "English Grammar Check":
    st.title("📝 AI-Powered **English** Grammar & Spell Checker")
    language = "English"
else:
    st.title("📝 AI-Powered **Hindi** Grammar & Spell Checker")
    language = "Hindi"

st.subheader("🔹 Correct spelling, grammar, and context errors instantly!")

# Text input area
user_input = st.text_area(f"✍️ Enter your {language} text:", height=200, placeholder="Type or paste your text here...")

# Multicolored button
if st.button("✅ Check & Correct"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text for correction.")
    else:
        with st.spinner("🔍 Checking and correcting..."):
            corrected_text = correct_text(user_input, language)
            st.success("✔️ Correction Complete!")
            st.markdown("### ✅ **Corrected Text:**")
            st.markdown(f"📌 {corrected_text}")

# Footer
st.markdown("---")
st.markdown("⚡ **Powered by Groq LLMs** | Made with ❤️ by Simran")
API_KEY = "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"