import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

st.title("Context-Aware Spell Checker (English)")

# Load pre-trained T5 model
model_name = "vennify/t5-base-grammar-correction"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Text area for user input
text = st.text_area("Enter Text:", value='', height=150)

if st.button("Check Spelling"):
    if text.strip() == '':
        st.warning("Please enter text for checking")
    else:
        with st.spinner("Processing..."):
            try:
                input_text = f"fix: {text}"
                input_ids = tokenizer.encode(input_text, return_tensors="pt")

                # Generate corrected text
                output_ids = model.generate(input_ids, max_length=200)
                corrected_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

                st.success("Correction Complete!")
                st.markdown(f"**Corrected Sentence:** {corrected_text}")

            except Exception as e:
                st.error(f"Error occurred: {e}")

