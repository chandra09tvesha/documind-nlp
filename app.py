
import streamlit as st

from config import MAX_DOCUMENT_CHARS
from src.document_loader import extract_document_text
from src.preprocessing import get_text_statistics
from src.llm_service import (
    summarize_document,
    answer_question,
    generate_quiz,
)

st.set_page_config(
    page_title="DocuMind NLP",
    layout="wide",
)

st.title("DocuMind NLP")
st.caption("AI-powered document understanding and summarization")

st.write(
    "Upload a PDF or TXT document to explore keywords, "
    "generate summaries, ask questions, and create quizzes."
)

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt"],
)

if uploaded_file is None:
    st.info("Upload a PDF or TXT file to get started.")
    st.stop()

try:
    document_text = extract_document_text(
        uploaded_file.name,
        uploaded_file.getvalue(),
    )
except Exception as exc:
    st.error(f"Could not read document: {exc}")
    st.stop()

if len(document_text) > MAX_DOCUMENT_CHARS:
    st.warning(
        f"Document exceeds {MAX_DOCUMENT_CHARS:,} characters. "
        "Only the beginning will be processed."
    )
    document_text = document_text[:MAX_DOCUMENT_CHARS]

stats = get_text_statistics(document_text)

st.success(f"Loaded: {uploaded_file.name}")

col1, col2, col3 = st.columns(3)
col1.metric("Words", f"{stats['word_count']:,}")
col2.metric("Unique words", f"{stats['unique_words']:,}")
col3.metric("Characters", f"{stats['character_count']:,}")

with st.expander("View extracted text"):
    st.text(document_text[:5000])

with st.expander("Explore NLP keywords"):
    st.write(", ".join(stats["keywords"]) or "No keywords found.")

summary_tab, qa_tab, quiz_tab = st.tabs(
    ["Summarize", "Ask a Question", "Generate a Quiz"]
)

with summary_tab:
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            try:
                st.session_state["summary_result"] = (
                    summarize_document(document_text)
                )
            except Exception as exc:
                st.error(f"Summary generation failed: {exc}")

    if st.session_state.get("summary_result"):
        st.markdown(st.session_state["summary_result"])

with qa_tab:
    question = st.text_input(
        "Enter your question",
        placeholder="What are the main findings?",
    )

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                try:
                    st.session_state["qa_result"] = answer_question(
                        document_text,
                        question.strip(),
                    )
                except Exception as exc:
                    st.error(f"Answer generation failed: {exc}")

    if st.session_state.get("qa_result"):
        st.markdown(st.session_state["qa_result"])

with quiz_tab:
    if st.button("Generate 5 Questions"):
        with st.spinner("Creating quiz..."):
            try:
                st.session_state["quiz_result"] = generate_quiz(
                    document_text
                )
            except Exception as exc:
                st.error(f"Quiz generation failed: {exc}")

    if st.session_state.get("quiz_result"):
        st.markdown(st.session_state["quiz_result"])

st.divider()
st.caption(
    "DocuMind NLP | Python | NLTK | Gemini API | Streamlit"
)
