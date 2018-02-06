
def hello(name):
    return 'Hello {}!'.format(name)


def test_hello():
    expected = 'Hello Eliot!'
    assert hello('Eliot') == expected
