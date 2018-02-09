import random


def test_random():
    choices = range(10)
    assert random.choice(choices) % 2 == 0
