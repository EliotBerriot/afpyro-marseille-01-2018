import afpyro


def test_afpyro_get_place():
    choices = [
        (1, 'La Boate'),
        (2, 'Zenith'),
        (3, 'Stade Vélodrome'),
        (4, 'Palais du Pharo'),
    ]
    for edition, expected in choices:
        assert afpyro.get_place(edition) == expected
