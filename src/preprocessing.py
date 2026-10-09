
import re
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer

TOKENIZER = TreebankWordTokenizer()

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "and", "or", "but", "if", "of", "to", "in",
    "on", "for", "with", "by", "as", "at", "it",
    "this", "that", "these", "those", "be", "been",
    "from", "has", "have", "had", "do", "does",
    "did", "not", "we", "you", "they", "their",
    "our", "your"
}


def clean_text(text: str) -> str:
    """Remove unwanted control characters and extra whitespace."""
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize_text(text: str) -> list[str]:
    """Split text into lowercase alphabetic words."""
    return [
        token.lower()
        for token in TOKENIZER.tokenize(text)
        if re.fullmatch(r"[A-Za-z]+", token)
    ]


def extract_keywords(text: str, limit: int = 10) -> list[str]:
    """Extract frequent keywords, excluding stopwords."""
    tokens = tokenize_text(text)

    keywords = [
        word for word in tokens
        if word not in STOPWORDS and len(word) > 2
    ]

    return [
        word for word, _ in Counter(keywords).most_common(limit)
    ]


def get_text_statistics(text: str) -> dict:
    """Calculate basic statistics about the document."""
    words = tokenize_text(text)

    return {
        "word_count": len(words),
        "unique_words": len(set(words)),
        "character_count": len(text),
        "keywords": extract_keywords(text),
    }
