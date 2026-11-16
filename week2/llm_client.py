from abc import ABC, abstractmethod
from google import genai
import requests


# Common interface
class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


# Gemini cloud provider
class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gemini-3.5-flash-lite"):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            return response.text
        except Exception:
            # Fallback in case of temporary 503 server load
            response = self.client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
            return response.text


# Ollama local provider
class OllamaProvider(LLMProvider):
    def __init__(self, model: str = "llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response is not None else None
            # Fallback to llama3.2:1b if llama3.2 is not yet found / downloaded
            if status_code == 404 and self.model != "llama3.2:1b":
                fallback_resp = requests.post(
                    self.url,
                    json={
                        "model": "llama3.2:1b",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=120
                )
                fallback_resp.raise_for_status()
                return fallback_resp.json()["response"]
            raise e


# Common client
class LLMClient:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
