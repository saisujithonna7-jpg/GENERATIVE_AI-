# Week 1: Introduction to Generative AI with Google Gemini API

## Aim
To set up the development environment, securely configure API credentials, and generate text completions using the Google GenAI SDK.

## Requirements
- Python 3.10+
- `google-genai`
- `python-dotenv`

## Project Structure
```text
week1/
├── .env               # Stores GEMINI_API_KEY (git-ignored)
├── .gitignore         # Ignores sensitive environment files
├── main.py            # Main application script
└── requirements.txt   # Project dependencies
```

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Configure `.env` file:**
   Create a `.env` file in `week1/`:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```

3. **Run the script:**
   ```powershell
   python main.py
   ```

## Output
The script connects to the Gemini model and generates an explanation of Artificial Intelligence in plain English.
