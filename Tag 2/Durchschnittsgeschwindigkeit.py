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

def berechne_durchschnitte(intervall_stunden):
    intervalle = int(np.ceil(GESAMTZEIT / intervall_stunden))
    durchschnitte = np.zeros_like(t)
    for i in range(intervalle):
        start = int(i * len(t) / (GESAMTZEIT / intervall_stunden))
        end = int((i + 1) * len(t) / (GESAMTZEIT / intervall_stunden)) if i < intervalle - 1 else len(t)
        durchschnitt = np.mean(geschwindigkeit[start:end])
        durchschnitte[start:end] = durchschnitt
    return durchschnitte

# Durchschnitte berechnen
stuendliche_durchschnitte = berechne_durchschnitte(1)
halbstuendliche_durchschnitte = berechne_durchschnitte(0.5)
viertelstuendliche_durchschnitte = berechne_durchschnitte(0.25)

# Diagramm erstellen
plt.figure(figsize=(12, 6))
plt.plot(t, geschwindigkeit, label='Momentangeschwindigkeit', alpha=0.7)
plt.plot(t, viertelstuendliche_durchschnitte, label='Viertelstündlicher Durchschnitt', color='g', linewidth=1.5)
plt.plot(t, halbstuendliche_durchschnitte, label='Halbstündlicher Durchschnitt', color='m', linewidth=2)
#plt.plot(t, stuendliche_durchschnitte, label='Stündlicher Durchschnitt', color='r', linewidth=2.5)
plt.axhline(y=DURCHSCHNITTSGESCHWINDIGKEIT, color='k', linestyle='--', label='Gesamtdurchschnitt')

plt.title('Geschwindigkeit über Zeit')
plt.xlabel('Zeit (Stunden)')
plt.ylabel('Geschwindigkeit (km/h)')
plt.legend()
plt.grid(True)

# Zusätzliche Informationen anzeigen
#plt.text(0.05, 0.95, f'Gesamtstrecke: {GESAMTSTRECKE} km\nDurchschnittsgeschwindigkeit: {DURCHSCHNITTSGESCHWINDIGKEIT:.1f} km/h\nGesamtzeit: {GESAMTZEIT:.2f} h', 
#         transform=plt.gca().transAxes, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.show()