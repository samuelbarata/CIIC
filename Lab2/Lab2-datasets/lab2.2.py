import numpy as np
import pandas as pd
import time

df = pd.read_csv('AAPL_yah.csv')

start_time1 = time.process_time()
start_time2 = time.perf_counter()

df['newCol'] = df['Volume'].cumsum()

print(f"time used in cumsum --> {time.process_time() - start_time1} seconds")
print(f"time used in cumsum --> {time.perf_counter() - start_time2} seconds")
