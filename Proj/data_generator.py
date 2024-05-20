import csv
import random

headers = 'MemoryUsage,ProcessorLoad,InpNetThroughput,OutNetThroughput,OutBandwidth,Latency,V_MemoryUsage,V_ProcessorLoad,V_InpNetThroughput,V_OutNetThroughput,V_OutBandwidth,V_Latency'.split(',')


with open('data/data_10_rng.csv', 'w', newline='') as file:
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


with open('data_rng_v2.csv', 'w', newline='') as file:
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

