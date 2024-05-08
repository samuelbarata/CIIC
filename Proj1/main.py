import pandas as pd
import matplotlib.pyplot as plt
from simpful import *

DATASET_PATH = 'CI4IoT23-24_Proj1_SampleData.csv'

# TODO: Remove this line https://github.com/aresio/simpful/tree/master/examples

# Create a fuzzy system
FS = FuzzySystem()

# Processor Load
PL_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=0.70), term="low")
PL_2 = FuzzySet(function=Triangular_MF(a=0.5, b=0.75, c=1.0), term="medium")
PL_3 = FuzzySet(function=Triangular_MF(a=0.70, b=1.0, c=1.0), term="high")
FS.add_linguistic_variable("ProcessorLoad", LinguisticVariable([PL_1, PL_2, PL_3], concept="Processor Load", universe_of_discourse=[0,1]))

# Memory Usage
MU_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=0.70), term="low")
MU_2 = FuzzySet(function=Triangular_MF(a=0.5, b=0.75, c=1.0), term="medium")
MU_3 = FuzzySet(function=Triangular_MF(a=0.70, b=1.0, c=1.0), term="high")
FS.add_linguistic_variable("MemoryUsage", LinguisticVariable([MU_1, MU_2, MU_3], concept="Memory Usage", universe_of_discourse=[0,1]))

# CpuMem
T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=0.70), term="low")
T_2 = FuzzySet(function=Triangular_MF(a=0.5, b=0.75, c=0.9), term="medium")
T_3 = FuzzySet(function=Triangular_MF(a=0.80, b=1.0, c=1.0), term="high")
FS.add_linguistic_variable("CpuMem", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0,1]))


# Define fuzzy rules
R1 = "IF (ProcessorLoad IS high) OR (MemoryUsage IS high) THEN (CpuMem IS high)"
R2 = "IF (ProcessorLoad IS medium) OR (MemoryUsage IS medium) THEN (CpuMem IS medium)"
R3 = "IF (ProcessorLoad IS low) OR (MemoryUsage IS low) THEN (CpuMem IS low)"
FS.add_rules([R1, R2, R3])

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

        # Set antecedents values
        FS.set_variable("ProcessorLoad", process_load)
        FS.set_variable("MemoryUsage", memory_usage)
        # Evaluate the system
        cpu_mem = FS.Mamdani_inference(["CpuMem"])


        print(f"CPU: {process_load}; Mem: {memory_usage}; {cpu_mem['CpuMem']}")
