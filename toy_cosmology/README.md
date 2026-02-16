# Toy Cosmology: Density–Driven Acceleration Demo

This folder contains a small Python experiment exploring whether a simple
density-dependent acceleration model can reproduce the qualitative expansion
history of our universe:

• early deceleration  
• later transition to acceleration  

This is **not** a full cosmological theory or fit to observational data.
It is a pedagogical / exploratory toy model.

---

## What this does

The script numerically integrates a scale factor a(t) using:

Primary expansion term  
Emergent attractive term proportional to density  
Late-time amplification term (activated at low density)

It then:

• plots a(t)  
• computes the deceleration parameter q(z)  
• estimates the redshift where acceleration begins  

This is intended only to test *qualitative behavior*.

---

## Files

`toy_cosmology.py`  
Main Python script.

---

## Requirements

Python 3  
numpy  
matplotlib  

Install with:

pip install numpy matplotlib

---

## Run

python toy_cosmology.py

---

## Important note

Free parameters are chosen manually.
No parameter fitting to ΛCDM or observational datasets is performed.

This code is meant to demonstrate structural plausibility only.

---

## Purpose

To provide a minimal computational companion to the geometric ideas
in the Omni-Horn-Orb manuscript, without claiming predictive power.
