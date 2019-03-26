"""The main module."""
import click
import requests


@click.command()
@click.argument('file', type=click.File())
def fileget(file):
    """Takes a file, and downloads the images from the given URLs."""
    content = file.readlines()
    lines = [line.strip() for line in content]

    for url in lines:
        response = requests.get(url)

        file_name = url.split('/')[-1]

        with open(file_name, 'wb') as out_file:
            out_file.write(response.content)

        click.echo(url)
