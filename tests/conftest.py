import pytest
from click.testing import CliRunner


@pytest.fixture(scope='module')
def isolated_filesystem_runner():
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner
