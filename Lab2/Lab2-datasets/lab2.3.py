import numpy as np
import pandas as pd
import time

df = pd.read_csv('AAPL_yah.csv')

a = np.arange(10)
print(a)
b=np.where(a<5, a, 10*a)
print(b)

df['signal']=np.where(df['Close']>df['Open'], 1.0, 0.0)
df.to_csv('ChangedData.csv', decimal=',', sep=';', index=False)
