import streamlit as st
from spellchecker import SpellChecker

st.title('Spell Checker In Python')

# Initialize SpellChecker
spell = SpellChecker()

# Text area for user input
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

if st.button('Check Spelling'):
    if text.strip() == '':
        st.write('Please enter text for checking')
    else:
        try:
            # Split text into words
            words = text.split()
            misspelled = spell.unknown(words)

            if misspelled:
                st.write("**Misspelled Words:**")
                for word in misspelled:
                    st.write(f"- **{word}**: Suggested corrections: {spell.candidates(word)}")
            else:
                st.success("No spelling errors found!")
        except Exception as e:
            st.error(f"An error occurred while checking the text: {e}")