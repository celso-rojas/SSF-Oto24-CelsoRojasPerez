# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:54:54 2024

@author: celso
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación diferencial para el oscilador armónico
def harmonic_eq(x, t, k):
    return x[1], -k * x[0]

# Método de Euler para resolver el sistema
def euler_2var(x, func, t, k, dt):
    y = func(x, t, k)
    return x[0] + dt * y[0], x[1] + dt * y[1]

# Función para calcular y graficar resultados
def calc_plot2var(method, equation, k, dt, n_steps):
    t = np.arange(0, n_steps * dt, dt)  # Vector de tiempo
    x = np.zeros((n_steps, 2))  # Inicializar matriz de resultados
    x[0][0] = 2.0  # Posición inicial
    
    # Iterar usando el método numérico
    for i in range(n_steps - 1):
        x[i + 1] = method(x[i], harmonic_eq, t[i], k, dt)
    
    # Graficar posición y velocidad en el tiempo
    fig = plt.figure(figsize=(12, 5))
    axes = fig.add_subplot(1, 2, 1)
    axes.plot(t, x[:, 0], 'r', label="$x(t)$")  # Posición
    axes.plot(t, x[:, 1], 'b', label="$v(t)$")  # Velocidad
    axes.set_xlabel("$t$")
    axes.set_title(f"Oscilador con $k={k}$, $dt={dt}$")
    plt.legend(loc='upper left')
    
    # Graficar diagrama de fase
    axes = fig.add_subplot(1, 2, 2)
    axes.plot(x[:, 0], x[:, 1], '#ff8800')
    axes.set_xlabel("$x(t)$")
    axes.set_ylabel("$v(t)$")
    axes.set_title("Diagrama de fase")
    plt.show()

# Parámetros de la tarea
k_ranges = {
    "cercano a 0": np.linspace(0.01, 1, 10),
    "entre 1 y 25": np.linspace(1, 25, 10),
    "entre 30 y 200": np.linspace(30, 200, 10)
}

dt_values = [0.01, 0.05, 0.1]  # Tamaño de la partición
n_steps_values = [500, 1000, 5000]  # Número de pasos

# Ejecutar simulaciones para los diferentes valores de k, dt y n_steps
if __name__ == "__main__":
    for k_range_name, k_values in k_ranges.items():
        print(f"Rango de k: {k_range_name}")
        for k in k_values:
            for dt in dt_values:
                for n_steps in n_steps_values:
                    print(f"Simulación con k={k:.2f}, dt={dt}, n_steps={n_steps}")
                    calc_plot2var(euler_2var, harmonic_eq, k, dt, n_steps)
