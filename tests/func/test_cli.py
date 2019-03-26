"""System level tests of the fileget module."""
import os

from fileget import fileget


def test_fileget(isolated_filesystem_runner):
    images = ("https://flowfx.de/images/flowfx.jpg\n"
              "https://flowfx.de/images/flowfx.thumbnail.jpg")

    with open('images.txt', 'w') as file:
        file.write(images)

    result = isolated_filesystem_runner.invoke(fileget, ['images.txt'])
    assert result.exit_code == 0
    assert result.output == f'{images}\n'

    assert os.path.isfile('flowfx.jpg')
    assert os.path.isfile('flowfx.thumbnail.jpg')
