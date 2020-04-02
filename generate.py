import sys
import caproto
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
print(f'Suggested git commit message:', file=sys.stderr)
print(f'MNT: Generating records.py from caproto {caproto.__version__}',
      file=sys.stderr)
print(source, file=output_file)
