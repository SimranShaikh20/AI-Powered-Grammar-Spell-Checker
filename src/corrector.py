import api_handler

def correct_text(text: str, language: str = "English") -> str:
    """
    Takes user input text and sends it to the LLM API for grammar and spelling correction.
    
    :param text: The raw input text to be corrected.
    :param language: The language of the input text (default is English, supports Hindi).
    :return: Corrected text.
    """
    if not text.strip():
        return "Input text cannot be empty."
    
    response = api_handler.send_request(text, language)
    if response:
        return response
    else:
        return "Error: Could not process the request. Please try again."

if __name__ == "__main__":
    print("Welcome to AI-Powered Grammar & Spell Checker!")
    language = input("Enter language (English/Hindi): ").strip()
    text = input("Enter text to correct: ").strip()
    corrected_text = correct_text(text, language)
    print("\nCorrected Text:")
    print(corrected_text)
