# Wobbling Circles Drawer

A small Python module to generate and plot smooth wobbling circles using Fourier-based radial deformation. I used this for a tattoo design ;)

## Features
- Create circles with configurable radius, position, line width, and wobble parameters.
- Export the generated image as a high-resolution PNG.

## How it works
The core idea behind the wobble effect:
- Each circle starts as a perfect circle.
- The radius is then slightly modified at each angle (theta) using a Fourier series: sine and cosine terms with random amplitudes create smooth radial fluctuations.
- The number of Fourier terms correspond to the number of wobbling points.
- The wobble_strength controls how far the circle deviates from a perfect radius.

## Python version
python >= 3.10

## Output example
![wobble_circles.png](https://github.com/marcobarenghi/wobbling_circles/blob/main/wobble_circles.png)
