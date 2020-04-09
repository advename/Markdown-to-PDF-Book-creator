import pathlib
import os
from PyPDF2 import PdfFileMerger
workdir = pathlib.Path(__file__).parent.absolute()
workdir = f"{workdir}"
workdir.replace(os.sep, '/')

with open(f'{workdir}/../config.py', 'r', encoding='utf-8') as inf:
    config = eval(inf.read())

temp_dir = f"{workdir}/../temp"
cover_dir = f"{workdir}/../cover"

cover_name_pdf = "cover_page.pdf"
back_cover_name_pdf = "back_cover_page.pdf"
book_name_pdf = "temp_book.pdf"
final_book = f"{workdir}/../book.pdf"

pdfs = []

# Add front cover page
if not config['disable-cover-page']:
    pdfs.append(f'{cover_dir}/{cover_name_pdf}')

# Add book pdf pages from md
pdfs.append(f'{temp_dir}/{book_name_pdf}')

# Add back cover page
if not config['disable-back-cover-page']:
    pdfs.append(f'{cover_dir}/{back_cover_name_pdf}')

# Combine pdfs
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(pdf)

# Delete previous result book
if os.path.exists(final_book):
    os.remove(final_book)

merger.write(final_book)
merger.close()