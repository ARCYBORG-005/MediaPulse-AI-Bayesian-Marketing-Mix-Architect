# posterior contains a Dataset, e.g., posterior['saturation_beta'] might be scalar
# Instead, use the channel_data shape

channel_cols = ["google_spend", "facebook_spend", "tv_spend"]

# Some versions store channel beta/lam as:
# posterior["saturation_beta"].values  -> shape (chain, draw)
# If channel-specific, you need to index along channel dimension, sometimes:
# posterior["constant_data"].channel_scale

# Let’s extract a practical mean per channel:

beta_values = posterior["saturation_beta"].mean(dim=["chain","draw"]).values
lam_values   = posterior["saturation_lam"].mean(dim=["chain","draw"]).values

# If beta/lam are scalar (same for all channels), you just reuse them:
print("Beta:", beta_values, "Lambda:", lam_values)
