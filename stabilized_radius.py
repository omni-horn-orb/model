from model_config import CONFIG
import numpy as np
from scipy.optimize import root_scalar
import json
from datetime import datetime

B = CONFIG["B"]
c = CONFIG["c"]
holonomy_amp = CONFIG["holonomy_amp"]

def A(r):
    return 1.0 + holonomy_amp * np.sin(2 * np.pi * r)

def V(r):
    return A(r) / r**2 + B * np.exp(-c / r)

def dV(r, eps=1e-6):
    return (V(r + eps) - V(r - eps)) / (2 * eps)

def d2V(r, eps=1e-5):
    return (V(r + eps) - 2 * V(r) + V(r - eps)) / eps**2

def find_stable_radius():
    roots = []

    scan_min = CONFIG["r_scan_min"]
    scan_max = CONFIG["r_scan_max"]
    scan_points = CONFIG["r_scan_points"]

    for guess in np.linspace(scan_min, scan_max, scan_points):
        try:
            sol = root_scalar(dV, bracket=[guess, guess + 0.2], method='brentq')
            r_candidate = sol.root

            if r_candidate > 0 and d2V(r_candidate) > 0:
                roots.append(r_candidate)
        except:
            continue

    if not roots:
        raise ValueError("No stable radius found.")

    return min(roots)

r_stable = find_stable_radius()

print("\n[Omni-Horn-Orb v2]")
print("Stabilized radius (lowest stable branch):", r_stable)
print("Config parameters:", CONFIG)
print("Discrete geometric enforcement active.\n")

def log_stabilization(filename="stabilization_snapshot.json"):
    snapshot = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "r_stable": float(r_stable),
        "config": CONFIG
    }

    with open(filename, "w") as f:
        json.dump(snapshot, f, indent=4)

    print(f"Stabilization snapshot written to {filename}")
