import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('train.csv')
test = pd.read_csv('test2.csv')

label = 'SeriousDlqin2yrs'
y_train = train[label]
X_train = train.drop(columns=[label])
X_test = test.drop(columns=[label]) 

clf = LogisticRegression().fit(X_train, y_train)

def main():
    df = pd.DataFrame()
    df[label] = clf.predict_proba(X_test)
    df.to_csv('test2-predictions.csv', index=False)

if __name__ == "__main__":
    main()