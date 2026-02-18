# RK45_expansion.py
# Omni-Horn-Orb v2 expansion solver with stabilized radius enforcement

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from stabilized_radius import r_stable

r = r_stable
print("Using stabilized radius:", r)


# Example effective Hubble parameter using stabilized radius
def H(z):
    return np.sqrt(1.0 / r**2 + (1 + z)**3)


def dadt(t, a):
    z = 1.0 / a - 1.0
    return a * H(z)


a0 = 1.0
t_span = (0, 5)

solution = solve_ivp(dadt, t_span, [a0], method="RK45", dense_output=True)

t_vals = np.linspace(0, 5, 200)
a_vals = solution.sol(t_vals)[0]

plt.figure()
plt.plot(t_vals, a_vals)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.title("Expansion History (v2 Stabilized Radius)")
plt.show()
