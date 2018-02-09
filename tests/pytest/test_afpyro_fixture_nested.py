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


@pytest.fixture
def populated_program_file(program_file):
    afpyro.write_program('TBD', program_file)
    return program_file


def test_read_program_file(populated_program_file):
    items = afpyro.read_program(populated_program_file)
    assert items == ['TBD']


def test_notify_participants(populated_program_file):
    participants = ['eliot@me.com', 'guido@van.rossum']
    mails = afpyro.notify(participants, populated_program_file)
    for mail in mails:
        assert 'TBD' in mail.body
