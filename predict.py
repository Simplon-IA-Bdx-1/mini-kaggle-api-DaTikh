import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv('train.csv')
test = pd.read_csv('test2.csv')

label = 'SeriousDlqin2yrs'
y_train = train[label]
X_train = train.drop(columns=[label])
X_test = test.drop(columns=[label]) 

def main():
    clf = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)
    df = pd.DataFrame(clf.predict_proba(X_test))
    df[1].to_csv('test2-predictions.csv', index=True)

if __name__ == "__main__":
    main()