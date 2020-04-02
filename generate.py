import sys
import caproto
import caproto.server.conversion

to_generate = sys.argv[1]

if to_generate not in {'menus', 'records'}:
    print('Please specify "menus" or "records"')
    sys.exit(1)

try:
    dbd_file = sys.argv[2]
    output_file = sys.argv[3]
except IndexError:
    dbd_file = 'reference.dbd'
    output_file = sys.stdout
else:
    output_file = open(output_file, 'wt')

if to_generate == 'menus':
    source = caproto.server.conversion.generate_all_menus_jinja(dbd_file)
elif to_generate == 'records':
    source = caproto.server.conversion.generate_all_records_jinja(dbd_file)

print(f'Suggested git commit message:', file=sys.stderr)
print(f'MNT: Generating {to_generate}.py from caproto {caproto.__version__}',
      file=sys.stderr)
print(source, file=output_file)
