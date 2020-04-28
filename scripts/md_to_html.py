import os
from os.path import isfile, join
from os import listdir
import subprocess
import re
import json
import pathlib
workdir = pathlib.Path(__file__).parent.absolute()
workdir.name.replace(os.sep, '/')

# Get config file
with open(f'{workdir}/../config.py', 'r', encoding='utf-8') as inf:
    config = eval(inf.read())

# Set global file/dir names
helpers_dir = f"{workdir}/../helpers"
markdown_files_dir = f"{workdir}/../markdown_files"
temp_dir = f"{workdir}/../temp"

book_name_md = "book.md"
book_name_html = "book.html"

metadata_file = f"{workdir}/../metadata.yaml"

jquery_url = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"

# Add javascript files
javascript_files = ['prism.js', 'fname_block_fixer.js', 'general_script.js']
javascript = f"<script src='{jquery_url}'></script>"  # needs to start with jQUery
for file in javascript_files:
    javascript += f"<script src='../helpers/{file}'></script>"

if os.path.exists(f"{temp_dir}/{book_name_md}"):
    os.remove(f"{temp_dir}/{book_name_md}")

#combine only retrieved markdown files.
markdown_files = [
    os.path.join(root, name)
    for root, dirs, files in os.walk(f"{markdown_files_dir}") for name in files
    if name.endswith(".md")
]


#put append and source to end if they exists
files_to_the_end = ["Appendix.md","Source.md"]
for item in files_to_the_end:
	for md in markdown_files:
		if md.endswith(item):
			markdown_files.append(markdown_files.pop(markdown_files.index(md)))


markdown_text = "\n\n\\newpage\n"  # start with new page because of Table of contents

# Put them together and add \newpage to the end except last page
for i, file in enumerate(markdown_files):
    with open(file, 'r', encoding="utf8") as file:
        markdown_text += file.read()
        if not i == len(markdown_files) - 1:
            markdown_text += "\n\n\\newpage\n"

# add newpage to h2 too. If previous line is an h1, dont do it.
markdown_text_list = markdown_text.split("\n")
for i, line in enumerate(markdown_text_list):
    if line.startswith("## "):
        if not markdown_text_list[i - 1].startswith("# "):
            # Add new pages after each h2
            markdown_text_list[i] = markdown_text_list[i].replace(
                "\n## ", "\n\n\\newpage\n## ")
markdown_text = "\n".join(markdown_text_list)

# Make sure there is an empty new line before each list start, else lists wont work
markdown_text_array = markdown_text.splitlines()
for i, line in enumerate(markdown_text_array):
    if line:
        if line[0] == "-":
            if not markdown_text_array[i - 1][0] == "-":
                markdown_text_array[i] = f"\n{line}"
markdown_text = "\n".join(markdown_text_array)

# Write to one combined md file
book_markdown = open(f"{temp_dir}/{book_name_md}", 'wb')
book_markdown.write(markdown_text.encode("utf8"))
book_markdown.close()

# --lua-filter=pagebreak.lua is needed to use page breaks
command = f"pandoc {temp_dir}/{book_name_md} -s -o {temp_dir}/{book_name_html} --css=../helpers/pandoc.css -t html5 --lua-filter={helpers_dir}/pagebreak.lua {metadata_file} --lua-filter={helpers_dir}/syntax_code_fix.lua --css=../helpers/prism.css"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# Edit html to work with prism
with open(f"{temp_dir}/{book_name_html}", 'r', encoding="utf8") as file:
    html_text = file.read()
html_text = html_text.replace(
    "<body>", '<body class="line-numbers"/>')  # add line number
html_text = html_text.replace("</body>", f"{javascript}</body>")

wr = open(f"{temp_dir}/{book_name_html}", 'w', encoding="utf8")
wr.write(html_text)

print("# Temp .md and .html files generated")