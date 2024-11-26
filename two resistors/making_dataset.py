import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

import time

import pandas as pd

start_time = time.time()

N = 4
broken_1 = 'V22'
broken_2 = 'V13'

# Initialize the circuit
circuit = Circuit('6x6 Resistor Grid')

# Function to get node name
def node_name(i, j):
    return f'N{i}{j}'

# Define resistors for the grid
resistance = 1@u_kOhm

df = pd.DataFrame()

def making_circuit(broken_1, broken_2, n):

    broken = broken_1 + broken_2

    # Add voltage source
    circuit.V(broken, node_name(1, 1)+broken, circuit.gnd, 10@u_V)  # 10V at top-left corner

    # Create a nxn grid of resistors
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Horizontal resistors
            if j < n:
                if broken_1 == f'H{i}{j}' or broken_2 == f'H{i}{j}':
                    circuit.R(f'H{i}{j}'+broken, node_name(i, j)+broken, node_name(i, (j+1))+broken, 0@u_uOhm)
                else:
                    circuit.R(f'H{i}{j}'+broken, node_name(i, j)+broken, node_name(i, (j+1))+broken, resistance)
            # Vertical resistors
            if i < n:
                if broken_1 == f'V{i}{j}' or broken_2 == f'V{i}{j}':
                    circuit.R(f'V{i}{j}'+broken, node_name(i, j)+broken, node_name((i+1), j)+broken, 0@u_uOhm)
                else:
                    circuit.R(f'V{i}{j}'+broken, node_name(i, j)+broken, node_name((i+1), j)+broken, resistance)

    # Ground the bottom-right corner
    circuit.R(f'GRD'+broken, node_name(n, n)+broken, circuit.gnd, 0@u_uOhm)  # Using a very low resistance to simulate ground connection

    # Define the simulator and run a DC analysis
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.operating_point()

    # # Print the circuit
    # print("The Circuit/Netlist:\n\n", circuit)

    data = []

    # Print the node voltages using double for loops
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n or j == 1 or j == n:
                node = node_name(i, j)+broken
                voltage = float(analysis[node].as_ndarray()[0])
                print('Node {}: {:4.1f} V'.format(node, voltage))
                data.append([i, j, voltage])              

    df1 = pd.DataFrame(data, columns=['X', 'Y', 'voltage'])

    df[broken] = df1['voltage']


def all_resistors(n):
    data = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            # horizontal
            if j < n:
                data.append([f'H{i}{j}', i, (j+0.5)])
            if i < n:
                data.append([f'V{i}{j}', (i+0.5), j])
    data.append(['', 0, 0])
    list = pd.DataFrame(data, columns=['name', 'X', 'Y'])
    # print(list['X'])
    list.index = list['name']
    # list = list.rename(index={'row2': 'new_row2'})
    return list


list = all_resistors(N)
# print(list)

# print(list['name'])
# print(list['X'])

# for i in list['name']:
#     # print(i)
#     making_circuit(i, N)
#     # print("something")


making_circuit(broken_1, broken_2, N)

df = df.transpose()
df['X'] = list['X']
df['Y'] = list['Y']

# print(df)







# # # saving data

path = 'two resistors/datasets/'
df.to_csv(path+'grid_'+broken_1+'_'+broken_2+'_nodes.csv', index=False)
print("Data saved to csv file.")



# # # print how much time the run took

end_time = time.time()
execution_time = end_time - start_time
print("time run:", execution_time)