from textblob import TextBlob
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_tool = language_tool_python.LanguageTool('en-US')  # English language model

    def correct_spell(self, text):
        words = text.split()
        corrected_words = [str(TextBlob(word).correct()) for word in words]
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_tool.check(text)
        found_mistakes = [match.ruleId for match in matches]
        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print("Corrected Spellings:", obj.correct_spell(message))
    print("Grammar Mistakes:", obj.correct_grammar(message))
