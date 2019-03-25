import os
import click
import requests
from click.testing import CliRunner

def test_fileget():
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


    runner = CliRunner()
    with runner.isolated_filesystem():
        images = ("https://flowfx.de/images/flowfx.jpg\n"
                  "https://flowfx.de/images/flowfx.thumbnail.jpg")

        with open('images.txt', 'w') as f:
            f.write(images)

        result = runner.invoke(fileget, ['images.txt'])
        assert result.exit_code == 0
        assert result.output == f'{images}\n'

        assert os.path.isfile('flowfx.jpg') == True
        assert os.path.isfile('flowfx.thumbnail.jpg') == True
