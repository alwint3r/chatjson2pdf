import optparse
import json

def validate_options(options):
    if not options.filename:
        print('Filename is required')
        return False
    return True

def main(options, args):
    if not validate_options(options):
        return

    file = open(options.filename, 'r')
    json_data = json.loads(file.read())
    file.close()

    print(f"Length: {len(json_data)}")

    for item in json_data:
        role = item['role']
        content = item['content']

        # capitalize the first letter of the role
        formatted_role = role[0].upper() + role[1:]
        print(f"{formatted_role}:\n{content}")
        print()

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', dest='filename', help='read data from FILENAME')
    (options, args) = parser.parse_args()
    main(options, args)