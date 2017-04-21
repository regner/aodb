

from os import mkdir
from os.path import exists

from . import exporters
from.resources import RESOURCES


DEFAULT_INPUT = 'inputs/'
DEFAULT_OUTPUT = 'outputs/'


def get_input_path(name: str, input_folder: str = DEFAULT_INPUT) -> str:
    return f'{input_folder}{name}.txt'


def get_output_version_folder(version: str, output_folder: str = DEFAULT_OUTPUT) -> str:
    return f'{output_folder}{version}/'


def get_output_path(name: str, version: str, output_folder) -> str:
    return f'{output_folder}{version}-{name}.' + '{}'


def generate_exports(version: str):
    """Generates the database conversions."""
    print('Generating exports...')

    output_folder = get_output_version_folder(version)
    if not exists(output_folder):
        mkdir(output_folder)

    for resource in RESOURCES:
        name = resource['name']
        print(f'Exporting {name}...')

        input_path = get_input_path(name)
        output_path = get_output_path(name, version, output_folder)

        exporters.XmlExporter(input_path, output_path).genreate_export()
        exporters.JsonExporter(input_path, output_path).genreate_export()


