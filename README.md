![Omni-Horn-Orb Banner](Screenshot_20260215_030709_Gallery.jpg)

<div align="center">
  <em>Omni-Horn-Orb hypersphere – custom visualisation by the author, 15 February 2026</em>
</div># Omni-Horn-Orb Model

**A Geometric Framework for Cosmology Without Dark Components**

Author: Christopher M. Gibson  
Date: February 15, 2026  
Permanent archive: [Zenodo DOI 10.5281/zenodo.18416212](https://doi.org/10.5281/zenodo.18416212)

### Full Computational Repository — Now Complete

This repository contains all the code, derivations, and numerical results for the Omni-Horn-Orb hypersphere cosmology described in the paper.

### What is now live:

- **`Omni_Horn_Orb_Full_Notebook.ipynb`** → Complete Jupyter notebook with live expansion history, w(z) calculations, and notes  
- **`lepton_lattice.py`** → Full lepton mass spectrum from the E₈-root lattice on the equatorial slice (exact matches to §5.7) + neutrino hints  
- **`RK45_expansion.py`** → Live Runge-Kutta integration — no hardcoded numbers, full dynamic H(z) and w_eff(z) table  
- **`metric_derivations_sympy.py`** → Symbolic metric and Christoffel symbols (from §2)  
- **The full paper** → `Omni-Horn-Orb-Model-20260215.pdf`

### How to run

All code runs with standard Python (numpy, scipy, matplotlib, sympy).  
Just clone the repo and run the files — no complicated setup.

### Quick start

```bash
# Run the live expansion table
python RK45_expansion.py

# Run the lepton masses
python lepton_lattice.py

# Open the full notebook
jupyter notebook Omni_Horn_Orb_Full_Notebook.ipynb
