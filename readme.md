# 📈 Function Plotter

This Python program takes a mathematical function and draws it in a window without using any third-party packages. The program generates a list of x-values for the function, computes the corresponding y-values, and then scales and plots the function in a window (previously using tkinter, now using matplotlib).

## Usage

To use the program, first, run `pip pip install -r requirements.txt`, and then simply run the `funcDraw.py` file and (when prompted) define your own function to be plotted inside the `f(x)` function. You can also customize the range of x-values to plot by adjusting the `x = np.linspace(-10, 10, 1000)` variable.


## Example
Here is an example of the output of the program with the f(x) = x**2 function:
![If you see this, the image didn't load. Shit. Uhh, basicaly it's an image of the program in action. Yeah.](https://i.imgur.com/VLsqAYh.png)

This program was created by [myself](https://github.com/necogay) as a personal project.

## Known Issues
- Sine, cosine, tangent and other trigonometric functions do not work as of now. Critical issue, will fix ASAP.
- The window looks barebones.
