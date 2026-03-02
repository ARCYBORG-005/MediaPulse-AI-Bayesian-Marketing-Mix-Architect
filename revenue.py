import os
from models.revenue import OpenAI

# 1. Define the Senior Consultant Logic
def get_ai_consultation(attribution_data):
    # This is the prompt we discussed - it turns a Data Scientist into a Consultant
    client = OpenAI(api_key="YOUR_OPENAI_API_KEY") 
    
    system_prompt = """
    You are a Senior Marketing Scientist. You interpret Bayesian MMM results.
    Your tone is executive, data-driven, and focused on Incremental ROI.
    Keywords to use: Saturation, Adstock, Marginal Contribution, Efficiency.
    """
    
    user_content = f"""
    Our Bayesian model results are in. 
    Total Revenue Attribution:
    {attribution_data.to_string()}
    
    What are the top 3 strategic recommendations for next quarter's budget?
    """

    # For the interview demo, you can print this or use the actual API
    print(" AI STRATEGIST PROMPT GENERATED:")
    print(user_content)

# 2. Prepare the data for the AI
# We use the df_contrib you just created
get_ai_consultation(df_contrib)

print("\nPROJECT COMPLETE: 'MediaPulse AI'")
print("Files ready for demo:")
print("1. models/trained_mmm_model.pickle (The Brain)")
print("2. data/revenue_attribution.png (The Proof)")
print("3. app.py (The Interface)")
