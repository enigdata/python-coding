###Metadata Extraction and Rotating Pages
from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        num_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}:

    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of pages: {num_of_pages}
    """

    print(txt)
    return info

if __name__=='__main__':
    path = 'reportlab-sample.pdf'
    extract_information(path)

