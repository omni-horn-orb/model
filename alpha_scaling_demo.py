import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Minimal demonstration of horn-entropy driven expansion
#
# From manuscript:
#   S_tot = ∫ M^2 dN
#   M(a) ∝ a^(3/2)
#   N(a) ∝ a^(1/2)
#   ⇒ S_tot ∝ a^(7/2)
#
# Therefore:
alpha = 3.5   # = 7/2 exactly
# -------------------------------------------------------

# time parameter (dimensionless)
t = np.linspace(0.01, 5.0, 500)

# simple scale factor model (toy)
# a(t) grows monotonically
a = t

# amplification term from entropy scaling
amp = a**alpha

# normalized for plotting clarity
amp = amp / np.max(amp)

plt.figure(figsize=(8,5))
plt.plot(a, amp, label="Amplification ~ a^alpha")

plt.xlabel("Scale factor a")
plt.ylabel("Normalized amplification")
plt.title("Horn-Entropy Amplification (alpha = 7/2)")
plt.legend()
plt.grid(True)

# show alpha directly on the plot
plt.text(0.6*np.max(a), 0.2,
         "alpha = 7/2\nS_tot ∝ a^(7/2)",
         fontsize=11)

plt.tight_layout()
plt.show()
