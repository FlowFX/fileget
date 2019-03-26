"""Pytest fixtures."""
import pytest
from click.testing import CliRunner


@pytest.fixture(scope='module')
def isolated_filesystem_runner():
    """Fixture to run a test in a temporary and isolated filesystem."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner
