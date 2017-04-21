

from . import exporters
from.resources import RESOURCES


DEFAULT_INPUT = 'inputs/'
DEFAULT_OUTPUT = 'outputs/'


def get_input_path(name: str, input_folder: str = DEFAULT_INPUT) -> str:
    return f'{input_folder}{name}.txt'


def get_output_path(name: str, output_folder: str = DEFAULT_OUTPUT) -> str:
    return f'{output_folder}{name}.' + '{}'


def generate_exports(version: str):
    """Generates the database conversions."""
    # Load the raw data
    # Run export

    print('Generating exports...')

    for resource in RESOURCES:
        name = resource['name']
        print(f'Exporting {name}...')

        input_path = get_input_path(name)
        output_path = get_output_path(name)

        exporters.XmlExporter(input_path, output_path).genreate_export()
        exporters.JsonExporter(input_path, output_path).genreate_export()


