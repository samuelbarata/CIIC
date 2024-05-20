import csv
import random
import pandas as pd
from sklearn.model_selection import train_test_split

import main

headers = 'MemoryUsage,ProcessorLoad,InpNetThroughput,OutNetThroughput,OutBandwidth,Latency,V_MemoryUsage,V_ProcessorLoad,V_InpNetThroughput,V_OutNetThroughput,V_OutBandwidth,V_Latency'.split(',')

LEARN_DATA_INPUT = 'data/data_10_rng.csv'
LEARN_DATA_OUTPUT = 'data/TestResult-FSS_10_rng.csv'
TEST_DATA_INPUT = 'data/data_rng'
TEST_DATA_OUTPUT = 'data/TestResult-FSS_rng.csv'

# ## TRAIN DATA ##

print("Generating train inputs")
## generate inputs
with open(LEARN_DATA_INPUT, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    MIN = 0
    MAX = 101
    STEP = 10
    RANGE = range(MIN, MAX, STEP)
    RANGE2 = (10, 70, 100)
    for MemUsage in RANGE:
        for ProcessorLoad in RANGE:
            for OutNetThroughput in RANGE:
                for OutBandwidth in RANGE:
                    writer.writerow([MemUsage/100, ProcessorLoad/100, random.randint(0, 100)/100, OutNetThroughput/100, OutBandwidth/100, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100])
print("Train inputs generated")

print("Generating train outputs (fuzzy system)")
## get outputs from fuzzy system
with open(LEARN_DATA_OUTPUT, 'w') as f:
    f.write("MemoryUsage,ProcessorLoad,InpNetThroughput,OutNetThroughput,OutBandwidth,Latency,V_MemoryUsage,V_ProcessorLoad,V_InpNetThroughput,V_OutNetThroughput,V_OutBandwidth,V_Latency,CLPVariation")
    for index, row in main.read_input(LEARN_DATA_INPUT).iterrows():
        clp = main.find_clp(row['MemoryUsage'], row['ProcessorLoad'], row['InpNetThroughput'], row['OutNetThroughput'], row['OutBandwidth'], row['Latency'], row['V_MemoryUsage'], row['V_ProcessorLoad'], row['V_InpNetThroughput'], row['V_OutNetThroughput'], row['V_OutBandwidth'], row['V_Latency'])
        f.write(f"\n{row['MemoryUsage']},{row['ProcessorLoad']},{row['InpNetThroughput']},{row['OutNetThroughput']},{row['OutBandwidth']},{row['Latency']},{row['V_MemoryUsage']},{row['V_ProcessorLoad']},{row['V_InpNetThroughput']},{row['V_OutNetThroughput']},{row['V_OutBandwidth']},{row['V_Latency']},{clp}")
print("Train outputs (fuzzy system) generated")

# ## TEST (and Validation) DATA ##

print("Generating train inputs")
## generate inputs
with open(TEST_DATA_INPUT, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(headers)
    for _ in range(10000000):
        MemUsage = random.randint(0, 100)
        ProcessorLoad = random.randint(0, 100)
        InpNetThroughput = random.randint(0, 100)
        OutNetThroughput = random.randint(0, 100)
        OutBandwidth = random.randint(0, 100)
        Latency = random.randint(0, 100)
        V_MemoryUsage = random.randint(0, 100)
        V_ProcessorLoad = random.randint(0, 100)
        V_InpNetThroughput = random.randint(0, 100)
        V_OutNetThroughput = random.randint(0, 100)
        V_OutBandwidth = random.randint(0, 100)
        V_Latency = random.randint(0, 100)
        writer.writerow([MemUsage/100, ProcessorLoad/100, InpNetThroughput/100, OutNetThroughput/100, OutBandwidth/100, Latency/100, V_MemoryUsage/100, V_ProcessorLoad/100, V_InpNetThroughput/100, V_OutNetThroughput/100, V_OutBandwidth/100, V_Latency/100])
print("Train inputs generated")

print("Generating train outputs (fuzzy system)")
## get outputs from fuzzy system
with open(TEST_DATA_OUTPUT, 'w') as f:
    f.write("MemoryUsage,ProcessorLoad,InpNetThroughput,OutNetThroughput,OutBandwidth,Latency,V_MemoryUsage,V_ProcessorLoad,V_InpNetThroughput,V_OutNetThroughput,V_OutBandwidth,V_Latency,CLPVariation")
    for index, row in main.read_input(TEST_DATA_INPUT).iterrows():
        clp = main.find_clp(row['MemoryUsage'], row['ProcessorLoad'], row['InpNetThroughput'], row['OutNetThroughput'], row['OutBandwidth'], row['Latency'], row['V_MemoryUsage'], row['V_ProcessorLoad'], row['V_InpNetThroughput'], row['V_OutNetThroughput'], row['V_OutBandwidth'], row['V_Latency'])
        f.write(f"\n{row['MemoryUsage']},{row['ProcessorLoad']},{row['InpNetThroughput']},{row['OutNetThroughput']},{row['OutBandwidth']},{row['Latency']},{row['V_MemoryUsage']},{row['V_ProcessorLoad']},{row['V_InpNetThroughput']},{row['V_OutNetThroughput']},{row['V_OutBandwidth']},{row['V_Latency']},{clp}")
print("Train outputs (fuzzy system) generated")

print("Spliting the test dataset into validation and test")
# split the test dataset in Validation and Test
df_test = pd.read_csv(TEST_DATA_OUTPUT)
data = df_test[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
target = df_test['CLPVariation']

data_test, data_validate, target_test, target_validate = train_test_split(data, target, test_size=0.5, random_state=42)
data_test.to_csv('data/data_test.csv', index=False)
data_validate.to_csv('data/data_validate.csv', index=False)
target_test.to_csv('data/target_test.csv', index=False)
target_validate.to_csv('data/target_validate.csv', index=False)

print("Test dataset into validation and test datasets splitted")