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
