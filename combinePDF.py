''' Forked and enhanced, after the original: https://github.com/titse/PythonCombinePDF '''

import os
from PyPDF2 import PdfFileMerger

# Directory of the where script and py are located
fileDir = os.path.dirname(os.path.realpath(__file__))
print(f"This is fileDir: {fileDir}")

#pdf get all the pdfs to merge
pdfToMerge = [pdfIndex for pdfIndex in os.listdir(fileDir) if pdfIndex.endswith(".pdf")]
print("The files to merge are:")
print(pdfToMerge)
merger = PdfFileMerger()

for pdf in pdfToMerge:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)
    merger.close()

print("Done!")
