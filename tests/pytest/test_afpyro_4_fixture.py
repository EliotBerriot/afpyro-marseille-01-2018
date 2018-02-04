import afpyro
import os
import tempfile
import pytest


@pytest.fixture
def program_file():
    _, f = tempfile.mkstemp()
    yield f
    # clean
    os.remove(f)


def test_write_afpyro_program(program_file):
    afpyro.write_program('Introduction to pytest', program_file)
    with open(program_file) as f:
        assert f.read() == 'Introduction to pytest'
