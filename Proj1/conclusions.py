import pandas as df
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = df.read_csv('TestResult-FFNN.csv')

x, y = data['CLPVariation'], data['NN_Regression']

# scatter
# SMALL scatter
plt.scatter(x, y, color='red', s=0.1)
plt.title('CLPVariation vs NN_Regression')
plt.xlabel('CLPVariation')
plt.ylabel('NN_Regression')

# linear regression
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='blue', label='Linear Regression')
plt.plot(x, x, color='green', label='Y=x')
plt.legend(loc="upper left")

plt.show()

