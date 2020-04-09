# Auto generate the metadata file for pandoc based on config.json
# Can be disabled by setting "disable-auto-pandoc-metadata-builder" to true in config.py
import pathlib
import os
workdir = pathlib.Path(__file__).parent.absolute()

workdir = f"{workdir}"
workdir.replace(os.sep, '/')

with open(f'{workdir}/../config.py', 'r', encoding='utf-8') as inf:
    config = eval(inf.read())
yaml_template = f"""
---
title: {config['title']}
rights: {config['license']}
lang: {config['license']}
tags: {config['tags']}
abstract: |
 {config['description']}
mainfont: {config['mainfont']}

# Filter preferences:
# - pandoc-crossref
linkReferences: true

---

"""

if not config['disable-auto-pandoc-metadata-builder']:
    file_name = f'{workdir}/../metadata.yaml'
    f = open(file_name, 'w+', encoding="utf8")  # open file in append mode
    f.write(yaml_template)
    f.close()
    print("# Metadata file generated")
