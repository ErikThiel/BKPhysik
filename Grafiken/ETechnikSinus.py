import numpy as np
import matplotlib.pyplot as plt

# Definiere die Parameter
amplitude = 5
frequency = 2  # Hz
omega = 2 * np.pi * frequency

# Erstelle einen Zeitvektor (0 bis 1 Sekunde mit 1000 Punkten)
t = np.linspace(0, 1, 1000)

# Berechne U(t)
U = amplitude * np.sin(omega * t)

# Erstelle den Plot
plt.figure(figsize=(10, 6))
plt.plot(t, U)
plt.title('U(t) = 5 * sin(2π * 2Hz * t)')
plt.xlabel('Zeit (s)')
plt.ylabel('Spannung (V)')
plt.grid(True)

# Füge eine horizontale Linie bei y=0 hinzu
plt.axhline(y=0, color='r', linestyle='--')

# Zeige den Plot
plt.show()