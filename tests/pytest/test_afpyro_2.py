import afpyro
import pytest


def test_afpyro_place_2():
    assert afpyro.get_place(edition=2) == 'Zenith'


def test_afpyro_place_3():
    assert afpyro.get_place(edition=3) == 'Stade Vélodrome'


def test_afpyro_place_4():
    assert afpyro.get_place(edition=4) == 'Palais du Pharo'


def test_afpyro_place_unknown():
    with pytest.raises(ValueError):
        afpyro.get_place(edition=42)


def test_afpyro_place_with_error():
    assert afpyro.get_place(1) == 'Paris'
