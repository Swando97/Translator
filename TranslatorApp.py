from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

sentence = ["Kjære venner og familie, jeg er veldig lei meg. Det var aldri min intensjon å skade noen. Meg inkludert.",
"Jeg må beklage. Jeg vil eie opp til feilene mine. Jeg var tapt. Jeg så utover etter svar; ikke innover.",
"Jeg var ikke motivert. Å ikke ha noen tidsplan fikk meg til å føle at jeg ikke hadde noen hensikt. Jeg kjempet mot smertene mine med stoffer.",
"Jeg følte meg mer funksjonshemmet enn noen gang før. Jeg ønsket å gå videre, men jeg følte meg frossen. Dette var min feil, ikke din.",
"Nå har jeg begynt å utvikle meg. Jeg har en daglig tidsplan. Jeg ser meg selv jobbe mot målene mine.",
"Jeg er spent på fremtiden, jeg håper du også er det. Jeg tenker på dere mennesker hver dag, og jeg kan ikke vende tilbake hendene på tiden.",
"Jeg kan imidlertid se tilbake og lære av feilene mine. Jeg skjønner at jeg ikke kunne ha gjort dette uten din hjelp og støtte.",
"Jeg vil aldri være i stand til å betale tilbake dere for de tingene dere gjorde. Jeg vil prøve. Jeg vil begynne med å si at jeg elsker deg. Takk skal du ha."]

# translate a spanish text to english text (by default)
translations = translator.translate(sentence)

for translation in translations:
    print(f"{translation.text}")

# Lets get the Text-to-Speech library imported and read this "hidden" message! 
# 1) download TTS library on terminal
# 2) import the TTS library into program
# 3) create instance of TTS object
# 4) invoke the TTS object to read sentences in English
# 5) give the TTS object a Norwegian accent for lol's 
# -----------------------------------------------------------------------------
# START NEW PYTHON PROJECT (Research some cool options)
# I need to make a push to GitHub... This is a shortcut day b/c I was developing my website QRZones and learning SalesForce 