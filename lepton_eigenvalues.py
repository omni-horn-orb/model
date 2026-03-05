import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh  # For large sparse matrices

# Parameters from paper
N = 1000  # Grid points
epsilon = 0.001  # Throat cutoff
r = 1.0  # Stabilized radius (adjust from stabilized_radius.py)
alpha = 137.0  # Holonomy constraint alpha = r / k; here assuming k\~0.007 for fine-structure link
l = 1  # Angular mode l >=1 (monopole l=0 excluded)
v_min = epsilon  # Throat
v_max = np.pi - epsilon  # Base approximation
dv = (v_max - v_min) / (N - 1)
v_grid = np.linspace(v_min, v_max, N)

# Define beta(v) = -2 sin(v) / (1 + cos(v))
beta = -2 * np.sin(v_grid) / (1 + np.cos(v_grid))

# beta' (numerical derivative for stability)
beta_prime = np.gradient(beta, dv)

# rho(v) = r * (1 + cos(v))
rho = r * (1 + np.cos(v_grid))

# Potential V(v)
V = (alpha**2 * l * (l + 1) / rho**2) - 0.5 * beta_prime - 0.25 * beta**2

# Build second-derivative finite-difference matrix (sparse tridiagonal)
# Operator: d²/dv² + V -> eigenvalues λ
diag_main = -2 / dv**2 + V
diag_off = np.ones(N-1) / dv**2
Laplacian = diags([diag_off, diag_main, diag_off], [-1, 0, 1], shape=(N, N), format='csr')

# Boundary conditions: Dirichlet at throat (g[0]=0), decaying at base (approximate Robin or Neumann; here set g[-1]=0 for simplicity)
# Adjust for decaying: could use shooting, but matrix eig for demo
Laplacian[0, :] = 0
Laplacian[0, 0] = 1  # g(0)=0
Laplacian[-1, :] = 0
Laplacian[-1, -1] = 1  # g(end)=0 (or implement exponential decay boundary)

# Compute lowest eigenvalues (use eigsh for sparse, k=5 modes)
eigenvalues, eigenvectors = eigsh(Laplacian, k=5, which='SM')  # Smallest magnitude

# Output eigenvalues (paper: \~9592, 9870, 10152, 10437, 10725 for alpha=137, r=1)
print("First 5 eigenvalues:", eigenvalues)

# Lepton masses (example scaling; adjust M_Pl and R for exact MeV)
M_Pl = 1.22e19  # GeV
R = 1.961
masses = np.sqrt(np.abs(eigenvalues)) * M_Pl / R / 1e12  # Rough scale to MeV (tune factor)
print("Lepton masses (MeV):", masses)  # Aim for [0.511, 105.6, 1777, ...]

# Convergence check: Refine N and check delta lambda < 0.005%
