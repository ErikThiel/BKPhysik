import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Define the function
def f(x):
    return x**2 - 3*x - 6.25

# Generate x values
x = np.linspace(-2.1, 5.1, 1000)
# Compute y values
y = f(x)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='y(x) = x² - 3x - 6.25')
plt.axhline(y=0, color='r', linestyle='--')
plt.axvline(x=0, color='r', linestyle='--')

# Highlight the area between the roots
x1 = (3 - np.sqrt(34)) / 2
x2 = (3 + np.sqrt(34)) / 2
x_fill = np.linspace(x1, x2, 1000)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color='lightgray', alpha=0.5, label='Area between roots')

# Add titles and labels
plt.title('Graph von y(x) = x² - 3x - 6.25')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

# Define the absolute function for integration
def abs_f(x):
    return abs(x**2 - 3*x - 6.25)

# Calculate the area between the roots
area, _ = integrate.quad(abs_f, x1, x2)
print(f"Die Fläche zwischen den Nullstellen beträgt etwa {area:.4f}")