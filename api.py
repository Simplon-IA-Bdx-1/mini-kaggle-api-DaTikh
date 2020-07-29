from flask import Flask, request
import pandas as pd
import numpy as np
from sklearn import metrics

app = Flask(__name__)       

@app.route('/submit', methods=['POST'])

def submit():
    f = request.files
    y = np.array(pd.read_csv('test2.csv')['SeriousDlqin2yrs'])
    pred = np.array(pd.read_csv(f['file'].stream))
    result = metrics.roc_auc_score(y, pred)
    return {
        "AUC": result
    }

if __name__ == '__main__':
    app.run(debug=True)