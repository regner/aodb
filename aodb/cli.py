

import click

from .main import generate


@click.command()
@click.option('--version', required=True, type=str, help='The version number to label the output with.')
def generate(version: str):
    """CLI wrapper for the main generate function."""
    generate(version)
