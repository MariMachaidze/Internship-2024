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

N = 10

# Initialize the circuit
circuit = Circuit('4x4 Resistor Grid')

# Function to get node name
def node_name(i, j):
    return f'N{i}{j}'


# Define resistors for the grid
resistance = 1@u_kOhm

# broken = 'V22'

df = pd.DataFrame()

mari_df = pd.DataFrame()

def making_circuit(broken, n):

    # Add voltage source
    circuit.V(broken, node_name(0, 0)+broken, circuit.gnd, 10@u_V)  # 10V at top-left corner

    # Create a nxn grid of resistors
    for i in range(n):
        for j in range(n):
            # Horizontal resistors
            if j < n-1:
                if broken == f'H{i}{j}':
                    circuit.R(f'H{i}{j}'+broken, node_name(i, j)+broken, node_name(i, j+1)+broken, 0@u_uOhm)
                else:
                    circuit.R(f'H{i}{j}'+broken, node_name(i, j)+broken, node_name(i, j+1)+broken, resistance)
            # Vertical resistors
            if i < n-1:
                if broken == f'V{i}{j}':
                    circuit.R(f'V{i}{j}'+broken, node_name(i, j)+broken, node_name(i+1, j)+broken, 0@u_uOhm)
                else:
                    circuit.R(f'V{i}{j}'+broken, node_name(i, j)+broken, node_name(i+1, j)+broken, resistance)

    # Ground the bottom-right corner
    circuit.R(f'GRD'+broken, node_name(n-1, n-1)+broken, circuit.gnd, 0@u_uOhm)  # Using a very low resistance to simulate ground connection

    # Define the simulator and run a DC analysis
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.operating_point()

    # # Print the circuit
    # print("The Circuit/Netlist:\n\n", circuit)

    # # Print the node voltages using double for loops
    # for i in range(4):
    #     for j in range(4):
    #         node = node_name(i, j)+broken
    #         voltage = float(analysis[node].as_ndarray()[0])
    #         print('Node {}: {:4.1f} V'.format(node, voltage))

    # # # perimeter
    data = []
    data_voltage = []

    # for i in range(n):
    #     for j in range(n):
    #         # print('i, j: {}, {}'.format(i, j))
    #         # Horizontal resistors
    #         if j < n - 1 and (i == 0 or i == n - 1):
    #             # print('i, j: {}, {}'.format(i, j), f'H{i}{j}')
    #             node1 = node_name(i, j)+broken
    #             node2 = node_name(i, j+1)+broken
    #             voltage1 = float(analysis[node1].as_ndarray()[0])
    #             voltage2 = float(analysis[node2].as_ndarray()[0])
    #             voltage = voltage1 - voltage2
    #             data.append([i, j, i, j+1, voltage])   
    #         # Vertical resistors
    #         if i < n - 1 and (j == 0 or j == n - 1):
    #             # print('i, j: {}, {}'.format(i, j), f'V{i}{j}')
    #             node1 = node_name(i, j)+broken
    #             node2 = node_name(i+1, j)+broken
    #             voltage1 = float(analysis[node1].as_ndarray()[0])
    #             voltage2 = float(analysis[node2].as_ndarray()[0])
    #             voltage = voltage1 - voltage2
    #             data.append([i, j, i, j+1, voltage]) 

    # print(data) # print perimeter data

    # # columns and rows

    for i in range(n):
        # print('i, j: {}, {}'.format(i, j))
        # Horizontal resistors
        node1 = node_name(0, i)+broken
        node2 = node_name(n-1, i)+broken
        voltage1 = float(analysis[node1].as_ndarray()[0])
        voltage2 = float(analysis[node2].as_ndarray()[0])
        voltage = voltage1 - voltage2
        data.append([0, i, n-1, i, voltage])
        data_voltage.append(voltage)
        # Vertical resistors
        node1 = node_name(i, 0)+broken
        node2 = node_name(i, n-1)+broken
        voltage1 = float(analysis[node1].as_ndarray()[0])
        voltage2 = float(analysis[node2].as_ndarray()[0])
        voltage = voltage1 - voltage2
        data.append([i, 0, i, n-1, voltage])
        data_voltage.append(voltage)

    # print(data) # print perimeter data


    df1 = pd.DataFrame(data, columns=['N1X', 'N1Y', 'N2X', 'N2Y', 'voltage'])

    # mari_df = df1
    # print(mari_df, "hello??")
    return df1

    df = pd.DataFrame(data_voltage)
# This needs to be corrected

def all_resistors(n):
    data = []
    for i in range(n):
        for j in range(n):
            # horizontal
            if j < n-1:
                data.append([f'H{i}{j}', i, j+0.5])
            if i < n-1:
                data.append([f'V{i}{j}', i+0.5, j])
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


mari_df = making_circuit("V66", N)

print(mari_df)

# df = df.transpose()
# df['X'] = list['X']
# df['Y'] = list['Y']

# print(df)




path = 'C:\\Users\\marim\\Desktop\\summer 2024 projects\\internship 2024\\neural network part\\'
# C:\Users\marim\Desktop\summer 2024 projects\internship 2024\neural network part

# Save DataFrame to a excel file
mari_df.to_csv(path+'datasetV66cr.csv', index=False) #'+str(N)+'


# Optionally, display a message
print("Data saved to csv file.")


end_time = time.time()

execution_time = end_time - start_time
print("time run:", execution_time)