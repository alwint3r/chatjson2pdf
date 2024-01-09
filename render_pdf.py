from xhtml2pdf import pisa
import optparse

def write_html_to_pdf(html_content, output_file):
    pisa_status = pisa.CreatePDF(html_content, dest=output_file)
    return pisa_status.err

def main(options, args):
    if not options.filename:
        print('HTML input filename is required')
        exit()

    if not options.output:
        print('Output file path is required')
        exit()

    html_file = open(options.filename, 'r')
    html_content = html_file.read()

    with open(options.output, 'wb') as output_file:
        err = write_html_to_pdf(html_content, output_file)
        if err:
            print('Error while rendering PDF')
        else:
            print('PDF successfully generated')


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('-f', '--filename', dest='filename',
                      help='HTML input filename')
    parser.add_option('-o', '--output', dest='output', help='Output file path')
    (options, args) = parser.parse_args()
    main(options, args)