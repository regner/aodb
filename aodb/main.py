

import tarfile

from os import mkdir, listdir
from os.path import exists, isfile, join
from collections import defaultdict

from . import exporters
from.resources import RESOURCES


DEFAULT_INPUT = 'inputs/'
DEFAULT_OUTPUT = 'outputs/'


def get_input_path(name: str, input_folder: str = DEFAULT_INPUT) -> str:
    file_name = f'{name}.txt'
    return join(input_folder, file_name)


def get_output_version_folder(version: str, output_folder: str = DEFAULT_OUTPUT) -> str:
    return join(output_folder, version)


def get_output_path(name: str, version: str, output_folder) -> str:
    file_name = f'{version}-{name}.' + '{}'
    return join(output_folder, file_name)


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

        exporters.XmlExporter(input_path, output_path).generate_export()
        exporters.JsonExporter(input_path, output_path).generate_export()


def compress_exports(version: str):
    """Groups and compresses all the files based on file extension."""
    print('Compressing exported files...')

    files_by_extension = defaultdict(list)
    folder_path = get_output_version_folder(version)

    for file in listdir(folder_path):
        full_path = join(folder_path, file)

        if isfile(full_path):
            extension = file.split('.')[-1]

            if extension != 'gz':
                files_by_extension[extension].append(full_path)

    for extension, files in files_by_extension.items():
        print(f'Compressing {extension} files now...')

        full_path = join(folder_path, f'{version}-{extension}.tar.gz')

        with tarfile.open(full_path, 'w:gz') as out_file:
            for file in files:
                out_file.add(file)
