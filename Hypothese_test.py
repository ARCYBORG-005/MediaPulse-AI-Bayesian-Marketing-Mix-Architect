import arviz as az

# 1. Define our Hypothesis Data
# We compare the posterior of 'channel_contribution' for Google vs Facebook
google_post = posterior["channel_contribution"].sel(channel="google_spend").sum(dim="date")
fb_post = posterior["channel_contribution"].sel(channel="facebook_spend").sum(dim="date")

# 2. Calculate the 'Difference' Distribution
# If the difference is consistently above 0, Google is better.
diff_distribution = google_post - fb_post

# 3. Plot the Hypothesis Test (ROPE)
plt.figure(figsize=(8, 5))
az.plot_posterior(
    diff_distribution, 
    ref_val=0, # Our Null Hypothesis: There is NO difference
    hdi_prob=0.95, 
    color='skyblue'
)
plt.title("Hypothesis Test: Google Contribution vs. Facebook Contribution")
plt.xlabel("Difference in Revenue ($)")
plt.savefig("data/hypothesis_test.png")
plt.show()

# 4. Senior Interpretation
prob_google_better = (diff_distribution > 0).mean().values
print(f"📊 Probability that Google outperformed Facebook: {prob_google_better*100:.2f}%")
