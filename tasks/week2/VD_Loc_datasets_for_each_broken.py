import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

import pandas as pd

# Initialize the circuit
circuit = Circuit('4x4 Resistor Grid')

# Function to get node name
def node_name(i, j):
    return f'N{i}{j}'

# Add voltage source
circuit.V(1, node_name(0, 0), circuit.gnd, 10@u_V)  # 10V at top-left corner

# Define resistors for the grid
resistance = 1@u_kΩ

broken = 'V22'

# Create a 4x4 grid of resistors
for i in range(4):
    for j in range(4):
        # Horizontal resistors
        if j < 3:
            if broken == f'H{i}{j}':
                circuit.R(f'H{i}{j}', node_name(i, j), node_name(i, j+1), 0@u_uOhm)
                print("yes",i,j,i,j+1)
            else:
                circuit.R(f'H{i}{j}', node_name(i, j), node_name(i, j+1), resistance)
        # Vertical resistors
        if i < 3:
            if broken == f'V{i}{j}':
                circuit.R(f'V{i}{j}', node_name(i, j), node_name(i+1, j), 0@u_uOhm)
                print("yes")
            else:
            # print(i, j, 'V')
                circuit.R(f'V{i}{j}', node_name(i, j), node_name(i+1, j), resistance)

# Ground the bottom-right corner
circuit.R(f'GRD', node_name(3, 3), circuit.gnd, 0@u_uOhm)  # Using a very low resistance to simulate ground connection

# Define the simulator and run a DC analysis
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

# Print the circuit
# print("The Circuit/Netlist:\n\n", circuit)


# Print the node voltages using double for loops
for i in range(4):
    for j in range(4):
        node = node_name(i, j)
        voltage = float(analysis[node].as_ndarray()[0])
        # print('Node {}: {:4.1f} V'.format(node, voltage)) #:4.1f

n = 0
data = []
data_broken = []

for i in range(4):
    for j in range(4):
        # print('i, j: {}, {}'.format(i, j))
        # Horizontal resistors
        if j < 3 and (i == 0 or i == 3):
            num = 1*100 + i*10 + j
            # print('i, j: {}, {}'.format(i, j), f'H{i}{j}')
            node1 = node_name(i, j)
            node2 = node_name(i, j+1)
            voltage1 = float(analysis[node1].as_ndarray()[0])
            voltage2 = float(analysis[node2].as_ndarray()[0])
            voltage = voltage1 - voltage2
            # data.append([f'H{i}{j}', num, voltage])           
            data.append([num, voltage])
            # n += 1
        else:
            num = 1*100 + i*10 + j
            data_broken.append([f'H{i}{j}', num])
        # Vertical resistors
        if i < 3 and (j == 0 or j == 3):
            num = 2*100 + i*10 + j
            # print('i, j: {}, {}'.format(i, j), f'V{i}{j}')
            node1 = node_name(i, j)
            node2 = node_name(i+1, j)
            voltage1 = float(analysis[node1].as_ndarray()[0])
            voltage2 = float(analysis[node2].as_ndarray()[0])
            voltage = voltage1 - voltage2
            # data.append([f'V{i}{j}', num, voltage])
            data.append([num, voltage])
            # n += 1
        else:
            num = 2*100 + i*10 + j
            data_broken.append([f'V{i}{j}', num])

print(data)

print(data_broken)

# df = pd.DataFrame(data, columns=['resistor', 'location', 'voltage'])
df = pd.DataFrame(data, columns=['location', 'voltage'])

df1 = pd.DataFrame(data_broken, columns=['resistor', 'location'])


path = 'C:\\Users\\marim\\Desktop\\summer 2024 projects\\internship 2024\\data\\datasets\\'

# # Save DataFrame to a excel file
df.to_csv(path+'Broken_VDLoc'+broken+'.csv', index=False)
df1.to_csv(path+'Broken_dataset.csv', index=False)


# # Optionally, display a message
print("Data saved to csv file.")
