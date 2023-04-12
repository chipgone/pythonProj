# Imports (albeit math is not used, it could be useful for the user for more complex functions)
import math
import tkinter as tk

# Function to plot (could make it editable by user later using input)
def f(x):
    return x**2 # A parabola as an example

# Range of x-values to plot
x_min = -10
x_max = 10
num_points = 1000

# Making a list of x-values
x_values = []
for i in range(num_points):
    x_values.append(x_min + i * (x_max - x_min) / (num_points - 1))

# Making a list of y-values
y_values = []
for x in x_values:
    y_values.append(f(x))

# Min and max y-values (for scaling)
y_min = min(y_values)
y_max = max(y_values)

# Defining the size and position of the window/GUI and creating it
window_width = 800
window_height = 600
window_x = 100
window_y = 100
root = tk.Tk()
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
root.title("Function Plotting")

# Create the canvas for the plot
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
canvas.pack(fill="both", expand=True)

# Plot the function
for i in range(num_points - 1):
    x1 = (x_values[i] - x_min) * window_width / (x_max - x_min)
    x2 = (x_values[i+1] - x_min) * window_width / (x_max - x_min)
    y1 = (y_values[i] - y_min) * window_height / (y_max - y_min)
    y2 = (y_values[i+1] - y_min) * window_height / (y_max - y_min)
    canvas.create_line(x1, window_height - y1, x2, window_height - y2, width=2)

root.mainloop()