"""The main module."""
import click
import requests


def clean_input(content):
    """Clean input file and return only valid URLs."""
    # Remove white space and return a list
    lines = [line.strip() for line in content]

    # Filter out empty strings
    lines = list(filter(None, lines))

    return lines


@click.command()
@click.argument('file', type=click.File())
def cli(file):
    """Takes a file, and downloads the images from the given URLs."""
    content = file.readlines()

    lines = clean_input(content)

    for url in lines:
        response = requests.get(url)

        file_name = url.split('/')[-1]

        with open(file_name, 'wb') as out_file:
            out_file.write(response.content)

        click.echo(url)
