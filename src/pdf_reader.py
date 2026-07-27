import pdfplumber


def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.

    Parameters:
        pdf_file: Uploaded PDF file from Streamlit

    Returns:
        Extracted text
    """

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text