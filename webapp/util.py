from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

stop_words = set(stopwords.words('english'))
porter_stemmer = PorterStemmer()

def data_preprocessing(data):
    data = data.lower()                                          # Lowercase
    data = re.sub(r'[^a-zA-Z0-9\s]', ' ', data)                  # Noise removal (regex to remove punctuations)
    data = data.strip()                                          # Noise removal (extra spaces)
    words = data.split()                                         # Split sentence into list of words
    words = [w for w in words if not w in stop_words]            # Stopwords removal
    words = [porter_stemmer.stem(word) for word in words]        # Replace the word by its stem
    data = ' '.join(words)                                       # Transform list of words to str
    return data

def data_vectorization(data, vectorizer):
    return vectorizer.transform([data])

def mbti_prediction(data, model_ie, model_sn, model_tf, model_jp):
    result_ie = model_ie.predict(data)
    result_sn = model_sn.predict(data)
    result_tf = model_tf.predict(data)
    result_jp = model_jp.predict(data)
    return f'{result_ie[0]}{result_sn[0]}{result_tf[0]}{result_jp[0]}'


# if __name__ == '__main__':
#     data = "Hello Boys !"
#     new_d = data_preprocessing(data)
#     print(new_d)
#     d_v = data_vectorization(new_d, vectorizer)
#     print(d_v)
#     pred = mbti_prediction(d_v, model_ie, model_sn, model_tf, model_jp)
#     print(pred)