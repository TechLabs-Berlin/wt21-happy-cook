import numpy as np
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words
import numpy as np
import re


def convert_lower_case(data):
    return np.char.lower(data)

def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def remove_apostrophe(data):
    return np.char.replace(data, "'", "")

def stemming(data):
    stemmer= PorterStemmer()
    
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text
    
def convert_numbers(data):
    tokens = word_tokenize(str(data))
    
    new_text = ""
    for w in tokens:

        for character in w:
            if character.isdigit():
                w = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", w)
        
        try:
            
            w = num2words(int(w))
        except:
            a = 0
        new_text = new_text + " " + w
        
    new_text = np.char.replace(new_text, "-", " ")
    
    return new_text


def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~"
    
    data = np.char.replace(data, " m\\n", ' minutes ' )
    data = np.char.replace(data, 'h\\', ' hours ')
    data = np.char.replace(data, ' h ', ' hours ')

    data = np.char.replace(data, "\\n", ' ')

    for i in range(len(symbols)):
        
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
        
    data = np.char.replace(data, ',', '')
    data = np.char.replace(data, ' f ', ' fahrenheit ')
    data = np.char.replace(data, ' c ', ' celcius ')
    data = np.char.replace(data, " u'", ' ' )

    return data


def remove_otherwords(data):
    data = np.char.replace(data, 'prep', ' ')
    data = np.char.replace(data, 'directions', ' ')
    return data


def preprocess(data):
    data = convert_lower_case(data)
    data = convert_numbers(data)
    data = remove_punctuation(data) #remove comma seperately
    data = convert_numbers(data)
    data = remove_apostrophe(data)
    data = remove_stop_words(data)
    data = convert_numbers(data)
    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
    return data