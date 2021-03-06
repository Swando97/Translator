from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

sentence = ["Dear friends and family, I am very sorry. It was never my intention to hurt anyone. Myself included.",
"I must apologize. I want to own up to my mistakes. I was lost. I was looking outward for answers; not inward.",
"I wasn't motivated. Having no schedule made me feel like I had no purpose. I was fighting my pain with substances.",
"I felt more disabled than ever before. I wanted to move forward but I felt frozen. This was my fault, not yours.",
"Now I have started to develop myself. I have a daily schedule. I see myself working towards my goals.",
"I'm excited for the future, I hope you are too. I think about you people everyday and I cannot turn back the hands of time.",
"I can however look back and learn from my mistakes. I realize couldn't have done this without your help and support.",
"I will never be able to repay you guys for the things you did. I want to try. I want to start by saying I love you. Thank you."]

# translate a spanish text to english text (by default)
translations = translator.translate(sentence, dest="no")

for translation in translations:
    print(f"{translation.text}")

