import pymupdf


def extract(file_path: str) -> str:
    """
    Extracts text from a PDF file and processes it.
    """

    text: str = ""

    with pymupdf.open(file_path) as pdf:
        for i in range(pdf.page_count):
            text += " " + pdf.load_page(i).get_text()
    
    return text.strip()
