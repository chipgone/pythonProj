# 📈 Function Plotter

This Python program takes a mathematical function and draws it in a window without using any third-party packages. The program generates a list of x-values for the function, computes the corresponding y-values, and then scales and plots the function in a Tkinter window.

## Usage

To use the program, simply run the `function_plotter.py` file and define your own function to be plotted inside the `f(x)` function. You can also customize the range of x-values to plot by adjusting the `x_min`, `x_max`, and `num_points` variables.

```python
# Function to plot (could make it editable by user later using input)
def f(x):
    return x**2 # A parabola as an example

# Range of x-values to plot
x_min = -10
x_max = 10
num_points = 1000
```

## Example
Here is an example of the output of the program with the f(x) = x**2 function:
![If you see this, the image didn't load. Shit. Uhh, basicaly it's an image of the program in action. Yeah.](https://i.imgur.com/LDlGEDY.png)

This program was created by [myself](https://github.com/necogay) as a personal project.