import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = 'C:\\Users\\marim\\Desktop\\summer 2024 projects\\internship 2024\\neural network part\\'
df = pd.read_csv(path + 'datasetV66cr.csv')  ## H01 example

# Extract the coordinates and the voltage columns from the DataFrame
N1X = df['N1X']
N1Y = df['N1Y']
N2X = df['N2X']
N2Y = df['N2Y']
voltages = df['voltage']

# Function to plot the grid with measured voltages
def plot_grid(values, title, ax):
    ax.set_title(title)
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    
    for i in range(len(N1X)):
        # Plot the nodes and connect them with a line
        ax.plot([N1X[i], N2X[i]], [N1Y[i], N2Y[i]], 'bo-', alpha=0.6)
        
        # Annotate the plot with the voltage values
        mid_x = (N1X[i] + N2X[i]) / 2
        mid_y = (N1Y[i] + N2Y[i]) / 2
        ax.text(mid_x, mid_y, f"{values[i]:.3f}", color='red', fontsize=10, ha='center', va='center')

    # Flip y-axis so that the upper-left corner is the origin
    ax.invert_yaxis()
    ax.grid(True)

# Create a plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot measured voltages
plot_grid(voltages, "Measured Voltages", ax)

# Show the plot
plt.tight_layout()
plt.show()