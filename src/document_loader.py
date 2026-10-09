
import fitz

from src.preprocessing import clean_text


def extract_document_text(filename: str, file_bytes: bytes) -> str:
    """Extract text from PDF or TXT files."""

    extension = filename.lower().rsplit(".", 1)[-1]

    if extension == "pdf":
        pages = []

        with fitz.open(stream=file_bytes, filetype="pdf") as document:
            for page in document:
                pages.append(page.get_text("text"))

        text = "\n".join(pages)

    elif extension == "txt":
        text = file_bytes.decode("utf-8-sig", errors="replace")

    else:
        raise ValueError(
            "Unsupported file type. Upload a PDF or TXT file."
        )

    text = clean_text(text)

    if not text:
        raise ValueError(
            "No readable text found. The PDF may be scanned "
            "or image-based and may require OCR."
        )

    return text
