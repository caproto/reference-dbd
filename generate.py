import sys
import caproto.server.conversion

try:
    dbd_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    dbd_file = 'reference.dbd'
    output_file = sys.stdout
else:
    output_file = open(output_file, 'wt')

source = caproto.server.conversion.generate_all_records_jinja(dbd_file)
print(source, file=output_file)
