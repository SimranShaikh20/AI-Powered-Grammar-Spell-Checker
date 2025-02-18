import streamlit as st
from symspellpy.symspellpy import SymSpell, Verbosity

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Add Hindi words to SymSpell dictionary (Expand for better accuracy)
hindi_words = [
    'भारत', 'में', 'अच्छा', 'लगता', 'है', 'यहां', 'संस्कृति', 'बहुत', 'समृद्ध', 
    'मैं', 'रोज', 'स्कूल', 'जाता', 'हूं', 'अध्ययन', 'करता', 'खुशी', 'हुई', 
    'आशा', 'करता', 'हूं', 'हम', 'फिर', 'से', 'मिलें'
]
for word in hindi_words:
    sym_spell.create_dictionary_entry(word, 1)

# Dictionary for rule-based grammar corrections
common_corrections = {
    "अच्छा लगता हूं": "अच्छा लगता है",
    "यहां है संस्कृति हूं समृद्ध है": "यहां की संस्कृति बहुत समृद्ध है",
    "फिर अध्ययन करता हूं से मिलें खुशी हूं": "और अध्ययन करता हूं। आपसे मिलकर खुशी हुई",
    "खुशी हूं": "खुशी हुई",
    "हुयी": "हुई",
    "हे": "है",
    "बहोत": "बहुत",
    "संस्क्रती": "संस्कृति",
    "फिरसे": "फिर से",
    "हु": "हूं",
    "अचछा": "अच्छा",
    "यहा": "यहां",
    "आपका मिलकर": "आपसे मिलकर",
    "हम फिर से मिले": "हम फिर से मिलें"
}


# Function to correct text
def correct_text(input_text):
    # Step 1: Apply manual corrections first
    for incorrect, correct in common_corrections.items():
        input_text = input_text.replace(incorrect, correct)

    # Step 2: Apply spelling correction word by word
    input_tokens = input_text.split()
    corrected_tokens = []
    
    for token in input_tokens:
        suggestions = sym_spell.lookup(token, Verbosity.CLOSEST, max_edit_distance=2)
        corrected_tokens.append(suggestions[0].term if suggestions else token)
    
    return " ".join(corrected_tokens)

# Streamlit UI
st.title("🔠 Hindi Spell & Grammar Checker")
st.write("Enter Hindi text below and get the corrected version in real-time.")

# User input
input_text = st.text_area("✍️ Enter Hindi Text:", height=150)

if st.button("🔍 Correct Spelling & Grammar"):
    if input_text.strip():
        corrected_text = correct_text(input_text)
        st.success("✅ Corrected Text:")
        st.write(corrected_text)
    else:
        st.warning("⚠️ Please enter some text.")

# Run with: streamlit run app.py
