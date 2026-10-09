
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

MAX_DOCUMENT_CHARS = 30000
MAX_OUTPUT_TOKENS = 2048

PROMPTS_DIR = BASE_DIR / "prompts"
