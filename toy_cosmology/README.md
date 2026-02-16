"""
Toy Cosmology: Density–Driven Expansion Demo

This script numerically integrates a very simple scale factor a(t)
using three qualitative components:

1. Primary expansion
2. Density-dependent emergent attraction
3. Late-time low-density amplification

Purpose:
Demonstrate whether such a structure can naturally produce:

- Early deceleration
- Later acceleration
- A transition redshift

This is a pedagogical toy model only.
Parameters are hand-chosen.
No observational fitting is performed.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# METHODS / MODEL DESCRIPTION
# -----------------------------
#
# We evolve a scale factor a(t) forward in time using:
#
#   a_ddot = +A               (primary expansion)
#            - B * rho       (emergent attraction)
#            + C / (rho+eps) (late-time amplification)
#
# Density rho scales as 1/a^3.
#
# This is NOT derived from GR or Friedmann equations.
# It is purely phenomenological.
#
# Goal: see if qualitative cosmic history appears:
# deceleration -> acceleration.


# -----------------------------
# Parameters (chosen manually)
# -----------------------------

A = 0.6      # primary expansion strength
B = 1.2      # density attraction
C = 0.15     # late-time amplification
eps = 1e-4   # prevents division by zero

dt = 0.01
steps = 6000

# -----------------------------
# Initial conditions
# -----------------------------

a = 0.05     # initial scale factor
v = 0.0      # da/dt

a_list = []
t_list = []
q_list = []
z_list = []
H_list = []

# -----------------------------
# Time integration
# -----------------------------

for i in range(steps):
    t = i * dt

    rho = 1.0 / (a**3)

    a_ddot = A - B * rho + C / (rho + eps)

    v += a_ddot * dt
    a += v * dt

    if a <= 0:
        continue

    # Deceleration parameter q = - (a * a_ddot) / v^2
    if v != 0:
        q = -(a * a_ddot) / (v*v)
    else:
        q = np.nan

    z = 1/a - 1

    a_list.append(a)
    t_list.append(t)
    q_list.append(q)
    z_list.append(z)

# Convert to arrays
a_arr = np.array(a_list)
t_arr = np.array(t_list)
q_arr = np.array(q_list)
z_arr = np.array(z_list)

# -----------------------------
# Find transition redshift
# -----------------------------

mask = np.isfinite(q_arr)
z_valid = z_arr[mask]
q_valid = q_arr[mask]

idx = np.where(q_valid < 0)[0]

if len(idx) > 0:
    z_transition = z_valid[idx[0]]
else:
    z_transition = np.nan

print("Estimated acceleration transition redshift:")
print("z_transition =", round(z_transition, 2))

# -----------------------------
# Plot results
# -----------------------------

plt.figure()

plt.plot(t_arr, a_arr, label="Scale factor a(t)")
plt.xlabel("Time (arbitrary units)")
plt.ylabel("Scale factor a")
plt.title("Toy Cosmology: Scale Factor Evolution")
plt.legend()
plt.show()

plt.figure()

plt.plot(z_valid, q_valid, label="Deceleration parameter q(z)")
plt.axhline(0, linestyle="--", label="Acceleration boundary")
plt.xlabel("Redshift z")
plt.ylabel("q(z)")
plt.title("Toy Cosmology: Deceleration → Acceleration")
plt.gca().invert_xaxis()
plt.legend()
plt.show()
