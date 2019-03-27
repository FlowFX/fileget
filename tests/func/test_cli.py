"""System level tests of the fileget module."""
import os
import magic

from fileget import fileget


def test_fileget(isolated_filesystem_runner):
    # GIVEN a text file with URLs to existing files on the internets
    images = ("https://flowfx.de/images/flowfx.thumbnail.jpg\n"
              "http://placekitten.com/200/200")

    with open('images.txt', 'w') as file:
        file.write(images)

    # WHEN executing the script
    result = isolated_filesystem_runner.invoke(fileget, ['images.txt'])

    # THEN it returns success and displays the filenames that have been
    # downloaded
    assert result.exit_code == 0
    assert result.output == f'{images}\n'

    # AND the files are actually doenloaded to the local file system
    assert os.path.isfile('flowfx.thumbnail.jpg')
    assert os.path.isfile('200')

    # AND the files are actually image files
    assert magic.from_file('flowfx.thumbnail.jpg', mime=True) == 'image/jpeg'
    assert magic.from_file('200', mime=True) == 'image/jpeg'


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
