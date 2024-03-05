# Google Translate In Python!
# Wonderland
# 2024-03-05
# This program is free for everyone to use, I am creating this as a learning opportunity for new developers.

from googletrans import Translator 
import time


class TextTranslator:
    def __init__(self):
        self.translator = Translator()
  
    def detect_language(self, text):
        translated = self.translator.detect(text)
        return translated.lang

    def translate(self, text, target_language='English'):
        translated = self.translator.translate(text, dest=target_language)
        return translated.text, translated.src

    def translate_to_specific_language(self, text, target_language):
        translated = self.translator.translate(text, dest=target_language)
        return translated.text, translated.src

if __name__ == "__main__":
    translator = TextTranslator()

    text_to_translate = input("Enter text to translate to English (any language): ")
    detected_language = translator.detect_language(text_to_translate)
    print("Detected language:", detected_language)

    translated_text, _ = translator.translate(text_to_translate)
    print("Translated to English:", translated_text)

    target_text = input("\n\nEnter the phrase you would like to translate (any language): ")
    target_language = input("Enter the language you would like to the phrase to: ")
    translated_text, _ = translator.translate_to_specific_language(target_text, target_language)
    print("Translated to", target_language + ":", translated_text)
    time.sleep(5)
