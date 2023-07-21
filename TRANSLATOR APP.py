#!/usr/bin/env python
# coding: utf-8

# # BHARAT INTERN ARTIFICIAL INTELLIGENCE INTERNSHIP

# # TASK 3: TRANSLATOR APP

# # BY AYUSHI GEORGE

# In[4]:


get_ipython().system('pip install googletrans==4.0.0-rc1')


# In[5]:


from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def main():
    print("Language Translator App")
    print("Supported Languages:")
    print("English: en, Spanish: es, French: fr, German: de, Hindi: hi, Chinese: zh-CN")
    
    src_lang = input("Enter the source language code (e.g., en for English): ")
    dest_lang = input("Enter the destination language code (e.g., fr for French): ")
    text_to_translate = input("Enter the text to translate: ")

    translated_text = translate_text(text_to_translate, src_lang, dest_lang)
    print("Translated Text:")
    print(translated_text)

if __name__ == "__main__":
    main()


# In[ ]:




