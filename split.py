import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

train_full = pd.read_csv('cs-training.csv')

def split_data():
    train, test = train_test_split(train_full, test_size=0.1, random_state=42)
    return train, test

def write_csv(dataframe, filename):
    dataframe.to_csv(f'./{filename}.csv', index=False)

def main():
    train, test = split_data()
    write_csv(train, 'train')
    write_csv(test, 'test2')

if __name__ == "__main__":
    main()