from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate("Hola Mundo")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

