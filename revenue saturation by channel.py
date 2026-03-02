import numpy as np
import matplotlib.pyplot as plt

x_spend = np.linspace(0, 15000, 100)
colors = ['#4285F4', '#1877F2', '#FF0000']
channel_cols = ["google_spend", "facebook_spend", "tv_spend"]

# Shared beta/lam from posterior
beta = posterior["saturation_beta"].mean().item()
lam   = posterior["saturation_lam"].mean().item()

plt.figure(figsize=(10, 6))

for i, channel in enumerate(channel_cols):
    y_revenue = beta * (1 - np.exp(-lam * x_spend / 10000))  # shared curve
    plt.plot(x_spend, y_revenue, label=f"{channel.replace('_spend','').title()} Curve", color=colors[i], lw=3)

plt.title("Diminishing Returns: Revenue Saturation by Channel", fontsize=14, fontweight='bold')
plt.xlabel("Weekly Spend ($)", fontsize=12)
plt.ylabel("Incremental Revenue Contribution", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.axvline(x=5000, color='gray', linestyle=':', label='Current Avg Spend')

plt.tight_layout()
plt.savefig("data/all_saturation_curves.png")
plt.show()

print("✅ SUCCESS: Saturation curves generated (shared curve for all channels).")
