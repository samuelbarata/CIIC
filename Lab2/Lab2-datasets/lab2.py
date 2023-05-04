import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime

STRANGE_COLUMN_NAME = 'DCOILBRENTEU'

df = pd.read_csv('DCOILBRENTEUv2.csv')
arr = np.array(df[STRANGE_COLUMN_NAME])

#Normalized min-max
normalized_vector = arr / np.linalg.norm(arr)

#Standardized z-score
mean = np.mean(arr)
std_dev = np.std(arr)
data_standardized = (arr - mean) / std_dev

#Smoothed 30-day moving average
NUM_DAYS = 30
weights = np.repeat(1.0, NUM_DAYS) / NUM_DAYS #[0.03333333, 0.03333333...]
smoothed_vector = np.convolve(data_standardized, weights, 'valid')

# the axis labels aren't technically aligned with the data :zipper_mouth_face:
get_random_points = np.arange(0, len(smoothed_vector), 90)
axis = [df['DATE'][i] for i in get_random_points]

# doesn't show the real data but makes sure the points are evenly spaced
x_smooth = np.arange(0, len(smoothed_vector))

plt.figure()
plt.subplot(411)
plt.title(label='Original')
plt.plot(df['DATE'], df[STRANGE_COLUMN_NAME])

plt.subplot(412)
plt.title(label='Normalized')
plt.plot(df['DATE'], normalized_vector)

plt.subplot(413)
plt.title(label='Standardized')
plt.plot(df['DATE'], data_standardized)

ax4 = plt.subplot(414)
plt.title(label='Smoothed')
plt.plot(x_smooth, smoothed_vector)
ax4.set_xticks(get_random_points)
ax4.set_xticklabels(axis)
plt.show()
