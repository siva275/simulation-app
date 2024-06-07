import numpy as np

def pv_simulation(irradiance, temperature):
    # Simple PV simulation model
    Isc = 5  # Short-circuit current (A)
    Voc = 0.6  # Open-circuit voltage (V)
    Rs = 0.01  # Series resistance (Ohms)
    Rsh = 1000  # Shunt resistance (Ohms)
    n = 1.3  # Ideality factor
    k = 1.38064852e-23  # Boltzmann constant (J/K)
    q = 1.60217662e-19  # Charge of an electron (C)
    T = temperature + 273.15  # Convert to Kelvin

    Iph = irradiance * Isc  # Photocurrent
    V = np.linspace(0, Voc, 100)  # Voltage array
    I = Iph - (Isc * (np.exp((V + Isc * Rs) / (n * k * T / q)) - 1)) - ((V + Isc * Rs) / Rsh)  # Current array
    P = V * I  # Power array

    return V, I, P
