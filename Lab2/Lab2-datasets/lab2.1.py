import numpy as np
import pandas as pd
df = pd.read_csv('AAPL_yah.csv')
df1 = df.sort_values(by=['Close'])
#df1.to_csv('ChangedData.csv')

df1.to_csv('ChangedData.csv', decimal=',', sep=';', index=False)
