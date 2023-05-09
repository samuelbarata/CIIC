import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def point_finder(df, column, sample):
    return df[column].tolist().index(sample)

def analyze_column(df, column, k=10):
    arr = np.array(df[column])
    mean = np.mean(arr)
    std_dev = np.std(arr)
    for i in arr:
        if(k*std_dev < abs(i - mean)):
            very_far_point_remove(df, column, i)

def very_far_point_remove(df, column, sample):
    """Finds the given point and removes it from df[column]"""
    index = point_finder(df, column, sample)
    print("Very far point at index: " + str(index))
    df.drop(index, inplace=True)

def very_far_point_previous(df, column, sample):
    """Finds the given point and changes it to the previous value"""
    index = point_finder(df, column, sample)
    print("Very far point at index: " + str(index))
    df[column][index] = df[column][index-1]

def very_far_point_interpolation(df, column, sample):
    """Finds the given point and changes it to the interpolation of previous and next values"""
    index = point_finder(df, column, sample)
    print("Very far point at index: " + str(index))
    df[column][index] = (df[column][index-1] + df[column][index+1]) / 2

df = pd.read_csv('EURUSD_Daily_Ask_2018.12.31_2019.10.05v2.csv')
COLUMNS = ['Open', 'High', 'Low', 'Close'] #, 'Volume']
for column in COLUMNS:
    analyze_column(df, column)
    plt.title(label=column)
    plt.plot(pd.to_datetime(df['Time (UTC)']), df[column])
    plt.show()

df.to_csv('ChangedData.csv', decimal='.', sep=',', index=False)
