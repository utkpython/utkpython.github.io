#make sure you have already downloaded the module we will be using, i.e.
# use the terminal or cmd.exe if you're on windows and type
# pip install translate
from translate import Translator
abbreviations = {"Chinese": "zh",
                "Russian": "ru",
                "German": "de",
                "French": "fr",
                "Japanese": "ja",
                "Korean": "ko",
                "Dutch": "nl",
                "Hindi": "hi",
                "Arabic": "ar",
                "Tamil": "ta"}
toGerman = Translator(to_lang=abbreviations["German"])
toFrench = Translator(to_lang=abbreviations["French"])
toKorean = Translator(to_lang=abbreviations["Korean"])
# make one for another one of the languages above
# better yet, search for another language abbreviation, add it to our dictionary, and translate for that language
toGerman.translate("Hi")
toFrench.translate("Hi")
toKorean.translate("Hi")

testTranslator = Translator(to_lang="en")
message = unicode("The day is young")
for abbrev in abbreviations:
    testTranslator.to_lang = abbreviations[abbrev]
    temp = testTranslator.translate('%s'%message)
    quotedMessage = "\"" + message + "\""
    print "A rough translation of", quotedMessage, "in", abbrev, "is", temp
