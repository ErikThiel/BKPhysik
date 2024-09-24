import numpy as np
import matplotlib.pyplot as plt

# Konstanten
DURCHSCHNITTSGESCHWINDIGKEIT = 97.8  # km/h
GESAMTSTRECKE = 586  # km
GESAMTZEIT = GESAMTSTRECKE / DURCHSCHNITTSGESCHWINDIGKEIT  # Stunden

# Zeitpunkte erstellen
t = np.linspace(0, GESAMTZEIT, 1000)

# Zufällige, stetige Geschwindigkeitskurve erzeugen
np.random.seed(42)  # Für Reproduzierbarkeit
geschwindigkeit = np.cumsum(np.random.randn(1000))
geschwindigkeit = geschwindigkeit - np.min(geschwindigkeit)  # Immer positiv
geschwindigkeit = geschwindigkeit / np.max(geschwindigkeit) * DURCHSCHNITTSGESCHWINDIGKEIT * 2
geschwindigkeit = geschwindigkeit + DURCHSCHNITTSGESCHWINDIGKEIT - np.mean(geschwindigkeit)

# Diagramm erstellen
plt.figure(figsize=(12, 6))
plt.plot(t, geschwindigkeit, label='Momentangeschwindigkeit')
plt.axhline(y=DURCHSCHNITTSGESCHWINDIGKEIT, color='r', linestyle='--', label='Durchschnittsgeschwindigkeit')

plt.title('Geschwindigkeit über Zeit')
plt.xlabel('Zeit (Stunden)')
plt.ylabel('Geschwindigkeit (km/h)')
plt.legend()
plt.grid(True)

# Zusätzliche Informationen anzeigen
plt.text(0.05, 0.95, f'Gesamtstrecke: {GESAMTSTRECKE} km\nDurchschnittsgeschwindigkeit: {DURCHSCHNITTSGESCHWINDIGKEIT:.1f} km/h\nGesamtzeit: {GESAMTZEIT:.2f} h', 
         transform=plt.gca().transAxes, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.show()