import os
import sys
import subprocess
import pathlib
workdir = pathlib.Path(__file__).parent.absolute()
workdir.name.replace(os.sep, '/')

os.system(f'python {workdir}/scripts/pandoc_yaml_metadata_maker.py')
os.system(f'python {workdir}/scripts/md_to_html.py')
os.system(f'python {workdir}/scripts/html_to_pdf.py')
os.system(f'python {workdir}/scripts/cover_back_page_combiner.py')