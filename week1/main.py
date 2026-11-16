import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Load .env from the same directory as this file
load_dotenv(Path(__file__).parent / ".env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Add it to the .env file.")

client = genai.Client(api_key=api_key)

# Using gemini-3.5-flash-lite for fast, reliable response (avoids temporary 503 spikes on 3.7)
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words.",
)

print("\nLLM Response:")
print(response.text)
