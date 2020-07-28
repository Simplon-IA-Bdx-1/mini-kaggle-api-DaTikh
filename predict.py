import numpy as np
import pandas as pd
from sklearn import svm

train = pd.read_csv('train.csv')
test = pd.read_csv('test2.csv')

label = 'SeriousDlqin2yrs'
y_train = train[label]
X_train = train.drop(columns=[label])
X_test = test.drop(columns=[label]) 

clf = svm.SVC().fit(X_train, y_train)

def main():
    df = pd.DataFrame(clf.predict(X_test), columns=['Pred'])
    df.to_csv('test2-predictions.csv')

if __name__ == "__main__":
    main()