import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81  # m/s^2
TIME_STEP = 1   # s

# Given values
theta = np.pi / 6  # 60 degrees
beta = np.pi / 4   # 45 degrees
initial_velocity = 30  # m/s

# Function to calculate trajectory
def calculate_trajectory(angle, velocity, time):
    velocity_x = velocity * np.cos(angle)
    velocity_y = velocity * np.sin(angle)
    height = -0.5 * GRAVITY * (time / velocity_x)**2 + (velocity_y * time) / velocity_x
    return height

# Time axis
time = np.arange(0, 101, TIME_STEP)

# Calculate heights for different angles
height_60_deg = calculate_trajectory(theta, initial_velocity, time)
height_45_deg = calculate_trajectory(beta, initial_velocity, time)

# Plotting
plt.plot(time, height_60_deg, label='60 Degrees')
plt.plot(time, height_45_deg, label='45 Degrees')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion at Different Angles')
plt.legend()
plt.grid(True)
plt.savefig('schrägerWurf.png')  # Save the plot as an image file
plt.show()
