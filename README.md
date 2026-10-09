# documind-nlp
NLP-based document intelligence system using an LLM API

# DocuMind NLP

DocuMind NLP is an AI-powered document understanding application that uses Natural Language Processing (NLP) and the Google Gemini API to analyze documents.

## Features

- Upload PDF and TXT documents
- Extract and clean document text
- Calculate word counts and identify keywords
- Generate document summaries
- Ask questions based on document content
- Generate multiple-choice quizzes

## Technologies Used

- Python
- Streamlit
- NLTK
- PyMuPDF
- Google Gemini API
- Pytest

## Project Structure

    documind-nlp/
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    ├── README.md
    ├── prompts/
    ├── src/
    └── tests/

## Installation

Install the dependencies:

    pip install -r requirements.txt

Create a `.env` file in the project root and add your Gemini API key:

    GEMINI_API_KEY=your_actual_api_key
    GEMINI_MODEL=gemini-2.5-flash

Never upload your actual API key to GitHub.

## Run the Application

    streamlit run app.py

## Run Tests

    python -m pytest -q

## Limitations

- Scanned PDFs may require OCR.
- Large documents are truncated to fit the processing limit.
- AI-generated answers may contain errors.
- API usage depends on Gemini availability and quotas.
