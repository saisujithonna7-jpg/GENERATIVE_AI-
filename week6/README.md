# Week 6: Golden Question Set Baseline Evaluation

## Aim
To establish an automated evaluation baseline (v0.1) for an LLM (`llama3.2` via Ollama) against a curated **Golden Question Set**, scoring answers through keyword matching and generating structured benchmark reports.

## Key Capabilities
- **Golden Dataset**: Curated questions with expected answers, target keywords, and references (`golden_set.json`).
- **Local Model Inference**: Automated querying of Ollama local model (`llama3.2`) at `temperature=0` for deterministic outputs.
- **Automated Scoring**: Calculates keyword matching accuracy, tagging responses as `PASS` (≥ 60%) or `REVIEW`.
- **Structured Export**: Exports evaluation results and metrics to CSV (`baseline_results.csv`).

## Project Structure
```text
week6/
├── .gitignore             # Ignores cache and temporary files
├── requirements.txt       # requests
├── golden_set.json        # Curated evaluation dataset
├── main.py                # Evaluation runner and scoring pipeline
└── baseline_results.csv   # Generated baseline report
```

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Ensure Ollama is running:**
   ```powershell
   ollama run llama3.2
   ```

3. **Run the baseline evaluation:**
   ```powershell
   python main.py
   ```
