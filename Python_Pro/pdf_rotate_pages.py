from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    #rotate page 90 degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)

    #rotate page 90 degrees to the left 
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)

    #rotate page upside down
    page_3 = pdf_reader.getPage(2).rotateCounterClockwise(180)
    pdf_writer.addPage(page_3)

    #add a page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(3))

    with open('rotated_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)

if __name__=="__main__":
    path = "Jupyter_Notebook.pdf"
    rotate_pages(path)