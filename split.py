import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

train_full = pd.read_csv('cs-training.csv')
y = train_full['SeriousDlqin2yrs']
X = train_full.drop(columns=['SeriousDlqin2yrs'])

def split_data():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    return X_train, X_test, y_train, y_test

def write_csv(dataframe, filename):
    pd.DataFrame.to_csv(f'./{filename}.csv', index=False)

def main():
    X_train, X_test2, y_train, test2 = split_data()
    write_csv(X_test2, 'test2-input')
    write_csv(test2, 'test2')

if __name__ == "__main__":
    main()