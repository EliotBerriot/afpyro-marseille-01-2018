import afpyro
import pytest


@pytest.mark.parametrize('edition,expected', [
    (1, 'La Boate'),
    (2, 'Zenith'),
    (3, 'Stade Vélodrome'),
    (4, 'Palais du Pharo'),
])
def test_afpyro_get_place(edition, expected):
    assert afpyro.get_place(edition) == expected
