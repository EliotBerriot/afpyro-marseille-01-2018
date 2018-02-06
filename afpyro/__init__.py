import collections


def get_place(edition=1):
    if edition == 1:
        return 'La Boate'
    if edition == 2:
        return 'Zenith'
    if edition == 3:
        return 'Stade Vélodrome'
    if edition == 4:
        return 'Palais du Pharo'
    raise ValueError("We don't know yet!")


def write_program(event, file_path):
    with open(file_path, 'a') as f:
        f.write(event)


def read_program(file_path):
    with open(file_path, 'r') as f:
        return [l for l in f.readlines()]


Mail = collections.namedtuple('Mail', ['body', 'recipient'])


def notify(recipients, program_path):
    agenda = ','.join(read_program(program_path))
    body_template = """
    Bonjour {recipient} !

    Voici un rappel du programme du prochain afpyro:

        {agenda}

    A très vite !
    """

    return [
        Mail(
            body_template.format(recipient=recipient, agenda=agenda),
            recipient)
        for recipient in recipients
    ]
