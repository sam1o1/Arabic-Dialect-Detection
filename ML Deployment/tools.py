from helper import tokenizer , text_normalize
import re 
import pickle 
import numpy as np


model=pickle.load(open(r"C:\Users\Eslam\OneDrive\Desktop\Arabic Dialect Classification\Machine learning\Files\logistic_regression.pickle",'rb'))
transformer=pickle.load(open(r"C:\Users\Eslam\OneDrive\Desktop\Arabic Dialect Classification\Machine learning\Files\Tfidf.pickle",'rb'))

def preprocessing(text):
    """
    The data preprocessing fuction takes string, extracts only arabic text out of it,
    removes الهمزة والتاء المربوطة
    Input >>> text
    Output >>> clean text
    """
    text=re.sub(r'[^\s\u0627-\u064a]','', text)
    text=re.sub(r'(.)\1+', r'\1', text)
    text=text_normalize(text)
    return text

def predcitor(text):
    """
    this function takes text and returns the dialect
    it normalizes the entered text and use it to predict the dialect.
    """
    y_id_to_word={           0: 'IQ',
                             1: 'LY',
                             2: 'QA',
                             3: 'PL',
                             4: 'SY',
                             5: 'TN',
                             6: 'JO',
                             7: 'MA',
                             8: 'SA',
                             9: 'YE',
                             10: 'DZ',
                             11: 'LB',
                             13: 'KW',
                             14: 'OM',
                             15: 'SD',
                             16: 'AE',
                             17: 'BH'}
    text=preprocessing(text)
    text=text.split(" ")
    try:
        return y_id_to_word[np.argmax(model.predict(transformer.transform(text)))]
    except:
        return "Cannot indentify"
    