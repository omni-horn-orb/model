import numpy as np
from scipy.integrate import solve_ivp

# Constants (from paper)
G4 = 1.0  # Normalized
alpha = 0.1  # Baseline
A = 0.32  # Growth rate per Hubble time
B = A / rho_max  # For logistic
rho_max = 1.0  # Normalized
H0 = 1.0  # Normalized present Hubble
Omega_m = 0.3
rho_m0 = 3 * H0**2 / (8 * np.pi * G4) * Omega_m
t_span = (0, 20)  # Billion years normalized
rho_g0 = 0.98 * rho_max  # Present gap density
phi0 = np.sqrt(2 * rho_g0)  # Assuming rho_g \~ phi^2 /2 for canonical

# Effective w_g (mild phantom)
def w_g(rho_g):
    return -1.37 + 0.37 * (rho_g / rho_max)  # Transitions to -1 then 0

# Saturation factor (1 at rho_max)
def sat_factor(rho_g):
    return rho_g / rho_max

# System: [H, rho_m, rho_g] (or add phi for full scalar)
def friedmann_system(t, y):
    H, rho_m, rho_g = y
    p_g = w_g(rho_g) * rho_g
    H_dot = - (4 * np.pi * G4 / 3) * (rho_m + 2 * rho_g + 3 * p_g)  # Base Raychaudhuri
    H_dot += alpha * (3 * H_dot + 9 * H**2) * sat_factor(rho_g)  # GB correction (self-consistent solve needed?)
    # Approximate logistic for rho_g (overdamped)
    rho_g_dot = A * rho_g - B * rho_g**2 - 3 * H * rho_g * (1 + w_g(rho_g))  # Expansion dilution
    rho_m_dot = -3 * H * rho_m  # Matter scaling
    return [H_dot, rho_m_dot, rho_g_dot]

# Initial conditions
y0 = [H0, rho_m0, rho_g0]

# Solve
sol = solve_ivp(friedmann_system, t_span, y0, method='RK45', rtol=1e-8, atol=1e-10)

# Find reversal time (H crosses 0)
reversal_idx = np.where(sol.y[0] < 0)[0][0] if np.any(sol.y[0] < 0) else None
print("Reversal time:", sol.t[reversal_idx] if reversal_idx else "No reversal in span")

# Plot or output (add matplotlib if needed)
