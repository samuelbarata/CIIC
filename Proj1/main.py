import pandas as pd
import matplotlib.pyplot as plt
from simpful import *
import logging

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
MU_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
MU_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
MU_3 = FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.75, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("MemoryUsage", LinguisticVariable([MU_1, MU_2, MU_3], concept="Memory Usage", universe_of_discourse=[0,1]))

# Hardware Resources
T_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
T_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
T_3 = FuzzySet(function=Trapezoidal_MF(a=0.7, b=0.75, c=1.0, d=1.0), term="high")
FS.add_linguistic_variable("CpuMem", LinguisticVariable([T_1, T_2, T_3], concept="Hardware Resources", universe_of_discourse=[0,1]))

R1 = []
R1.append("IF (ProcessorLoad IS high) AND (MemoryUsage IS high) THEN (CpuMem IS high)")
R1.append("IF (ProcessorLoad IS medium) AND (MemoryUsage IS high) THEN (CpuMem IS high)")
R1.append("IF (ProcessorLoad IS low) AND (MemoryUsage IS high) THEN (CpuMem IS high)")
R1.append("IF (ProcessorLoad IS high) AND (MemoryUsage IS medium) THEN (CpuMem IS high)")
R1.append("IF (ProcessorLoad IS medium) AND (MemoryUsage IS medium) THEN (CpuMem IS medium)")
R1.append("IF (ProcessorLoad IS low) AND (MemoryUsage IS medium) THEN (CpuMem IS medium)")
R1.append("IF (ProcessorLoad IS high) AND (MemoryUsage IS low) THEN (CpuMem IS high)")
R1.append("IF (ProcessorLoad IS medium) AND (MemoryUsage IS low) THEN (CpuMem IS medium)")
R1.append("IF (ProcessorLoad IS low) AND (MemoryUsage IS low) THEN (CpuMem IS low)")
FS.add_rules(R1)


# #### NETWORK USAGE ####

# ### Output Congestion ###

FS2 = FuzzySystem(show_banner=False)

# Output Net Throughput
OUT_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.3, d=0.5), term="low")
OUT_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
OUT_3 = FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.75, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutNetThroughput", LinguisticVariable([OUT_1, OUT_2, OUT_3], concept="Output Network Throughput", universe_of_discourse=[0,1]))

# Available Output Bandwidth
OB_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.3, d=0.5), term="low")
OB_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
OB_3 = FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.75, c=1.0, d=1.0), term="high")

FS2.add_linguistic_variable("AvailOutBandwidth", LinguisticVariable([OB_1, OB_2, OB_3], concept="Available Output Bandwidth", universe_of_discourse=[0,1]))

# Output Congestion
OC_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.5), term="low")
OC_2 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.6, c=0.70, d=0.8), term="medium")
OC_3 = FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.75, c=1.0, d=1.0), term="high")
FS2.add_linguistic_variable("OutCongestion", LinguisticVariable([OC_1, OC_2, OC_3], concept="Output Congestion", universe_of_discourse=[0,1]))

"""
  Output Bandwith Available
   ╭───┬───┬───┬───╮
N  │   │ L │ M │ H │
e  ├───┼───┼───┼───┤
t  │ L │ m │ l │ l │
   ├───┼───┼───┼───┤
t  │ M │ h │ m │ m │
h  ├───┼───┼───┼───┤
r  │ H │ h │ h │ h │
o  ╰───┴───┴───┴───╯
ughput
"""

R2 = []
R2.append("IF (OutNetThroughput IS low) AND (AvailOutBandwidth IS low) THEN (OutCongestion IS medium)")
R2.append("IF (OutNetThroughput IS medium) AND (AvailOutBandwidth IS low) THEN (OutCongestion IS high)")
R2.append("IF (OutNetThroughput IS high) AND (AvailOutBandwidth IS low) THEN (OutCongestion IS high)")
R2.append("IF (OutNetThroughput IS low) AND (AvailOutBandwidth IS medium) THEN (OutCongestion IS low)")
R2.append("IF (OutNetThroughput IS medium) AND (AvailOutBandwidth IS medium) THEN (OutCongestion IS medium)")
R2.append("IF (OutNetThroughput IS high) AND (AvailOutBandwidth IS medium) THEN (OutCongestion IS high)")
R2.append("IF (OutNetThroughput IS low) AND (AvailOutBandwidth IS high) THEN (OutCongestion IS low)")
R2.append("IF (OutNetThroughput IS medium) AND (AvailOutBandwidth IS high) THEN (OutCongestion IS medium)")
R2.append("IF (OutNetThroughput IS high) AND (AvailOutBandwidth IS high) THEN (OutCongestion IS high)")
FS2.add_rules(R2)


# #### COMPUTING LOAD PERCENTAGE (CLP) ####

FS_CLP = FuzzySystem(show_banner=False)

