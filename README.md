# Markdown to PDF Book creator
Converts a bunch of markdown files into a book looking pdf.
This creator is made for writers who wish to publish **programming** books but can be used for other purposes.

You can see the results by inspecting the files inside **/markdown_files** and **/cover** directory and the final result, the **book.pdf** file in the root.

**Because of a current bug**, make sure that the folder this repository is saved in, and all its parents directories DO NOT CONTAIN SPACES. Else the create_book.py file fails.

## Features

- Use css files to style your book
- Use cover and back cover pages
- Beautiful syntax highlighter with line number and file name for code blocks
- Supports all available Prism syntax highlighting languages (https://prismjs.com/)
- Multiple markdown files into one
- Jumps to a new page after each h1 and h2 (only if the direct previous line is not and h1)
- Auto generated Table of contents based on h1, h2 and h3
- Single configuration file `config.py` or fully configurable by editing the source code ;)
- Uses Pandoc, wkhtmltopdf and Python under the hood.



### Requirements:
You need to install:
- wkhtmltopdf - https://wkhtmltopdf.org/
- Pandoc -https://pandoc.org/installing.html
- LaTeX (See https://tug.org/mactex/ on OS X, https://miktex.org/ on Windows, or install the texlive package on Linux.
- Python  - https://www.python.org/downloads/

Visit the respective pages for installation instructions.

### Basic usage
1. Download and extract the files to a directory
2. Install pdfkit (python package)  `pip install pdfkit`
3. Place all your files in the `/markdown_files` directory
4. Make sure the markdown files are alphabetically sorted (0-9, then A - z)
5. Edit the config.py file to your needs
6. Create a front cover page and back cover page by creating `cover_page.pdf` and `back_cover_page.pdf` files in the `/cover` directory. These files will be combined with your markdown files and are not part of the Table of contents or page numbering.
7. Run `python create_book.py` in the project directory
8. Your book



## Configurations

### config.py

The config.py file provides information to Pandoc (md to html), wkhtmltopdf (html to pdf using pdfkit) and Python (general settings).

These attributes are used for autogenerating metadata.yaml:

```
	"title":"Birdy book",
	"license": "MIT License",
	"lang": "en-us",
	"tags": "[book, birds, sky]",
	"description": "My personal book",
	"mainfont": "Source Sans Pro",
```

You can, of course use your own metadata.yaml file setting  `	"disable-auto-pandoc-metadata-builder" : True`.



All attributes inside the `html-to-pdf-options` dictionary are direct parameters with values taken from the wkhtmltopdf documentation page (https://wkhtmltopdf.org/usage/wkhtmltopdf.txt). Use those which you need.



You can disable cover pages with: `"disable-cover-page" : True`

You can disable back cover pages with: `"disable-back-cover-page": True`



### Code block file naming

You can indicate to the reader which file the code block belongs to. Using the custom file name tag as shown below:

```
__<fname>file.txt</fname>__
​```
"Hello world"
​```
```

The `__<fname> FILE_NAME </fname>__` syntax needs to be placed directly above the code block. In markdown, the file name is bold.  The PDF highlights the file name with a blue background.



### Belongs together

If you wish to keep items together on one page, you can wrap them around using `<div class="belongs-together"> ... </div>` wrapper to inform the creator NOT to separate them over multiple pages. This can be helpful for example when you have images with descriptions that need to stay together.

```
<div class="belongs-together">

![Image 1](https://example.com/image1)
An image of flying birds.

</div>
```

