import optparse

def main(options, args):
    file = open(options.filename, 'r')
    print(file.read())

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', dest='filename', help='read data from FILENAME')
    (options, args) = parser.parse_args()
    main(options, args)