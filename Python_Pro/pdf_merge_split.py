from PyPDF2 import PdfFileReader, PdfFileWriter

# def merge_pdfs(paths, output):
#     pdf_writer = PdfFileWriter()

#     for path in paths:
#         pdf_reader = PdfFileReader(path)
#         for page_num in range(pdf_reader.getNumPages()):
#             #add each page to the writer object
#             pdf_writer.addPage(pdf_reader.getPage(page_num))

#     #write out the merged PDF
#     with open(output, 'wb') as f:
#         pdf_writer.write(out)

# if __name__ == '__main__':
#     paths = ['doc1.pdf', 'doc2.pdf']
#     merge_pdfs(paths, output='merged.pdf')

#### Splitting PDFs

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page_num in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page_num))

        output = f'{name_of_split}{page_num}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__=='__main__':
    path = "Jupyter_Notebook.pdf"
    split(path, 'Jupyter_page')