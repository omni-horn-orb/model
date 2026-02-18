# lepton_lattice.py
# Omni-Horn-Orb v2 lepton spectrum demonstration

import numpy as np
from stabilized_radius import r_stable

r = r_stable
print("Using stabilized radius:", r)


def lepton_mass(n):
    return n / r


levels = range(1, 6)

for n in levels:
    print(f"Level {n} mass:", lepton_mass(n))
