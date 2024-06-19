import re
import sys

allowed_prefixes = ['r', 'v', 'i', 't', 'g', 'm', 'db', 'r3', 'ps']
allowed_prefixes_str = '|'.join(allowed_prefixes)
module_name_pattern = re.compile(fr'^({allowed_prefixes_str})\.[a-z0-9.]+[a-z0-9]$')

module_name = '{{ cookiecutter.tool }}'

if not re.match(module_name_pattern, module_name):
    # TODO: point to documentation what is valid name
    print(f'ERROR: {module_name} is not a valid addon name!')
    sys.exit(1)
