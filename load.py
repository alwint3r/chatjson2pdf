import optparse
import json
import mistune

def validate_options(options):
    if not options.filename:
        print('Filename is required')
        return False
    return True

def render_chat_block(message):
    role = message['role']
    content = message['content']
    
    formatted_role = role[0].upper() + role[1:]

    html_content = f"""
    <div style="margin-bottom: 16px; padding: 8px;">
        <div style="font-weight: bold; margin-bottom: 4px;">{formatted_role}</div>
        <div>{mistune.html(content)}</div>
    </div>
    """

    return html_content

def render_chat_page(messages):
    renderd_blocks = [render_chat_block(message) for message in messages]
    parent_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="initial-scale=1.0">
            <style>
                body {{
                    font-family: sans-serif;
                    font-size: 16px;
                    line-height: 1.5;
                }}
            </style>
        </head>
        <body>
            <div style="max-width: 600px; margin: 0 auto; padding: 16px;">
                {"".join(renderd_blocks)}
            </div>
        </body>
    </html>
    """

    return parent_content

def main(options, args):
    if not validate_options(options):
        return

    file = open(options.filename, 'r')
    json_data = json.loads(file.read())
    file.close()

    print(render_chat_page(json_data))

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', dest='filename', help='read data from FILENAME')
    (options, args) = parser.parse_args()
    main(options, args)