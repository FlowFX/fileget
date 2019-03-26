import os
from click.testing import CliRunner

from fileget import fileget


def test_fileget():
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
