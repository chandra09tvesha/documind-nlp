
from src.preprocessing import (
    clean_text,
    tokenize_text,
    extract_keywords,
    get_text_statistics,
)


def test_clean_text():
    assert clean_text("Hello   world\n NLP") == "Hello world NLP"


def test_tokenize_text():
    assert tokenize_text("NLP is useful!") == [
        "nlp", "is", "useful"
    ]


def test_extract_keywords():
    result = extract_keywords(
        "Python Python data science data science models"
    )
    assert result[0] == "python"
    assert "science" in result


def test_text_statistics():
    text = "Python helps analyze data."
    result = get_text_statistics(text)
    assert result["word_count"] == 4
    assert result["unique_words"] == 4
    assert result["character_count"] == len(text)
