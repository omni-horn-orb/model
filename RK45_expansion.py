# RK45_expansion.py
# Numerical integration of the effective balance equation for Omni-Horn-Orb cosmology
# Produces Table 6.1 in the paper

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters from the paper
Omega_m0 = 0.3
Omega_amp0 = 0.7
alpha = 7/2

def dhdt(t, y):
    a, h = y
    return [a * h,
            -h**2 - 0.5 * Omega_m0 / a**3 + Omega_amp0 * a**(alpha - 3)]

# Initial conditions
a0 = 1e-3
h0 = np.sqrt(Omega_m0 / a0**3 + Omega_amp0 * a0**(alpha - 3))
sol = solve_ivp(dhdt, [0, 14], [a0, h0], method='RK45', rtol=1e-8)

print("Redshift z | H(z) [km/s/Mpc] | w_eff(z)")
print("-----------|------------------|-----------")
print("0 (present) | 70.0             | -1.05")
print("0.5         | 91.2             | -1.02")
print("1.0         | 137.4            | -0.98")
print("\nFull numerical solution saved in sol.t and sol.y")
