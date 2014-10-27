#make sure you have already downloaded the module we will be using, i.e.
#    use the terminal or cmd.exe if you're on windows and type
#    pip install translate

from translate import Translator

abbreviations = {"English": "eng",
                 "Chinese": "zh",
                 "Russian": "ru",
                 "German": "de",
                 "French": "fr",
                 "Japanese": "ja",
                 "Korean": "ko"}

toGerman = Translator(to_lang=abbreviations["German"])
toFrench = Translator(to_lang="abbreviations["French"])
toKorean = Translator(to_lang=abbreviations["Korean"])

toGerman.translate("Hi")
toFrench.translate("Hi")
toKorean.translate("Hi")

