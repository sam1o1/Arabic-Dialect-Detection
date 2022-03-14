from camel_tools.utils.normalize import normalize_alef_maksura_ar
from camel_tools.utils.normalize import normalize_alef_ar
from camel_tools.utils.normalize import normalize_teh_marbuta_ar
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re 
import pickle 
import numpy as np

rnn = tf.keras.models.load_model(r"C:\Users\Eslam\OneDrive\Desktop\Arabic Dialect Classification\Deepl learning\Files\rnn_model.h5")
token = pickle.load(open(r"C:\Users\Eslam\OneDrive\Desktop\Arabic Dialect Classification\Deepl learning\Files\tokenizer.pickle", "rb"))

def text_normalize(text):
    text = normalize_alef_maksura_ar(text)
    text = normalize_alef_ar(text)
    text = normalize_teh_marbuta_ar(text)
    return text
    
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
    max_length=86
    y_id_to_word={1: 'eg',2: 'pl',3: 'kw',4: 'ly',5: 'qa',6: 'jo',7: 'lb',8: 'sa',9: 'ae',10: 'bh',11: 'om',12: 'sy',13: 'dz',14: 'iq',15: 'sd',16: 'ma',17: 'ye',18: 'tn'}
    text=preprocessing(text)
    sentence = [token.word_index[word] for word in text.split()]
    sentence = pad_sequences([sentence], maxlen=max_length, padding='post')
    return y_id_to_word[np.argmax(rnn.predict(sentence)[0])]