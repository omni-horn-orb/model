import numpy as np
from scipy.integrate import quad

def a(theta, R=1.0):
    return R * (1 + np.cos(theta))

def ap(theta, R=1.0):
    return -R * np.sin(theta)

def app(theta, R=1.0):
    return -R * np.cos(theta)

def L_GB(theta, R=1.0):
    aa = a(theta, R)
    aap = ap(theta, R)
    aapp = app(theta, R)
    if aa < 1e-12:
        return 0.0
    aap2 = np.power(aap, 2)
    aap4 = np.power(aap, 4)
    aa3 = np.power(aa, 3)
    aa4 = np.power(aa, 4)
    term1 = 24 * aapp * aap2 / aa3
    term2 = 12 * aap4 / aa4
    term3 = 6 / aa4
    term4 = 6 * aapp / aa
    term5 = 18 * aap2 / np.power(aa, 2)
    return term1 + term2 + term3 + term4 + term5

def integrand(theta, R=1.0):
    return np.power(a(theta, R), 3) * L_GB(theta, R)

# Parameters
eps = 0.001
R = 1.0  # Baseline

# Compute integral
integral, err = quad(integrand, 0, np.pi - eps, epsabs=1e-10, epsrel=1e-10, limit=10000)
print(f"Integrated value: {integral} ± {err}")

# Additional checks for different eps (as in paper)
for e in [0.01, 0.0001]:
    int_e, err_e = quad(integrand, 0, np.pi - e, epsabs=1e-10, epsrel=1e-10, limit=10000)
    print(f"For eps={e}: {int_e} ± {err_e}")
