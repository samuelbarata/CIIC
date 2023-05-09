import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('ChangedData.csv')

# variation from the previous day
plt.title(label='Variation from the previous day')
plt.hist(df['Close'].diff())
plt.show()

# histogram with the variation in the day (High to Low)
plt.title(label='Variation in the day (High to Low)')
High = df['High']
Low = df['Low']
plt.hist(High - Low)
plt.show()

