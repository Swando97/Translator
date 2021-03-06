from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

sentence = ["Dear friends and family, I am very sorry. It was never my intention to hurt you. I must apologize.",
"I want to own up to my mistakes. I was lost. I was looking outward for answers; not inward.",
"I wasn't motivated. Having no schedule made me feel like I had no purpose. I was fighting my pain with substances.",
"I felt more disabled than ever before. I wanted to move forward but I felt frozen. This was my fault, not yours.",
"Now I have started to develop myself, with your help! I have a daily schedule. I can see myself working towards something.",
"I'm excited for the future, I hope you are too. I think about you everyday. I miss you. I miss your smile.",
"When you came home from work, our dark apartment started to shine. I was blinded and foolish.",
"I wish I realized this when it mattered most. I cannot turn back the hands of time.",
"I can look back and learn from my mistakes. "]

# translate a spanish text to english text (by default)
translations = translator.translate(sentence, dest="uk")

for translation in translations:
    print(f"{translation.text}")

