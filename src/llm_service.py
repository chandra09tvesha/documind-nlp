
from functools import lru_cache

from google import genai
from google.genai import types

from config import (
    API_KEY,
    MODEL_NAME,
    MAX_OUTPUT_TOKENS,
    PROMPTS_DIR,
)


@lru_cache(maxsize=8)
def load_prompt(prompt_name: str) -> str:
    """Load and cache an approved prompt template."""

    allowed_prompts = {
        "summarization.txt",
        "question_answering.txt",
        "quiz_generation.txt",
    }

    if prompt_name not in allowed_prompts:
        raise ValueError("Unknown prompt template.")

    path = PROMPTS_DIR / prompt_name
    return path.read_text(encoding="utf-8")


def generate_response(prompt: str) -> str:
    """Send a prompt to Gemini and return its response."""

    if not API_KEY:
        raise RuntimeError(
            "Gemini API key is missing. Configure GEMINI_API_KEY."
        )

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=MAX_OUTPUT_TOKENS,
        ),
    )

    answer = response.text

    if not answer:
        raise RuntimeError("Gemini returned an empty response.")

    return answer.strip()


def summarize_document(document: str) -> str:
    template = load_prompt("summarization.txt")
    prompt = template.replace("{document}", document)
    return generate_response(prompt)


def answer_question(document: str, question: str) -> str:
    template = load_prompt("question_answering.txt")
    prompt = (
        template.replace("{document}", document)
        .replace("{question}", question)
    )
    return generate_response(prompt)


def generate_quiz(document: str) -> str:
    template = load_prompt("quiz_generation.txt")
    prompt = template.replace("{document}", document)
    return generate_response(prompt)
