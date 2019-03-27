"""Unit tests for the fileget module."""
from fileget.cli import clean_input


def test_clean_input_removes_empty_lines():
    content = ['  http://placekitten.com/200/200  ', '\n']

    assert clean_input(content) == ['http://placekitten.com/200/200']
