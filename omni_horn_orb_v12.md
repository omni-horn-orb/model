
Omni-Horn-Orb Framework
Version 12
PART I — MATHEMATATICAL STRUCTURE
1. Geometric Setup
Let Sigma^3 be a 3-dimensional Lorentzian hypersurface embedded in 5-dimensional Minkowski space M^(1,4).
Coordinates:
v in (0, pi)
(theta, phi) on S^2
Warping function:
rho(v) = r (1 + cos v)
Metric:
ds^2 = - dv^2 + rho(v)^2 dOmega^2
where dOmega^2 is the unit 2-sphere metric.
2. Asymptotic Behaviour Near v = pi
As v approaches pi:
rho(v) behaves like (r/2) (pi - v)^2
After reparametrization tau proportional to (pi - v):
ds^2 behaves like
ds^2 = - dtau^2 + C tau^4 dOmega^2
This produces angular confinement near the horn tip.
3. Scalar Mode Reduction
Assume separation:
psi(v, theta, phi) = g(v) Y_lm(theta, phi)
The radial equation becomes:
d^2 g / dv^2 + V(v) g = lambda g
on the interval (0, pi)
Boundary conditions (Dirichlet approximation for lowest modes):
g(0) = 0
g(pi - epsilon) = 0
4. Effective Potential
V(v) = alpha^2 l(l+1) / rho(v)^2
- (1/2) beta'(v)
- (1/4) beta(v)^2
where
beta(v) = - 2 sin v / (1 + cos v)
rho(v) = r (1 + cos v)
Holonomy constraint:
alpha = r / k
Numerical values used:
alpha = 137
r = 1
l = 1
5. Numerical Discretisation
Finite difference scheme:
Grid points: N = 1000
Cutoff: epsilon = 0.001
Tridiagonal matrix eigenproblem
Eigenvalues computed via symmetric tridiagonal solver.
First five eigenvalues:
lambda1 approx 9592
lambda2 approx 9870
lambda3 approx 10152
lambda4 approx 10437
lambda5 approx 10725
Convergence verified by:
Doubling N to 2000
Reducing epsilon to 0.0005
Relative change less than 0.005 percent.
6. Scaling with alpha
Varying alpha (50, 100, 137, 200) with other parameters fixed shows:
lambda scales proportionally to alpha^2
Specifically:
lambda / alpha^2 approx constant
lambda / alpha approx grows linearly with alpha
This confirms quadratic dependence at operator level.
7. Spectral Properties
Because:
The interval is finite
The potential diverges near v = pi
Dirichlet boundary conditions are imposed
The spectrum is discrete.
Eigenvalue spacing reflects angular structure l(l+1).
PART II — INTERPRETATION (SEPARATE FROM MATHEMATICS)
The Omni-Horn-Orb represents a geometrically embedded hypersurface whose warping structure generates a discrete excitation spectrum.
Mass ratios arise from:
Angular excitation structure
Holonomy-fixed amplification parameter
Confinement from horn geometry
No propagating scalar field on the hypersurface is required.
The spectrum emerges from geometry itself.
The amplification parameter alpha currently enters through the holonomy condition:
alpha = r / k
It is numerically consistent with the fine-structure scale but not yet derived uniquely from embedding or topology.
Metaphysical interpretation is not required for mathematical validity.
The mathematics stands independently.
Version 12 complete.
