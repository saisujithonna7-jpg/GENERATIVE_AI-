# Week 5: LLM Feature Budget and Capacity Planning

## Aim
To model, evaluate, and test token economics, API quota limits (RPM/TPM), and cost estimations with safety margins prior to building Generative AI features.

## Key Capabilities
- **Token Economics**: Computes daily and monthly input/output token usage.
- **Cost Estimation**: Estimates daily and monthly operational costs based on per-million token pricing.
- **Capacity Planning**: Validates peak Requests Per Minute (RPM) and Tokens Per Minute (TPM) against configured provider quotas.
- **Automated Validation**: Unit tests (`test_budget.py`) asserting budget checks and limit enforcements.

## Project Structure
```text
week5/
├── .env                 # Environment variables (pricing, RPM/TPM limits, budget targets)
├── .gitignore           # Ignores .env and cache
├── requirements.txt     # python-dotenv
├── budget.py            # FeatureBudget model and capacity reporting logic
└── test_budget.py       # Unit tests verifying capacity and budget limits
```

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Run budget analysis:**
   ```powershell
   python budget.py
   ```

3. **Run unit tests:**
   ```powershell
   python test_budget.py
   ```
