import streamlit as st
from symspellpy import SymSpell, Verbosity

st.title('Spell Checker In Python')

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = "frequency_dictionary_en_82_765.txt"  # Path to the dictionary file
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# Text area for user input
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

if st.button('Check Spelling'):
    if text.strip() == '':
        st.write('Please enter text for checking')
    else:
        try:
            # Check for spelling errors
            suggestions = sym_spell.lookup_compound(text, max_edit_distance=2)
            corrected_text = suggestions[0].term
            st.markdown('**Corrected Sentence - **' + corrected_text)
        except Exception as e:
            st.error(f"An error occurred while checking the text: {e}")