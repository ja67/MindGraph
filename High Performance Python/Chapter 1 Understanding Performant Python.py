import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files (x86)\Graphviz2.38\bin\dot.exe"
from graphviz import Digraph

Chapter1 = Digraph(comment='The Fundamental Computer System')
# Computer System
Chapter1.node("Computer System", "Computer System")

Chapter1.node("Computing Units", "Computing Units")
Chapter1.node("Memory Units", "Memory Units")
Chapter1.node("Communication Layers", "Communication Layers")

Chapter1.edge("Computer System", "Computing Units")
Chapter1.edge("Computer System", "Memory Units")
Chapter1.edge("Computer System", "Communication Layers")

# Computing Units
Chapter1.node("IPC", "Instructions per cycle(IPC)")
Chapter1.node("Clock Speed", "Clock Speed")
Chapter1.node("Vectorization", "Vectorization(SIMD)")
Chapter1.node("Hyperthreading", "Hyperthreading")
Chapter1.node("Out-of-order execution", "Out-of-order execution")
Chapter1.node("Multicore", "Multicore")
Chapter1.node("Amdahl's Law", "Amdahl's Law")
Chapter1.node("GIL", "Global Interpreter Lock(GIL)")

Chapter1.edge("Computing Units", "IPC")
Chapter1.edge("Computing Units", "Clock Speed")
Chapter1.edge("Computing Units", "Vectorization")
Chapter1.edge("Computing Units", "Hyperthreading")
Chapter1.edge("Computing Units", "Out-of-order execution")
Chapter1.edge("Computing Units", "Multicore")
Chapter1.edge("Multicore", "Amdahl's Law")
Chapter1.edge("Multicore", "GIL")

# Memory Units
Chapter1.node("Sequential Read/Random Read", "Sequential Read/Random Read")
Chapter1.node("Latency", "Latency")
Chapter1.node("Type", "Type")
Chapter1.node("HDD", "Spinning Hard Drive")
Chapter1.node("SSD", "Solid State Drive")
Chapter1.node("RAM", "RAM")
Chapter1.node("Cache", "L1/L2 Cache")

Chapter1.edge('Memory Units', "Sequential Read/Random Read")
Chapter1.edge('Memory Units', "Latency")
Chapter1.edge('Memory Units', "Type")
Chapter1.edge('Type', "HDD")
Chapter1.edge('Type', "SSD")
Chapter1.edge('Type', "RAM")
Chapter1.edge('Type', "Cache")

# Communication Layers
Chapter1.node('Bus', 'Bus')
Chapter1.node('Frontside Bus')
Chapter1.node('External Bus')
Chapter1.node('Network')
Chapter1.node('Bus Width')
Chapter1.node('Bus Frequency')

Chapter1.edge("Communication Layers", "Bus")
Chapter1.edge("Communication Layers", "Network")
Chapter1.edge("Bus", "Frontside Bus")
Chapter1.edge("Bus", "External Bus")
Chapter1.edge("Bus", "Bus Width")
Chapter1.edge("Bus", "Bus Frequency")



print(Chapter1.source)
Chapter1.view('Chapter 1 Understanding Performant Python.gv')
