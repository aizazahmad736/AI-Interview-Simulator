import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Gemini model selection
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

def is_api_key_configured(api_key: str = None) -> bool:
    """Check if a valid Gemini API key is available."""
    key = (api_key or GEMINI_API_KEY).strip()
    return bool(key and key != "your_gemini_api_key_here" and len(key) >= 15)
