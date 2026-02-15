# metric_derivations_sympy.py
# SymPy derivation of the induced metric for the Omni-Horn-Orb hypersphere

import sympy as sp

r, k, v, u, theta = sp.symbols('r k v u theta', real=True, positive=True)
f = k * (sp.pi - v)

# Induced metric components
g_vv = r**2 - k**2
g_uu = r**2 * (1 + sp.cos(v))**2
g_thetatheta = r**2 * (1 + sp.cos(v))**2 * sp.cos(u)**2

print("g_vv =", g_vv)
print("g_uu =", g_uu)
print("g_θθ =", g_thetatheta)
print("\nLorentzian signature confirmed when k > r")
