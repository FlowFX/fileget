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


def test_empty_file(isolated_filesystem_runner):
    # GIVEN an empty input file
    images = ''

    with open('images.txt', 'w') as file:
        file.write(images)

    # WHEN executing the script
    result = isolated_filesystem_runner.invoke(fileget, ['images.txt'])

    # THEN it returns success and no output
    assert result.exit_code == 0
    assert result.output == ''


def test_no_file(isolated_filesystem_runner):
    # GIVEN no input file
    # WHEN executing the script
    result = isolated_filesystem_runner.invoke(fileget)

    # THEN it exits with an error
    assert result.exit_code != 0

    # AND displays a help text
    expected = 'Usage: fileget [OPTIONS] FILE'
    assert expected in result.output
