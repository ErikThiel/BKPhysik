import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def math_operations(function_str):
    # Definiere die Symbole
    x = sp.Symbol('x')
    
    # Erstelle die Funktion
    function = sp.sympify(function_str)
    
    # a) Integration
    integral = sp.integrate(function, x)
    
    # b) Ableitung
    derivative = sp.diff(function, x)
    
    # c) Phasenverschiebung um π/2
    phase_shift = function.subs(x, x - sp.pi/2)
    
    # Ergebnisse ausgeben
    print(f"Originale Funktion: {function}")
    print(f"a) Integral: {integral}")
    print(f"b) Ableitung: {derivative}")
    print(f"c) Phasenverschiebung um π/2: {phase_shift}")
    
    # Funktionen für das Plotten vorbereiten
    f = sp.lambdify(x, function, "numpy")
    i = sp.lambdify(x, integral, "numpy")
    d = sp.lambdify(x, derivative, "numpy")
    p = sp.lambdify(x, phase_shift, "numpy")
    
    # Wertebereich für x
    x_vals = np.linspace(-1*np.pi, 1*np.pi, 1000)
    
    # Plot erstellen mit Subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))
    fig.suptitle(f"Grafische Darstellung für f(x) = {function_str}", fontsize=16)
    
    # Original Funktion
    axs[0, 0].plot(x_vals, f(x_vals))
    axs[0, 0].set_title('Original Funktion')
    axs[0, 0].grid(True)
    
    # Integral
    axs[0, 1].plot(x_vals, i(x_vals))
    axs[0, 1].set_title('Integral')
    axs[0, 1].grid(True)
    
    # Ableitung
    axs[1, 0].plot(x_vals, d(x_vals))
    axs[1, 0].set_title('Ableitung')
    axs[1, 0].grid(True)
    
    # Phasenverschiebung
    axs[1, 1].plot(x_vals, p(x_vals))
    axs[1, 1].set_title('Phasenverschiebung um π/2')
    axs[1, 1].grid(True)
    
    # Achsenbeschriftungen und Gitterlinien für alle Subplots
    for ax in axs.flat:
        ax.set(xlabel='x', ylabel='y')
        ax.axhline(y=0, color='k', linestyle='--')
        ax.axvline(x=0, color='k', linestyle='--')
    
    # Layout anpassen
    plt.tight_layout()
    plt.show()

# Beispielaufruf
function_str = "5*sin(2*pi*x)"
math_operations(function_str)