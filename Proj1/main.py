import pandas as pd
import matplotlib.pyplot as plt
from simpful import *

DATASET_PATH = 'CI4IoT23-24_Proj1_SampleData.csv'

# TODO: Remove this line https://github.com/aresio/simpful/tree/master/examples


# #### HARDWARE RESOURCES ####
FS = FuzzySystem(show_banner=False)

# Processor Load
PL_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
PL_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
PL_3 = FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.75, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("ProcessorLoad", LinguisticVariable([PL_1, PL_2, PL_3], concept="Processor Load", universe_of_discourse=[0,1]))

# Memory Usage
MU_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
MU_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=0.75, d=1), term="medium")
MU_3 = FuzzySet(function=Trapezoidal_MF(a=0.70, b=1.0, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("MemoryUsage", LinguisticVariable([MU_1, MU_2, MU_3], concept="Memory Usage", universe_of_discourse=[0,1]))

# Hardware Resources
T_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
T_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
T_3 = FuzzySet(function=Trapezoidal_MF(a=0.7, b=0.75, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("CpuMem", LinguisticVariable([T_1, T_2, T_3], concept="Hardware Resources", universe_of_discourse=[0,1]))

# Define fuzzy rules
R1_1 = "IF (ProcessorLoad IS high) OR (MemoryUsage IS high) THEN (CpuMem IS high)"
R1_2 = "IF (ProcessorLoad IS medium) OR (MemoryUsage IS medium) THEN (CpuMem IS medium)"
R1_3 = "IF (ProcessorLoad IS low) OR (MemoryUsage IS low) THEN (CpuMem IS low)"
FS.add_rules([R1_1, R1_2, R1_3])


# #### NETWORK USAGE ####

# ### Output Congestion ###

FS2 = FuzzySystem(show_banner=False)

# OutNetThroughput
OUT_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
OUT_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
OUT_3 = FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.75, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutNetThroughput", LinguisticVariable([OUT_1, OUT_2, OUT_3], concept="Output Network Throughput", universe_of_discourse=[0,1]))

# OutBandwidth
OB_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
OB_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=0.75, d=1), term="medium")
OB_3 = FuzzySet(function=Trapezoidal_MF(a=0.70, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutBandwidth", LinguisticVariable([OB_1, OB_2, OB_3], concept="Available Output Bandwidth", universe_of_discourse=[0,1]))

# Output Congestion
OC_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
OC_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=0.75, d=1), term="medium")
OC_3 = FuzzySet(function=Trapezoidal_MF(a=0.70, b=1.0, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutCongestion", LinguisticVariable([OC_1, OC_2, OC_3], concept="Output Congestion", universe_of_discourse=[0,1]))

# Define fuzzy rules
R2_1 = "IF (OutNetThroughput IS high) THEN (OutCongestion IS high)"
R2_2 = "IF (OutNetThroughput IS medium) AND (OutBandwidth IS low) THEN (OutCongestion IS high)"
R2_3 = "IF (OutNetThroughput IS low) AND (OutBandwidth IS low) THEN (OutCongestion IS medium)"
R2_4 = "IF (OutNetThroughput IS medium) THEN (OutCongestion IS medium)"
R2_5 = "IF (OutNetThroughput IS low) THEN (OutCongestion IS low)"
FS2.add_rules([R2_1, R2_2, R2_3, R2_4, R2_5])


# ### Network Usage ###

FS3 = FuzzySystem(show_banner=False)

# Output Congestion
FS3.add_linguistic_variable("OutCongestion", LinguisticVariable([OC_1, OC_2, OC_3], concept="Output Congestion", universe_of_discourse=[0,1]))

# # InpNetThroughput
IN_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0, d=0.7), term="low")
IN_2 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.70, c=0.7, d=0.8), term="medium")
IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.60, b=1.0, c=1.0, d=1.0), term="high")
FS3.add_linguistic_variable("InpNetThroughput", LinguisticVariable([IN_1, IN_2, IN_3], concept="Input Network Throughput", universe_of_discourse=[0,1]))

# Network Usage
NU_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
NU_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
NU_3 = FuzzySet(function=Trapezoidal_MF(a=0.7, b=0.75, c=1.0, d=1.0), term="high")
FS3.add_linguistic_variable("NetUsage", LinguisticVariable([NU_1, NU_2, NU_3], concept="Network Usage", universe_of_discourse=[0,1]))

