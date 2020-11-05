# MBTI-PREDICTION

:date: Creation date: October 2020 

## :dart: Objective

Predict the user's MBTI profile from a few sentences defining it.

The **Myers–Briggs Type Indicator (MBTI)** is an introspective self-report questionnaire indicating differing psychological preferences in how people perceive the world and make decisions. The test attempts to assign four categories:
- introversion (I) or extraversion (E),
- sensing (S) or intuition (N), 
- thinking (T) or feeling (F), 
- judging (J) or perceiving (P).

One letter from each category is taken to produce a four-letter test result, like "INFJ" or "ENFP".
<br>Source : https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator
<br>Data source : https://www.kaggle.com/datasnaek/mbti-type

## :black_nib: Description

Once the web application is launched, the user should write the largest description of himself. After that, the user clicks on the "Predict" button and the models return the user MBTI profile.

## :rocket: How to start the application?

To download and install the dependencies:
```
pip install -r requirements.txt
```
To launch the web application:
```
python app.py
```
To access the application in a web browser, enter this address in the search bar:
```
http://127.0.0.1:5000/
```

## :weight_lifting: Details on model training strategy

Available notebooks:
- Multi-class classification: [Strategy 1](notebooks/Strategy&#32;1.ipynb)
- Multiple binary classifications: [Strategy 2](notebooks/Strategy&#32;2.ipynb)

## :eyes: Overview



