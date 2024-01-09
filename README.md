# Render JSON of Chat History to PDF

## Pre-requisites

### Install Requirements

_As of now, the requirements.txt may include unnecessary packages. I will clean this up later._

```bash
pip3 install mistune xhtml2pdf
```


## Usage

### Rendering Chat JSON to HTML

```
python3 render_html.py -f <path/to/chat.json> -o <path/to/output.html>
```

Then

```
python3 render_pdf.py -f <path/to/output.html> -o <path/to/output.pdf>
```
