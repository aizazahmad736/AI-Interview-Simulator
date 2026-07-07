import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")