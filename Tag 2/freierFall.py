import numpy as np
import matplotlib.pyplot as plt

# Parameters
time = np.arange(0, 3.1, 0.1)  # Time in seconds
initial_height = 40            # Initial height in meters
gravity = 9.81                 # Acceleration due to gravity in m/s^2

# Equation of motion
height = -0.5 * gravity * time**2 + initial_height

# Plotting
plt.plot(time, height, label='Height vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Free Fall Motion')
plt.grid(True)
plt.legend()
plt.savefig('free_fall_plot.png')  # Save the plot as an image file
plt.show()