import main
import NN
import NN_classifier

import pickle
import pandas as pd

INPUT = 'Proj1_TestS.csv'
OUTPUT_FIS = 'TestResult-FSS.csv'
OUTPUT_NN = 'TestResult-FFNN.csv'

MLP_PATH = 'mlp.pickle'

## FUZZY SYSTEM ##

fs = []

df = main.read_input(INPUT)
for index, row in df.iterrows():
    clp = main.find_clp(row['MemoryUsage'], row['ProcessorLoad'], row['InpNetThroughput'], row['OutNetThroughput'], row['OutBandwidth'], row['Latency'], row['V_MemoryUsage'], row['V_ProcessorLoad'], row['V_InpNetThroughput'], row['V_OutNetThroughput'], row['V_OutBandwidth'], row['V_Latency'])
    fs.append(clp)

with open(OUTPUT_FIS, 'w') as f:
    f.write("CLPVariation")
    for clp in fs:
        f.write(f"\n{clp}")

## NEURAL NETWORK ##

mlp = pickle.load(open(MLP_PATH, 'rb'))

data = df[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
df = pd.read_csv(OUTPUT_FIS)
target = df['CLPVariation']

pred_regr = NN.test(mlp, data, target)
pred_class = NN_classifier.test(mlp, data, NN_classifier.transform_target(target))
outs = [fs, pred_regr, pred_class]

with open(OUTPUT_NN, 'w') as f:
    f.write("CLPVariation,NN_Regression,NN_Classifier")
    for i in range(len(outs[0])):
        f.write(f"\n{outs[0][i]},{outs[1][i]},{outs[2][i]}")
