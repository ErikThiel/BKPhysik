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

# Orts-Zeit-Verlauf berechnen durch Integration der Geschwindigkeit
ort = np.cumsum(geschwindigkeit) * (t[1] - t[0])  # Numerische Integration

# Integration der stündlichen Durchschnitte
ort_stuendlich = np.cumsum(stuendliche_durchschnitte) * (t[1] - t[0])

# Diagramme erstellen
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12), sharex=True)

# Orts-Zeit-Diagramm
ax1.plot(t, ort, label='Zurückgelegte Strecke')
ax1.plot(t, DURCHSCHNITTSGESCHWINDIGKEIT * t, 'r--', label='Erwartete Strecke (Durchschnitt)', color ='grey')
ax1.plot(t, ort_stuendlich, 'r--', label='Strecke basierend auf stündlichen Durchschnitten', color='red')

ax1.set_title('Zurückgelegte Strecke über Zeit')
ax1.set_xlabel('Zeit (Stunden)')
ax1.set_ylabel('Strecke (km)')
ax1.legend()
ax1.grid(True)

# Geschwindigkeit-Zeit-Diagramm
ax2.plot(t, geschwindigkeit, label='Momentangeschwindigkeit', alpha=0.7)
ax2.plot(t, stuendliche_durchschnitte, label='Stündlicher Durchschnitt', color='r', linewidth=2.5)
ax2.axhline(y=DURCHSCHNITTSGESCHWINDIGKEIT, color='k', linestyle='--', label='Gesamtdurchschnitt')

ax2.set_title('Geschwindigkeit über Zeit')
ax2.set_ylabel('Geschwindigkeit (km/h)')
ax2.legend()
ax2.grid(True)

# Zusätzliche Informationen anzeigen
ax2.text(0.05, 0.95, f'Gesamtstrecke: {GESAMTSTRECKE} km\nDurchschnittsgeschwindigkeit: {DURCHSCHNITTSGESCHWINDIGKEIT:.1f} km/h\nGesamtzeit: {GESAMTZEIT:.2f} h',
         transform=ax2.transAxes, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()