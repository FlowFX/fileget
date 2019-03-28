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


def item_show_func(item):
    print(str(item))


@click.command()
@click.argument('file', type=click.File())
def cli(file):
    """Takes a file, and downloads the images from the given URLs."""
    content = file.readlines()

    lines = clean_input(content)
    print(len(lines))

    click.secho('Hello World!', fg='green')
    click.echo(click.style('ERROR', fg='red'))

    with click.progressbar(lines, item_show_func=item_show_func) as bar:
        for url in bar:
            # click.echo(Downloading url …)
            response = requests.get(url)

            # click.echo(DONE / ERROR):w


            # if 

            file_name = url.split('/')[-1]

            with open(file_name, 'wb') as out_file:
                out_file.write(response.content)

            # click.echo(url)
