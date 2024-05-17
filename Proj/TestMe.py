import main

INPUT = 'data.csv'
OUTPUT = 'TestResult-FSS.csv'
APPEND = True

outs = []

if not APPEND:
    df = main.read_input(INPUT)
    for index, row in df.iterrows():
        clp = main.find_clp(row['MemoryUsage'], row['ProcessorLoad'], row['InpNetThroughput'], row['OutNetThroughput'], row['OutBandwidth'], row['Latency'], row['V_MemoryUsage'], row['V_ProcessorLoad'], row['V_InpNetThroughput'], row['V_OutNetThroughput'], row['V_OutBandwidth'], row['V_Latency'])
        outs.append(clp)

    with open(OUTPUT, 'w') as f:
        f.write("CLPVariation")
        for clp in outs:
            f.write(f"\n{clp}")
else:
    with open(OUTPUT, 'w') as f:
        f.write("MemoryUsage,ProcessorLoad,InpNetThroughput,OutNetThroughput,OutBandwidth,Latency,V_MemoryUsage,V_ProcessorLoad,V_InpNetThroughput,V_OutNetThroughput,V_OutBandwidth,V_Latency,CLPVariation")
        for index, row in main.read_input(INPUT).iterrows():
            clp = main.find_clp(row['MemoryUsage'], row['ProcessorLoad'], row['InpNetThroughput'], row['OutNetThroughput'], row['OutBandwidth'], row['Latency'], row['V_MemoryUsage'], row['V_ProcessorLoad'], row['V_InpNetThroughput'], row['V_OutNetThroughput'], row['V_OutBandwidth'], row['V_Latency'])
            f.write(f"\n{row['MemoryUsage']},{row['ProcessorLoad']},{row['InpNetThroughput']},{row['OutNetThroughput']},{row['OutBandwidth']},{row['Latency']},{row['V_MemoryUsage']},{row['V_ProcessorLoad']},{row['V_InpNetThroughput']},{row['V_OutNetThroughput']},{row['V_OutBandwidth']},{row['V_Latency']},{clp}")
