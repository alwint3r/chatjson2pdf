# Render JSON of Chat History to PDF

Supported format:
```json
[
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi, how can I help you?"}
]
```

## Pre-requisites

### Install Requirements

```bash
pip3 install mistune xhtml2pdf
```


## Usage

### Rendering Chat JSON to HTML

```bash
python3 render_html.py -f <path/to/chat.json> -o <path/to/output.html>
```

Then

```bash
python3 render_pdf.py -f <path/to/output.html> -o <path/to/output.pdf>
```
