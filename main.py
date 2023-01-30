from pdf2docx import Converter

pdf_file = "sample.pdf"
docx_file = "sample.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()