import pandas as pd
import matplotlib.pyplot as plt
from simpful import *

DATASET_PATH = 'CI4IoT23-24_Proj1_SampleData.csv'

# TODO: Remove this line https://github.com/aresio/simpful/tree/master/examples

# Create a fuzzy system
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
PL_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=0.6), term="low")
PL_2 = FuzzySet(function=Triangular_MF(a=0.5, b=0.65, c=0.8), term="medium")
PL_3 = FuzzySet(function=Triangular_MF(a=0.7, b=0.8, c=1.0), term="high")
FS.add_linguistic_variable("ProcessorLoad", LinguisticVariable([PL_1, PL_2, PL_3], concept="Processor Load", universe_of_discourse=[0,1]))

MU_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=0.6), term="low")
MU_2 = FuzzySet(function=Triangular_MF(a=0.5, b=0.65, c=0.8), term="medium")
MU_3 = FuzzySet(function=Triangular_MF(a=0.7, b=0.8, c=1.0), term="high")
FS.add_linguistic_variable("MemoryUsage", LinguisticVariable([MU_1, MU_2, MU_3], concept="Memory Usage", universe_of_discourse=[0,1]))

T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=0.6), term="low")
T_2 = FuzzySet(function=Triangular_MF(a=0.5, b=0.65, c=0.8), term="medium")
T_3 = FuzzySet(function=Triangular_MF(a=0.7, b=0.8, c=1.0), term="high")
FS.add_linguistic_variable("Action", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0,1]))

# Define fuzzy rules
R1 = "IF (ProcessorLoad IS high) OR (MemoryUsage IS high) THEN (Action IS high)"
R2 = "IF (ProcessorLoad IS medium) OR (MemoryUsage IS medium) THEN (Action IS medium)"
R3 = "IF (ProcessorLoad IS low) OR (MemoryUsage IS low) THEN (Action IS low)"
FS.add_rules([R1, R2, R3])

if __name__ == '__main__':
    df = pd.read_csv(DATASET_PATH)

    time = [0]
    memory_usage_plot = []
    process_load_plot = []
    action_plot = []

    for index, row in df.iterrows():
        time.append(time[-1] + 1)
        memory_usage = row['MemoryUsage']
        process_load = row['ProcessorLoad']
        # Set antecedents values
        FS.set_variable("ProcessorLoad", process_load)
        FS.set_variable("MemoryUsage", memory_usage)
        # Evaluate the system
        #print(FS.Mamdani_inference(["Action"]))
        action = FS.Mamdani_inference(["Action"])
        memory_usage_plot.append(memory_usage)
        process_load_plot.append(process_load)
        action_plot.append(action['Action'])

        print(f"CPU: {process_load}; Mem: {memory_usage}; {action['Action']}")

    plt.plot(time[1:], memory_usage_plot, label='Memory Usage')
    plt.plot(time[1:], process_load_plot, label='Processor Load')
    plt.plot(time[1:], action_plot, label='Action')

    plt.show()
