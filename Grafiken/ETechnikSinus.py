import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Sinuswelle
def sine_wave(t, amplitude, frequency, phase_shift):
    omega = 2 * np.pi * frequency
    return amplitude * np.sin(omega * t + phase_shift)

# Erstelle einen Zeitvektor (0 bis 1 Sekunde mit 1000 Punkten)
t = np.linspace(0, 1, 1000)

# Parameter für die erste Welle
amplitude1 = 5
frequency1 = 2  # Hz

# Parameter für die zweite Welle
amplitude2 = 2.5
frequency2 = 2  # Hz
# Berechne die Phasenverschiebung für eine Nullstelle bei 0.125s
phase_shift2 = -2 * np.pi * frequency2 * 0.125
print(phase_shift2)

# Berechne die Wellenformen
U1 = sine_wave(t, amplitude1, frequency1, 0)
U2 = sine_wave(t, amplitude2, frequency2, phase_shift2)

# Erstelle die Plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Erste Welle
ax1.plot(t, U1)
ax1.set_title('U(t) = 5 * sin(2π * 2Hz * t)')
ax1.set_xlabel('Zeit (s)')
ax1.set_ylabel('Spannung (V)')
ax1.grid(True)
ax1.axhline(y=0, color='r', linestyle='--')

# Zweite Welle
ax2.plot(t, U2)
ax2.set_title('U(t) = 2.5 * sin(2π * 2Hz * t + φ), Nullstelle bei 0.125s')
ax2.set_xlabel('Zeit (s)')
ax2.set_ylabel('Spannung (V)')
ax2.grid(True)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.axvline(x=0.125, color='g', linestyle='--', label='Nullstelle bei 0.125s')
ax2.legend()

plt.tight_layout()
plt.show()