from project import pdf_to_text, clean_file, pdf_to_txt

words = pdf_to_txt("pdf_files/sample.pdf", "result.txt")
def test_pdf_to_text():
    assert pdf_to_text("pdf_files/sample.pdf", "output.txt") == True

def test_clean_file():
    assert clean_file("output.txt", "cleaned.txt") == True

def test_pdf_to_txt():
    assert pdf_to_txt("pdf_files/sample.pdf", "result.txt") == words