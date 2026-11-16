# Week 3: LLM Observability & Monitoring with MongoDB

## Aim
To extend the provider-agnostic client by adding full observability and monitoring. The client measures latency, captures input/output tokens, computes estimated API costs, logs every request into a MongoDB Atlas database, and includes timeout and retry mechanisms for fault tolerance.

## Key Concepts
- **Token Tracking**: Capturing `prompt_token_count` and `candidates_token_count` from Gemini metadata, and `prompt_eval_count` / `eval_count` from Ollama.
- **Latency Measurement**: Accurate request duration timing using `time.perf_counter()`.
- **Cost Estimation**: Dynamic pricing calculation based on per-million token rates configured in `.env`.
- **Fault Tolerance**: Automatic exponential backoff retries (1s, 2s) for transient HTTP errors (408, 429, 500, 502, 503, 504) and connection timeouts.
- **Persistent Logging**: Storing request metadata in MongoDB Atlas (`llm_monitoring` database, `api_usage` collection).

## Project Structure
```text
week3/
├── .env               # GEMINI_API_KEY, MONGODB_URI, pricing rates
├── .gitignore         # Prevents committing .env and cache
├── usage_logger.py    # MongoDB connection and usage logging logic
├── llm_client.py      # LLMProvider, GeminiProvider, OllamaProvider, LLMClient with retries
├── main.py            # Main interactive monitoring application
├── test_client.py     # Unit test with FakeProvider and FakeLogger
└── requirements.txt   # Dependencies
```

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Configure `.env` file:**
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   GEMINI_INPUT_PRICE_PER_MILLION=0
   GEMINI_OUTPUT_PRICE_PER_MILLION=0
   ```

3. **Run Unit Tests:**
   ```powershell
   python -m unittest test_client.py
   ```

4. **Run the Application:**
   ```powershell
   python main.py
   ```

5. **Verify Logs in MongoDB Atlas:**
   Log in to [cloud.mongodb.com](https://cloud.mongodb.com) -> **Clusters** -> **Browse Collections** -> Database `llm_monitoring` -> Collection `api_usage`.
