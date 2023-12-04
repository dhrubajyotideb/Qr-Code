from googletrans import Translator
def translate_text(text, target_language='bn'):  # 'bn' is the language code for Bengali 'hi' for Hindi
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Take user input
text_to_translate = input("Enter the text you want to translate from English to Bengali: ")

translated_text = translate_text(text_to_translate)
print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")