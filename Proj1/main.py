import pandas as pd
from sklearn import preprocessing

DATASET_PATH = 'CI4IoT23-24_Proj1_SampleData.csv'


if __name__ == '__main__':
    df = pd.read_csv(DATASET_PATH)
    print(df.head())
