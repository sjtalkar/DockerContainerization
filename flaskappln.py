from flask import Flask, request
import pandas as pd
import numpy as np
import pickle as pkl

app=Flask(__name__)



pickle_in = open('classifier.pkl', 'rb')
classifier= pkl.load(pickle_in)

@app.route('/')
def  welcome():
    return "Welcome to the application"

@app.route('/predict')
def predict_note_authentication():

    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return f"The predicted value is class : {prediction}"


@app.route('/predict_file', methods=['POST'])
def predict_note_authentication_file():

    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)

    return f"The predicted values are : {list(prediction)}"



if __name__=='__main__':
    app.run()
