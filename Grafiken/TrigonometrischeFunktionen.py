import numpy as np
import matplotlib.pyplot as plt

# Definiere den Bereich für x-Werte
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Berechne die Funktionswerte
sin_y = np.sin(x)
cos_y = np.cos(x)
tan_y = np.tan(x)

# Erstelle den Plot
plt.figure(figsize=(12, 8))
plt.plot(x, sin_y, label='sin(x)', color='blue')
plt.plot(x, cos_y, label='cos(x)', color='red')
plt.plot(x, tan_y, label='tan(x)', color='green')

# Begrenze den y-Achsenbereich für bessere Sichtbarkeit
plt.ylim(-3, 3)

# Füge vertikale Linien für die Asymptoten von tan(x) hinzu
for i in range(-2, 2):
    plt.axvline(x=(i + 0.5) * np.pi, color='green', linestyle='--', alpha=0.5)

# Konfiguriere den Plot
plt.title('Trigonometrische Funktionen')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Füge Beschriftungen für wichtige x-Werte hinzu
xticks = np.arange(-2*np.pi, 2*np.pi + np.pi/2, np.pi/2)
xlabels = ['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
plt.xticks(xticks, xlabels)

# Zeige den Plot
plt.tight_layout()
plt.show()