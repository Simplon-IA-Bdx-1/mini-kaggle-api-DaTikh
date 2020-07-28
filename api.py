from flask import Flask, request
from flask_restplus import Api, Resource
import pandas as pd
import numpy as np
from sklearn import metrics

app = Flask(__name__)       

@app.route('/submit', method=['POST'])

def get_auc():
    y = np.array(pd.read_csv('test2.csv')['SeriousDlqin2yrs'])
    pred = np.array(pd.read_csv(request.files)['pred'])
    result = metrics.auc(y, pred)
    return {
        "AUC": result
    }

if __name__ == '__main__':
    app.run(debug=True)