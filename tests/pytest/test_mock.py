import tempfile

import afpyro


def test_notify_calls_read_program(mocker):
    _, program_file = tempfile.mkstemp()
    read_program = mocker.spy(afpyro, 'read_program')
    afpyro.notify(['anna@conda.com'], program_file)

    read_program.assert_called_once_with(program_file)


def test_notify_sends_items_to_user(mocker):
    mocker.patch('afpyro.read_program', return_value=['TBD'])
    mails = afpyro.notify(['anna@conda.com'], '/wrong/path')

    for mail in mails:
        assert 'TBD' in mail.body
