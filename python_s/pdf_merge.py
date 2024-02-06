from PyPDF2 import PdfReader, PdfWriter

PATH_TO_PDFS="/home/john/Downloads/"

def merge_pdfs(paths, output, pages):
    pdf_writer = PdfWriter()

    for i, path in enumerate(paths):
        pdf_reader = PdfReader(path)
        desired_pages = pages[i]
        for page in range(len(pdf_reader.pages)):
            if page in desired_pages:
            # Add each page to the writer object
                pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = [f'{PATH_TO_PDFS}lettuce.pdf', f'{PATH_TO_PDFS}lbmtheory.pdf', f'{PATH_TO_PDFS}unitopsprocedures.pdf', f'{PATH_TO_PDFS}selfreliance.pdf']
    pages = [[i for i in range(16)], [i for i in range(7)], [0, 6, 7, 8, 9, 14, 15, 16], [i for i in range(1,20)]]
    merge_pdfs(paths, output=f'{PATH_TO_PDFS}merged.pdf', pages=pages)
