from camel_tools.utils.normalize import normalize_alef_maksura_ar
from camel_tools.utils.normalize import normalize_alef_ar
from camel_tools.utils.normalize import normalize_teh_marbuta_ar
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def text_normalize(text):
    text = normalize_alef_maksura_ar(text)
    text = normalize_alef_ar(text)
    text = normalize_teh_marbuta_ar(text)
    return text
    
def tokenizer(text):
    stop_words=[text_normalize(word) for word in stopwords.words("arabic")]
    tokens = word_tokenize(text)
    return [word for word in tokens if word not in stop_words]