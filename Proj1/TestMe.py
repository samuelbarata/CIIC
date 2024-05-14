import main

INPUT = 'Proj1_TestS.csv'
OUTPUT = 'TestResult-FSS.csv'

outs = []

df = main.read_input(INPUT)
for index, row in df.iterrows():
    clp = main.find_clp(row['MemoryUsage'], row['ProcessorLoad'], row['InpNetThroughput'], row['OutNetThroughput'], row['OutBandwidth'], row['Latency'], row['V_MemoryUsage'], row['V_ProcessorLoad'], row['V_InpNetThroughput'], row['V_OutNetThroughput'], row['V_OutBandwidth'], row['V_Latency'])
    outs.append(clp)

with open(OUTPUT, 'w') as f:
    f.write("CLPVariation")
    for clp in outs:
        f.write(f"\n{clp}")
