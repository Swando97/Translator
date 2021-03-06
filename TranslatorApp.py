from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

sentence = [ "Dear Yuliia, I am very sorry. It was never my intention to hurt you. I must apologize.",
"Looking back I want to own up to my mistakes. I was lost. I was looking outward for answers; not inward.",
"I didn't feel motivated. Having no schedule made me feel like I had no purpose.",
"I felt more disabled than ever before. I wanted to move forward but I felt frozen."]

# translate a spanish text to english text (by default)
translations = translator.translate(sentence, dest="uk")

for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

