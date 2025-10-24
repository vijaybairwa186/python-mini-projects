# --> PDFMerger Merge PDFs using Python

from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

n = int(input("How many PDFs do you want to merge? "))

pdfs = []
for i in range(n):
    name = input(f"Enter the name of PDF {i + 1} (with or without .pdf extension): ").strip()
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    
    if os.path.exists(name):
        pdfs.append(name)
    else:
        print(f"File '{name}' not found. Skipping this one.")

for pdf in pdfs:
    merger.append(pdf)

output_name = input("Enter a name for the merged PDF (default: merged.pdf): ").strip()
if output_name == "":
    output_name = "merged.pdf"
elif not output_name.lower().endswith(".pdf"):
    output_name += ".pdf"

merger.write(output_name)
merger.close()

print(f"Successfully merged {len(pdfs)} PDF(s) into '{output_name}'.")
