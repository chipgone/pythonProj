import matplotlib.pyplot as plt
import numpy as np
import re
import math

# Define a function to check if a string is a valid mathematical function
def is_valid_function(f):
    try:
        x = np.arange(-10, 10, 0.1)
        eval(f)
        return True
    except:
        return False

# Prompt the user to enter a function
while True:
    f = input("Enter a mathematical function: ")

    # Check if the function is valid
    if is_valid_function(f):
        break
    else:
        print("Invalid function. Please try again.")

# Replace "^" with "**" in the function string
f = re.sub(r'\^', r'**', f)

# Define the function to be plotted
def plot_func(x):
    # Allow the use of trigonometric and logarithmic functions
    sin = math.sin
    cos = math.cos
    tan = math.tan
    log = math.log10
    return eval(f)

# Generate x-values for the function
x = np.linspace(-10, 10, 1000)

# Generate y-values for the function
y = plot_func(x)

# Create a plot with the x- and y-values
plt.plot(x, y)

# Set the plot title and axis labels
plt.title('Function Plotter')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()