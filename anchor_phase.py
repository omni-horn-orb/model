# anchor_phase.py
# Omni-Horn-Orb v2 anchor phase using stabilized radius

import numpy as np
from stabilized_radius import r_stable

r = r_stable
print("Using stabilized radius:", r)


def anchor_phase(chi):
    return np.cos(chi / r)


if __name__ == "__main__":
    chi_vals = np.linspace(0, 10, 100)
    phases = anchor_phase(chi_vals)

    print("Anchor phase computed using stabilized radius.")
