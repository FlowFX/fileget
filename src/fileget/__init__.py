import click
import requests


@click.command()
@click.argument('f', type=click.File())
def fileget(f):
    content = f.readlines()
    lines = [line.strip() for line in content]

    for url in lines:
        response = requests.get(url)

        file_name = url.split('/')[-1]

        with open(file_name, 'wb') as out_file:
            out_file.write(response.content)

        click.echo(url)
