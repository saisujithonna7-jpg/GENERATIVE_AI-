# Week 2: Provider-Agnostic LLM Client

## Aim
To design and build a provider-agnostic LLM client using the Strategy/Adapter design pattern that provides a single uniform interface over both a cloud-hosted API (Google Gemini) and a local offline model (Ollama running `llama3.2`).

## Key Concepts
- **Provider-Agnostic Interface**: The client application interacts with `LLMClient.generate(prompt)` regardless of whether the model runs locally or in the cloud.
- **Abstract Base Class (`LLMProvider`)**: Enforces a strict contract requiring all provider adapters to implement `generate(prompt)`.
- **Unit Testing with Mocks**: Using a `FakeProvider` to test client logic without making real network calls or consuming tokens.

## Project Structure
```text
week2/
├── .env               # Stores GEMINI_API_KEY
├── .gitignore         # Keeps secrets out of version control
├── llm_client.py      # Core interfaces, GeminiProvider, OllamaProvider, LLMClient
├── main.py            # Interactive CLI application
├── test_client.py     # Unit test suite using unittest / pytest
└── requirements.txt   # Dependencies
```

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Ollama Setup (for local inference):**
   - Ensure Ollama is installed and running (`http://localhost:11434`).
   - Pull the model:
     ```powershell
     ollama pull llama3.2
     ```

3. **Run Unit Tests:**
   ```powershell
   python -m unittest test_client.py
   # or
   pytest test_client.py
   ```

4. **Run Application:**
   ```powershell
   python main.py
   ```
   Choose `gemini` or `ollama` when prompted and enter your question.