L_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.5, d=0.7), term="low")
L_3 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.5, c=1, d=1), term="high")
FS_CLP.add_linguistic_variable("Latency", LinguisticVariable([L_1, L_3], concept="Latency", universe_of_discourse=[0,1]))
FS_CLP.add_linguistic_variable("CpuMem", LinguisticVariable([T_1, T_2, T_3], concept="Hardware Resources", universe_of_discourse=[0,1]))
FS_CLP.add_linguistic_variable("OutCongestion", LinguisticVariable([OC_1, OC_2, OC_3], concept="Output Congestion", universe_of_discourse=[0,1]))


IN_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.5, d=0.7), term="low")
IN_3 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.5, c=1.0, d=1.0), term="high")
FS_CLP.add_linguistic_variable("InpNetThroughput", LinguisticVariable([IN_1, IN_3], concept="Input Network Throughput", universe_of_discourse=[0,1]))


CLP_1 = FuzzySet(function=Trapezoidal_MF(a=-1, b=-1, c=-0.75, d=-0.5), term="decrease_much")
CLP_2 = FuzzySet(function=Trapezoidal_MF(a=-0.75, b=-0.5, c=-0.2, d=0), term="decrease")
CLP_3 = FuzzySet(function=Trapezoidal_MF(a=-0.2, b=-0.1, c=0.1, d=0.2), term="mantain")
CLP_4 = FuzzySet(function=Trapezoidal_MF(a=0, b=0.2, c=0.5, d=0.75), term="increase")
CLP_5 = FuzzySet(function=Trapezoidal_MF(a=0.5, b=0.75, c=1, d=1), term="increase_much")
FS_CLP.add_linguistic_variable("CLP", LinguisticVariable([CLP_1, CLP_2, CLP_3, CLP_4, CLP_5], concept="CLP Variation", universe_of_discourse=[-1,1]))

"""
   Netowrk Congestion
   ╭─────┬─────┬─────┬─────╮
C  │     │  L  │  M  │  H  │
p  ├─────┼─────┼─────┼─────┤
u  │  L  │ ↑↑  │ ↑↑  │ ↑↑  │
M  ├─────┼─────┼─────┼─────┤
e  │  M  │  ↑  │  ↑  │  ↓  │
m  ├─────┼─────┼─────┼─────┤
   │  H  │ ↓↓  │  ↓  │  ↓  │
   ╰─────┴─────┴─────┴─────╯
"""

# Rules
RC = []

RC.append("IF (CpuMem IS low) THEN CLP IS increase_much")
RC.append("IF (CpuMem IS high) AND (OutCongestion IS low) THEN CLP IS decrease_much")
RC.append("IF (CpuMem IS high) AND (OutCongestion IS medium) THEN CLP IS decrease")
RC.append("IF (CpuMem IS high) AND (OutCongestion IS high) THEN CLP IS decrease")
RC.append("IF (CpuMem IS medium) AND (OutCongestion IS low) THEN CLP IS increase")
RC.append("IF (CpuMem IS medium) AND (OutCongestion IS medium) THEN CLP IS increase") # faz-me sentido ser manter, mas pelos testes não?
RC.append("IF (CpuMem IS medium) AND (OutCongestion IS high) THEN CLP IS increase")

FS_CLP.add_rules(RC)

SHOW_3D = True
SHOW_2D = False
LOGGING_LEVEL = logging.INFO
# LOGGING_LEVEL = logging.DEBUG

if __name__ == '__main__':
    df = pd.read_csv(DATASET_PATH)
    logging.basicConfig(level=LOGGING_LEVEL, format='%(levelname)s: %(message)s')

    if SHOW_3D:
        fig = FS.plot_surface(variables=['ProcessorLoad','MemoryUsage'], output='CpuMem')
        fig2 = FS2.plot_surface(variables=['OutNetThroughput','AvailOutBandwidth'], output='OutCongestion')
        fig4 = FS_CLP.plot_surface(variables=['CpuMem','OutCongestion'], output='CLP')

    if SHOW_2D:
        FS.plot_variable("ProcessorLoad")
        FS.plot_variable("MemoryUsage")
        FS2.plot_variable("OutNetThroughput")
        FS2.plot_variable("AvailOutBandwidth")
        FS2.plot_variable("OutCongestion")
        FS_CLP.plot_variable("CpuMem")
        FS_CLP.plot_variable("OutCongestion")
        FS_CLP.plot_variable("CLP")


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
        cpu_mem = FS.Mamdani_inference()['CpuMem']

        FS2.set_variable("OutNetThroughput", output_throughput)
        FS2.set_variable("AvailOutBandwidth", output_available_bandwidth)
        out_congestion = FS2.Mamdani_inference()["OutCongestion"]

        FS_CLP.set_variable("Latency", latency)
        FS_CLP.set_variable("InpNetThroughput", input_throughput)
        FS_CLP.set_variable("CpuMem", cpu_mem)
        FS_CLP.set_variable("OutCongestion", out_congestion)
        clp = FS_CLP.Mamdani_inference()["CLP"]

        logging.debug(f"CPU: {process_load}; Mem: {memory_usage}; {cpu_mem}")
        logging.debug(f"OutThroughput: {output_throughput}; OutBandAvail: {output_available_bandwidth}; {out_congestion}")
        logging.info(f"Predicted CLP: {int(round(clp, 2)*100)}%; Expected CLP: {int(clp_variation*100)}%")
