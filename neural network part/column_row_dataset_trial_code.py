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

# Initialize the circuit
circuit = Circuit('4x4 Resistor Grid')

# Function to get node name
def node_name(i, j):
    return f'N{i}{j}'


# Define resistors for the grid
resistance = 1@u_kOhm

broken = 'V12'

df = pd.DataFrame()

mari_df = pd.DataFrame()

def making_circuit(broken, n, X1, Y1, X2, Y2, a):
    print(X1, Y1, X2, Y2, a)
    name = str(a)

    # Add voltage source
    circuit.V(name, node_name(X1, Y1)+name, circuit.gnd, 10@u_V)  # 10V at top-left corner

    # Create a nxn grid of resistors
    for i in range(n):
        for j in range(n):
            # Horizontal resistors
            if j < n-1:
                if broken == f'H{i}{j}':
                    circuit.R(f'H{i}{j}'+name, node_name(i, j)+name, node_name(i, j+1)+name, 0@u_uOhm)
                else:
                    circuit.R(f'H{i}{j}'+name, node_name(i, j)+name, node_name(i, j+1)+name, resistance)
            # Vertical resistors
            if i < n-1:
                if broken == f'V{i}{j}':
                    circuit.R(f'V{i}{j}'+name, node_name(i, j)+name, node_name(i+1, j)+name, 0@u_uOhm)
                else:
                    circuit.R(f'V{i}{j}'+name, node_name(i, j)+name, node_name(i+1, j)+name, resistance)

    # Ground the bottom-right corner
    circuit.R(f'GRD'+name, node_name(X2, Y2)+name, circuit.gnd, 0@u_uOhm)  # Using a very low resistance to simulate ground connection

    # Define the simulator and run a DC analysis
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.operating_point()

    data = []
    data_voltage = []

    # # columns and rows

    for i in range(n):
        # print('i, j: {}, {}'.format(i, j))
        # Horizontal resistors
        node1 = node_name(0, i)+name
        node2 = node_name(n-1, i)+name
        voltage1 = float(analysis[node1].as_ndarray()[0])
        voltage2 = float(analysis[node2].as_ndarray()[0])
        voltage = voltage1 - voltage2
        # if(abs(voltage) < 0.00001):
        #     voltage = 0
        print(0, i, voltage1, n-1 , i, voltage2, voltage)
        data.append([0, i, n-1, i, voltage])
        data_voltage.append(voltage)
        # Vertical resistors
        node1 = node_name(i, 0)+name
        node2 = node_name(i, n-1)+name
        voltage1 = float(analysis[node1].as_ndarray()[0])
        voltage2 = float(analysis[node2].as_ndarray()[0])
        voltage = voltage1 - voltage2
        # if(abs(voltage) < 0.00001):
        #     voltage = 0
        print(i, 0, voltage1, i, n-1, voltage2, voltage)
        data.append([i, 0, i, n-1, voltage])
        data_voltage.append(voltage)

    print()
    # print(data) # print perimeter data


    df1 = pd.DataFrame(data, columns=['N1X', 'N1Y', 'N2X', 'N2Y', 'voltage'])

    # mari_df = df1
    # print(mari_df, "hello??")

    df[name] = pd.DataFrame(data_voltage)
    # print(df)

    return df1

resistors = [(0, 0, 3, 3),
             (0, 0, 0, 3),
             (1, 0, 1, 3),
             (2, 0, 2, 3),
             (3, 0, 3, 3),
             (0, 0, 3, 0),
             (0, 1, 3, 1),
             (0, 2, 3, 2),
             (0, 3, 3, 3),]

a=0
for i in resistors:
    a += 1
    mari_df = making_circuit(broken, N, i[0], i[1], i[2], i[3], a)

    
# df = df.transpose()
print(df)

print(mari_df)


path = 'C:\\Users\\marim\\Desktop\\summer 2024 projects\\internship 2024\\neural network part\\'
# C:\Users\marim\Desktop\summer 2024 projects\internship 2024\neural network part

# Save DataFrame to a excel file
# mari_df.to_csv(path+broken+'_2_cr.csv', index=False) #'+str(N)+'
df.to_csv(path+broken+'__cr.csv', index=False) #'+str(N)+'


# Optionally, display a message
print("Data saved to csv file.")


end_time = time.time()

execution_time = end_time - start_time
print("time run:", execution_time)