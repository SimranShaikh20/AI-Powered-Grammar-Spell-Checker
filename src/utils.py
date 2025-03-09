# utils.py - Helper functions for text processing
def load_text(file_path):
    """Loads text from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("File not found.")
        return ""

def save_text(file_path, text):
    """Saves text to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Saved corrected text to {file_path}")
