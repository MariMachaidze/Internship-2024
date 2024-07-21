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

broken = 'H11'

# Create a 4x4 grid of resistors
for i in range(4):
    for j in range(4):
        # Horizontal resistors
        if j < 3:
            if broken == f'H{i}{j}':
                circuit.R(f'H{i}{j}', node_name(i, j), node_name(i, j+1), 0@u_uOhm)
            else:
                circuit.R(f'H{i}{j}', node_name(i, j), node_name(i, j+1), resistance)
        # Vertical resistors
        if i < 3:
            if broken == f'V{i}{j}':
                circuit.R(f'V{i}{j}', node_name(i, j), node_name(i+1, j), 0@u_uOhm)
            else:
                circuit.R(f'V{i}{j}', node_name(i, j), node_name(i+1, j), resistance)

# Ground the bottom-right corner
circuit.R(f'GRD', node_name(3, 3), circuit.gnd, 0@u_uOhm)  # Using a very low resistance to simulate ground connection

# Define the simulator
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

# Print the circuit
# print("The Circuit/Netlist:\n\n", circuit)

data = []

# Print the node voltages using double for loops
for i in range(4):
    for j in range(4):
        node = node_name(i, j)
        voltage = float(analysis[node].as_ndarray()[0])
        print('Node {}: {:4.1f} V'.format(node, voltage)) #:4.1f
        data.append([node, voltage])


df = pd.DataFrame(data, columns=['node', 'voltage'])

path = 'C:\\Users\\marim\\Desktop\\summer 2024 projects\\internship 2024\\data\\'

# # Save DataFrame to a excel file
df.to_csv(path+'BrokenH11_Voltage.csv', index=False)

# # Optionally, display a message
print("Data saved to csv file.")
