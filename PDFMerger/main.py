import PyPDF2

merger= PyPDF2.PdfWriter()

pdfs=["dummy.pdf","dummmy2.pdf","dummy3.pdf"]

for pdf in pdfs:
  merger.append(pdf)

merger.write("newPdf.pdf")
