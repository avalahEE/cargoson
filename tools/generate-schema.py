import argparse
import json
import os.path
import re
import sys
from jsonschemagen import generate_jsonschema_class

TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')


def get_schemas(options):
    openapi_data = json.load(options.schema)
    if 'components' not in openapi_data or 'schemas' not in openapi_data['components']:
        raise Exception('OpenAPI schemas not found in input file')
    return openapi_data['components']['schemas']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('schema', help='Schema file', type=argparse.FileType('r'))
    parser.add_argument('-v', help='Verbose logging', action='store_true')
    options = parser.parse_args()

    python_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'delivery_cargoson', 'models', 'schema'))
    schema_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'schema'))

    try:
        schemas = get_schemas(options)
        imports = list()
        for name in sorted(schemas.keys()):
            print(f'# [+] Generating class: {name}')
            py_src = generate_jsonschema_class(name, schemas[name])
            if options.v:
                print(py_src)

            file_name = TO_SNAKE.sub('_', name).lower()
            output_path = os.path.join(python_dir, f'{file_name}.py')
            with open(output_path, 'w') as fd:
                fd.write(py_src)
            imports.append(f'from .{file_name} import {name}')

            json.dump(
                schemas[name],
                open(os.path.join(schema_dir, f'schema_{file_name}.json'), 'w'),
                indent=4
            )

        # overwrite __init__.py
        with open(os.path.join(python_dir, '__init__.py'), 'w') as fd:
            fd.write('\n'.join(imports))
            fd.write('\n')

    except Exception as err:
        print(f'/!\\ Error: {err}')
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
