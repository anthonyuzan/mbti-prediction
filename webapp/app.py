from flask import Flask, render_template, request
from joblib import load
from util import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    req_data = request.get_json()['sentences']
    data_preprocessed = data_preprocessing(req_data)
    data_vector = data_vectorization(data_preprocessed, vectorizer)
    prediction = mbti_prediction(data_vector, model_ie, model_sn, model_tf, model_jp)
    return prediction

if __name__ == '__main__':
    vectorizer = load('../vectorizers/tfidf.joblib')
    model_ie = load('../models/model_ie.joblib')
    model_sn = load('../models/model_sn.joblib')
    model_tf = load('../models/model_tf.joblib')
    model_jp = load('../models/model_jp.joblib')
    app.run(port=5000)