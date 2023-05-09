import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df1 = pd.read_csv('DCOILWTICOv2.csv')
df2 = pd.read_csv('DCOILBRENTEUv2.csv')

# plot the two series
plt.title(label='WTI and BRENT')
plt.plot(pd.to_datetime(df1['DATE']), df1['DCOILWTICO'], label='WTI')
plt.plot(pd.to_datetime(df2['DATE']), df2['DCOILBRENTEU'], label='BRENT')
plt.legend()
plt.show()


merged = pd.merge(df1, df2, on='DATE', how='inner')
#merged.to_csv('MergedData.csv', decimal='.', sep=',', index=False)
merged["Difference"] = merged["DCOILWTICO"] - merged["DCOILBRENTEU"]

plt.title(label='WTI - BRENT')
plt.scatter(pd.to_datetime(merged['DATE']), merged['Difference'])
plt.show()
