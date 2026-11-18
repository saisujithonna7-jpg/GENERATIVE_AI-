import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Ensure week3 is on sys.path
sys.path.insert(0, str(Path(__file__).parent))

from llm_client import GeminiProvider, OllamaProvider, LLMClient
from mongo_logger import MONGOLOGGER

# Load .env
load_dotenv(Path(__file__).parent / ".env", override=True)
load_dotenv(override=True)

usage_logger = MONGOLOGGER()

try:
    provider_name = input("Choose provider (gemini/ollama): ").strip().lower()

    if provider_name == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")
        provider = GeminiProvider(api_key)

    elif provider_name == "ollama":
        provider = OllamaProvider("llama3.2")

    else:
        raise ValueError("Invalid provider selected")

    client = LLMClient(provider, usage_logger)

    prompt = input("Enter your question: ")
    answer = client.generate(prompt)

    print("\nLLM Response:")
    print(answer)

finally:
    usage_logger.close()
