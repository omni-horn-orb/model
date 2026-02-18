# metric_derivations_sympy.py
# Omni-Horn-Orb v2 symbolic metric with stabilized radius

import sympy as sp
from stabilized_radius import r_stable

r = r_stable
print("Using stabilized radius:", r)

t, chi = sp.symbols("t chi")

a = sp.Function("a")(t)

metric = sp.Matrix([
    [-1, 0],
    [0, a**2 * r**2]
])

print("Metric tensor:")
sp.pprint(metric)
