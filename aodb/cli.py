

import click

from .main import generate_exports


@click.command()
@click.option('-v', '--version', required=True, type=str, help='The version number to label the output with.')
def generate(version: str):
    """CLI wrapper for the main generate function."""
    generate_exports(version)
