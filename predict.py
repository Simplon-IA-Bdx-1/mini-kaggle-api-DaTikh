import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier

train = pd.read_csv('train.csv')
test = pd.read_csv('test2.csv')

label = 'SeriousDlqin2yrs'
y_train = train[label]
X_train = train.drop(columns=[label])
X_test = test.drop(columns=[label]) 

def main():
    clf = SGDClassifier().fit(X_train, y_train)
    df = pd.DataFrame(clf.predict(X_test))
    df.to_csv('test2-predictions.csv', index=False)

if __name__ == "__main__":
    main()