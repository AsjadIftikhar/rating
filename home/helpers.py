import fitz


def pdf_to_string(file):
    with fitz.open(file) as doc:
        text = ""
        for page in doc:
            text += page.getText()

    return text
