import pandas as pd
import matplotlib.pyplot as plt
from simpful import *

DATASET_PATH = 'CI4IoT23-24_Proj1_SampleData.csv'

# TODO: Remove this line https://github.com/aresio/simpful/tree/master/examples

# CPU Memory
FS = FuzzySystem()

# Processor Load
PL_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
PL_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=0.75, d=1), term="medium")
PL_3 = FuzzySet(function=Trapezoidal_MF(a=0.70, b=1.0, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("ProcessorLoad", LinguisticVariable([PL_1, PL_2, PL_3], concept="Processor Load", universe_of_discourse=[0,1]))

# Memory Usage
MU_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
MU_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=0.75, d=1), term="medium")
MU_3 = FuzzySet(function=Trapezoidal_MF(a=0.70, b=1.0, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("MemoryUsage", LinguisticVariable([MU_1, MU_2, MU_3], concept="Memory Usage", universe_of_discourse=[0,1]))

# CpuMem
T_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.6), term="low")
T_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.7, c=0.7, d=0.9), term="medium")
T_3 = FuzzySet(function=Trapezoidal_MF(a=0.80, b=1.0, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("CpuMem", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0,1]))


# Define fuzzy rules
R1_1 = "IF (ProcessorLoad IS high) OR (MemoryUsage IS high) THEN (CpuMem IS high)"
R1_2 = "IF (ProcessorLoad IS medium) OR (MemoryUsage IS medium) THEN (CpuMem IS medium)"
R1_3 = "IF (ProcessorLoad IS low) OR (MemoryUsage IS low) THEN (CpuMem IS low)"
FS.add_rules([R1_1, R1_2, R1_3])

# Network
FS2 = FuzzySystem()

# InpNetThroughput
IN_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
IN_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.70, c=0.7, d=0.8), term="medium")
IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.60, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("InpNetThroughput", LinguisticVariable([IN_1, IN_2, IN_3], concept="Input Network Throughput", universe_of_discourse=[0,1]))

# OutNetThroughput
OUT_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
OUT_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.70, c=0.7, d=0.8), term="medium")
OUT_3 = IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.60, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutNetThroughput", LinguisticVariable([OUT_1, OUT_2, OUT_3], concept="Output Network Throughput", universe_of_discourse=[0,1]))

# OutBandwidth
OB_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
OB_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.70, c=0.7, d=0.8), term="medium")
OB_3 = IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.60, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutBandwidth", LinguisticVariable([OB_1, OB_2, OB_3], concept="Output Bandwidth", universe_of_discourse=[0,1]))

# Latency
L_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
L_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.70, c=0.7, d=0.8), term="medium")
L_3 = IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.60, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("Latency", LinguisticVariable([L_1, L_2, L_3], concept="Latency", universe_of_discourse=[0,1]))

# Network Usage
NU_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
NU_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.70, c=0.7, d=0.8), term="medium")
NU_3 = IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.60, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("NetUsage", LinguisticVariable([NU_1, NU_2, NU_3], concept="Network Usage", universe_of_discourse=[0,1]))

# Define Rules
R2_1 = "IF (InpNetThroughput IS high) OR (OutNetThroughput IS high) OR (OutBandwidth IS high) OR (Latency IS high) THEN (NetUsage IS high)"




FS_OUT = FuzzySystem()








if __name__ == '__main__':
    df = pd.read_csv(DATASET_PATH)

    fig = FS.plot_surface(variables=['ProcessorLoad','MemoryUsage'], output='CpuMem')

    for index, row in df.iterrows():
        memory_usage = row['MemoryUsage']
        process_load = row['ProcessorLoad']
        input_throughput = row['InpNetThroughput']
        output_throughput = row['OutNetThroughput']
        output_available_bandwidth = row['OutBandwidth']
        latency = row['Latency']
        memory_usage_variation = row['V_MemoryUsage']
        process_load_variation = row['V_ProcessorLoad']
        input_throughput_variation = row['V_InpNetThroughput']
        output_throughput_variation = row['V_OutNetThroughput']
        output_available_bandwidth_variation = row['V_OutBandwidth']
        latency_variation = row['V_Latency']
        clp_variation = row['CLPVariation']

        # Set values
        FS.set_variable("ProcessorLoad", process_load)
        FS.set_variable("MemoryUsage", memory_usage)

        FS2.set_variable("InpNetThroughput", input_throughput)
        FS2.set_variable("OutNetThroughput", output_throughput)
        FS2.set_variable("OutBandwidth", output_available_bandwidth)
        FS2.set_variable("Latency", latency)

        # Evaluate the system
        cpu_mem = FS.Mamdani_inference(["CpuMem"])
        #network = FS2.Mamdani_inference(["NetUsage"])






        print(f"CPU: {process_load}; Mem: {memory_usage}; {cpu_mem['CpuMem']}")
        break
