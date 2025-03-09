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
    
    /* Increase width of text areas */
    .stTextArea textarea {
        width: 90% !important;
        height: 200px !important;
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
    [data-testid="stSidebar"] {
        background-color: #2b2b2b !important;
        padding: 20px;
        border-radius: 10px;
    }
    [data-testid="stSidebar"] h1, h2, h3 {
        color: white !important;
    }

    /* Footer Styling */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: white;
        font-size: 14px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Groq API Key (Replace with your actual key)
API_KEY = "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"

# Function to Correct Text using Groq API
def correct_text(text, language):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Hindi correction without translation
    if language == "Hindi":
        system_prompt = (
            "आप एक अत्याधुनिक हिंदी व्याकरण और वर्तनी सुधारक हैं। "
            "कृपया दिए गए हिंदी पाठ को सही करें लेकिन उसका अनुवाद न करें। "
            "केवल व्याकरण, वाक्य संरचना और वर्तनी की त्रुटियों को ठीक करें, अर्थ को वैसा ही रखें।"
        )
        user_prompt = f"सुधार करें (अनुवाद न करें): {text}"
    else:
        system_prompt = "You are an advanced English grammar and spell checker. Correct the text while maintaining its meaning."
        user_prompt = f"Correct this English text: {text}"

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        corrected_output = response.json()
        return corrected_output["choices"][0]["message"]["content"]
    else:
        return f"📌 Error: {response.json()}"

# Sidebar Navigation
st.sidebar.title("🔍 Select Language")
selected_option = st.sidebar.radio("Choose:", ["English Grammar Check", "Hindi Grammar Check"])

# Display only the selected language's correction
if selected_option == "English Grammar Check":
    st.title("📝 AI-Powered **English** Grammar & Spell Checker")
    language = "English"
    st.subheader("🔹 Correct spelling, grammar, and context errors instantly! ✨")
    user_input = st.text_area("✍️ Enter your English text:", height=200, placeholder="Type or paste your text here...")

elif selected_option == "Hindi Grammar Check":
    st.title("📝 AI-Powered **Hindi** Grammar & Spell Checker")
    language = "Hindi"
    st.subheader("🔹 हिंदी व्याकरण और वर्तनी की त्रुटियों को सही करें! ✨")
    user_input = st.text_area("✍️ अपना हिंदी पाठ यहाँ दर्ज करें:", height=200, placeholder="अपना पाठ यहाँ टाइप करें...")

if st.button("✅ Check & Correct"):
    if user_input.strip() == "":
        st.warning("⚠️ Input Text cannot be empty! Please enter some text to correct.")
    else:
        with st.spinner("🔍 Ruuning..."):
            corrected_text = correct_text(user_input, language)
            st.success("✔️ Corrected text is here ")
            
            st.text_area("✅ Correct text:", corrected_text, height=200)

# Footer
st.markdown('<div style="text-align: center; color: white;"> Made with ❤️ by Simran</div>', unsafe_allow_html=True)