# Define fuzzy rules
R3_1 = "IF (OutCongestion IS high) THEN (NetUsage IS high)"
R3_2 = "IF (OutCongestion IS medium) AND (InpNetThroughput IS high) THEN (NetUsage IS high)"
R3_3 = "IF (OutCongestion IS low) AND (InpNetThroughput IS high) THEN (NetUsage IS medium)"
R3_4 = "IF (OutCongestion IS medium) THEN (NetUsage IS medium)"
R3_5 = "IF (OutCongestion IS low) THEN (NetUsage IS low)"
FS3.add_rules([R3_1, R3_2, R3_3, R3_4, R3_5])


# #### COMPUTING LOAD PERCENTAGE (CLP) ####

FS_CLP = FuzzySystem(show_banner=False)

# Latency TODO: VERIFICAR!!; estes valores de latencia fazem sentido, mas o CSV n tem nada deste tipo...
L_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=3, d=10), term="low")
L_2 = FuzzySet(function=Trapezoidal_MF(a=5, b=10, c=30, d=50), term="medium")
L_3 = FuzzySet(function=Trapezoidal_MF(a=30, b=70, c=10000000, d=10000000), term="high")
FS_CLP.add_linguistic_variable("Latency", LinguisticVariable([L_1, L_2, L_3], concept="Latency", universe_of_discourse=[0,10000000]))
FS_CLP.add_linguistic_variable("CpuMem", LinguisticVariable([T_1, T_2, T_3], concept="Hardware Resources", universe_of_discourse=[0,1]))
FS_CLP.add_linguistic_variable("NetUsage", LinguisticVariable([NU_1, NU_2, NU_3], concept="Network Usage", universe_of_discourse=[0,1]))

CLP_1 = FuzzySet(function=Trapezoidal_MF(a=-1, b=-1, c=-0.5, d=-0.75), term="decrease_much")
CLP_2 = FuzzySet(function=Trapezoidal_MF(a=-0.75, b=-0.5, c=-0.2, d=0), term="decrease")
CLP_3 = FuzzySet(function=Trapezoidal_MF(a=-0.2, b=-0.1, c=0.1, d=0.2), term="mantain")
CLP_4 = FuzzySet(function=Trapezoidal_MF(a=0, b=0.2, c=0.5, d=0.75), term="increase")
CLP_5 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=1, d=1), term="increase_much")
FS_CLP.add_linguistic_variable("CLP", LinguisticVariable([CLP_1, CLP_2, CLP_3, CLP_4, CLP_5], concept="CLP Variation", universe_of_discourse=[-1,1]))

# Rules
RC_1 = "IF (CpuMem IS high) AND (NetUsage IS low) THEN CLP IS decrease_much"
RC_2 = "IF (CpuMem IS low) AND (NetUsage IS high) THEN CLP IS increase_much"
RC_3 = "IF (CpuMem IS medium) AND (NetUsage IS medium) THEN CLP IS mantain"
FS_CLP.add_rules([RC_1, RC_2, RC_3])




if __name__ == '__main__':
    df = pd.read_csv(DATASET_PATH)

    # fig = FS.plot_surface(variables=['ProcessorLoad','MemoryUsage'], output='CpuMem')
    # fig2 = FS2.plot_surface(variables=['OutNetThroughput','OutBandwidth'], output='OutCongestion')
    # fig3 = FS3.plot_surface(variables=['OutCongestion','InpNetThroughput'], output='NetUsage')
    fig4 = FS_CLP.plot_surface(variables=['CpuMem','NetUsage'], output='CLP')

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
        cpu_mem = FS.Mamdani_inference(["CpuMem"])['CpuMem']

        FS2.set_variable("OutNetThroughput", output_throughput)
        FS2.set_variable("OutBandwidth", output_available_bandwidth)
        out_congestion = FS2.Mamdani_inference(["OutCongestion"])["OutCongestion"]

        FS3.set_variable("OutCongestion", out_congestion)
        FS3.set_variable("InpNetThroughput", input_throughput)
        net_usage = FS3.Mamdani_inference(["NetUsage"])["NetUsage"]

        FS_CLP.set_variable("Latency", latency)
        FS_CLP.set_variable("CpuMem", cpu_mem)
        FS_CLP.set_variable("NetUsage", net_usage)
        clp = FS_CLP.Mamdani_inference(["CLP"])["CLP"]

        #print(f"CPU: {process_load}; Mem: {memory_usage}; {cpu_mem}")
        #print(f"OutThroughput: {output_throughput}; OutBandAvail: {output_available_bandwidth}; {out_congestion}")
        print(f"Predicted CLP: {clp}; Expected CLP: {clp_variation}")
