import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import * # meaning for example selecting ohm for a resistor

V = 10@u_V
R = 1@u_kOhm
n = 4

# # making a delta network circuit
# # run an operating point analysis

# Create the circuit
circuit = Circuit('Delta Network Circuit')

'''
  1 -  2 -  3 -  4
  5 -  6 -  7 -  8
  9 - 10 - 11 - 12
 13 - 14 - 15 - 16
'''

# # Add components to the circuit
# circuit.V('input', 'B', circuit.gnd, V)  # Voltage source
# circuit.R(1, 'B', circuit.gnd, R1) # Resistor 1
# circuit.R(2, 'B', 'C', R2) # Resistor 2
# circuit.R(3, 'C', circuit.gnd, R3) # Resistor 3

circuit.V('input', 'A', 'G', V)  # Voltage source
circuit.R(1, 'A', 'B', R) # Resistor 1
circuit.R(2, 'B', 'C', R) # Resistor 2
circuit.R(3, 'C', 'D', R) # Resistor 3
circuit.R(4, 'A', 'L', R) # Resistor 4
circuit.R(5, 'B', '1', R) # Resistor 5
circuit.R(6, 'C', '2', R) # Resistor 6
circuit.R(7, 'D', 'E', R) # Resistor 7
circuit.R(8, 'L', '1', R) # Resistor 8
circuit.R(9, '1', '2', R) # Resistor 9
circuit.R(10, '2', 'E', R) # Resistor 10
circuit.R(11, 'L', 'K', R) # Resistor 11
circuit.R(12, '1', '3', R) # Resistor 12
circuit.R(13, '2', '4', R) # Resistor 13
circuit.R(14, 'E', 'F', R) # Resistor 14
circuit.R(15, 'K', '3', R) # Resistor 15
circuit.R(16, '3', '4', R) # Resistor 16
circuit.R(17, '4', 'F', R) # Resistor 17
circuit.R(18, 'K', 'J', R) # Resistor 18
circuit.R(19, '3', 'I', R) # Resistor 19
circuit.R(20, '4', 'H', R) # Resistor 20
circuit.R(21, 'F', 'G', R) # Resistor 21
circuit.R(22, 'J', 'I', R) # Resistor 22
circuit.R(23, 'I', 'H', R) # Resistor 23
circuit.R(24, 'H', 'G', R) # Resistor 24

# Create a simulator object
simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)

# Print the circuit
# print("The Circuit/Netlist:\n\n", circuit)

# Run analysis
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print('Node {}: {:4.1f} V'.format(str(node), float(node))) # Fixme: format value + unit


print('Node {} - {}: {:4.1f} V'.format(str(analysis.A), str(analysis.B), float(analysis.A) - float(analysis.B))) # A - B
print('Node {} - {}: {:4.1f} V'.format(str(analysis.B), str(analysis.C), float(analysis.B) - float(analysis.C))) # B - C
print('Node {} - {}: {:4.1f} V'.format(str(analysis.C), str(analysis.D), float(analysis.C) - float(analysis.D))) # C - D
print('Node {} - {}: {:4.1f} V'.format(str(analysis.D), str(analysis.E), float(analysis.D) - float(analysis.E))) # D - E
print('Node {} - {}: {:4.1f} V'.format(str(analysis.E), str(analysis.F), float(analysis.E) - float(analysis.F))) # E - F
print('Node {} - {}: {:4.1f} V'.format(str(analysis.F), str(analysis.G), float(analysis.F) - float(analysis.G))) # F - G
print('Node {} - {}: {:4.1f} V'.format(str(analysis.G), str(analysis.H), float(analysis.G) - float(analysis.H))) # G - H
print('Node {} - {}: {:4.1f} V'.format(str(analysis.H), str(analysis.I), float(analysis.H) - float(analysis.I))) # H - I
print('Node {} - {}: {:4.1f} V'.format(str(analysis.I), str(analysis.J), float(analysis.I) - float(analysis.J))) # I - J
print('Node {} - {}: {:4.1f} V'.format(str(analysis.J), str(analysis.K), float(analysis.J) - float(analysis.K))) # J - K
print('Node {} - {}: {:4.1f} V'.format(str(analysis.K), str(analysis.L), float(analysis.K) - float(analysis.L))) # K - L
print('Node {} - {}: {:4.1f} V'.format(str(analysis.L), str(analysis.A), float(analysis.L) - float(analysis.A))) # L - A