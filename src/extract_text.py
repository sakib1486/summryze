import fitz

def extract_text(filepath=""):
    document = fitz.open(filepath)

    text = ""

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()

    return " ".join(text.split())