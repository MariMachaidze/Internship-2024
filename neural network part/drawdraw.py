import matplotlib.pyplot as plt

# Coordinates and corresponding values from the image
coordinates = [(0, 0), (1, 0), (2, 0), (3, 0),  # Bottom row
               (0, 1), (3, 1),                  # Middle row
               (0, 2), (3, 2),                  # Middle row
               (0, 3), (1, 3), (2, 3), (3, 3)]  # Top row

values = [None, None, None, 10,                 # Bottom row
          None, 4.67,                           # Middle row
          None, 2.43,                           # Middle row
          4.07, 0.9, -1.32, -4.4]               # Top row

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the points
for i, (x, y) in enumerate(coordinates):
    if values[i] is not None:
        ax.scatter(x, y, color='black')   # Plot the point
        ax.text(x, y, str(values[i]), fontsize=12, ha='center', va='bottom')  # Annotate with value
    else:
        ax.scatter(x, y, color='black')   # Just the point without value

# Set limits and labels
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 3.5)
ax.set_xticks([])
ax.set_yticks([])

# Arrows for indication
ax.annotate('', xy=(0, 0), xytext=(-0.5, 0), arrowprops=dict(facecolor='black', arrowstyle='->'))
ax.annotate('', xy=(3, 0), xytext=(3.5, 0), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display the plot
plt.gca().invert_yaxis()  # Invert the y-axis to match the whiteboard image
plt.show()
