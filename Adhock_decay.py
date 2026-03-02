import numpy as np
import matplotlib.pyplot as plt

# Posterior scalar alpha (shared across channels)
alpha = posterior["adstock_alpha"].mean().item()  # scalar

weeks = np.arange(0, 9)
decay = alpha ** weeks

plt.figure(figsize=(8, 5))
plt.bar(weeks, decay, color='orange', alpha=0.7)
plt.plot(weeks, decay, marker='o', color='darkorange')
plt.title("Adstock Decay (Carryover Effect)")
plt.xlabel("Weeks After Ad Aired")
plt.ylabel("Percentage of Impact Remaining")
plt.grid(alpha=0.3)
plt.savefig("data/adstock_decay.png")
plt.show()
