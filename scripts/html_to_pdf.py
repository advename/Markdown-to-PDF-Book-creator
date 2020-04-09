import os
from os.path import isfile, join
from os import listdir
import subprocess
import re
import json
import pdfkit
import pathlib
workdir = pathlib.Path(__file__).parent.absolute()
# workdir.name.replace(os.sep, '/')

# Get config file
with open(f'{workdir}/../config.py', 'r', encoding='utf-8') as inf:
    config = eval(inf.read())
# print(config['html-to-pdf-options'])

# Set global file/dir names
helpers_dir = f"{workdir}/../helpers"
markdown_files_dir = f"{workdir}/../markdown_files"
temp_dir = f"{workdir}/../temp"

book_name_md = "book.md"
book_name_html = "book.html"
book_name_pdf = "temp_book.pdf"

metadata_file = f"{workdir}/../metadata.yaml"

# Remove pdf if already exists
if os.path.exists(f"{temp_dir}/{book_name_pdf}"):
    os.remove(f"{temp_dir}/{book_name_pdf}")

options = config['html-to-pdf-options']

pdfkit.from_file(f"{temp_dir}/{book_name_html}",
                 f"{temp_dir}//{book_name_pdf}",
                 options=options)

# Delete temp book.md
# if os.path.exists(book_name_md):
#   os.remove(book_name_md)
