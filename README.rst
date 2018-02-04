Apfyro #1
=========


Pytest: introduction, trucs et astuces


Introduction
------------

- Pour exécuter les tests (marche aussi avec les tests unittests)
- Pour écrire les tests

Le meilleur des deux mondes: pour écrire et lancer les tests

Installation
------------

    pip install pytest

Premier test
------------

.. code-block:: python

    # afpyro/__init__.py
    def get_place(edition=1):
        if edition == 1:
            return 'La Boate'
        if edition == 2:
            return 'Zenith'
        if edition == 3:
            return 'Stade Vélodrome'
        if edition == 4:
            return 'Palais du Pharo'
        raise ValueError('We don\'t know yet!')

    # tests/test_afpyro.py
    import afpyro

    def test_afpyro_place():
        assert afpyro.get_place() == 'La Boate'


Lancement::

    pytest tests/test_afpyro.py


Plus de tests:

.. code-block:: python

    # tests/test_afpyro.py
    def test_afpyro_place_2():
        assert afpyro.get_place(edition=2) == 'Zénith'

    def test_afpyro_place_3():
        assert afpyro.get_place(edition=3) == 'Stade Vélodrome'

    def test_afpyro_place_4():
        assert afpyro.get_place(edition=4) == 'Palais du Pharo'

    def test_afpyro_place_unknown():
        with pytest.raises(ValueError):
            afpyro.get_place(edition=42)

    def test_afpyro_place_with_error():
        assert afpyro.get_place(1) == 'Paris'

- Les assertions utilisent le mot clé assert de python
- L'affichage en cas d'erreur est amélioré pour faciliter le débug

Options pratiques
-----------------

- -x pour stopper sur la première erreur
- --lf pour relancer uniquement les tests ayant échoués
- -v pour jouer sur la verbosité
- lancer un module, un fichier ou un test en particulier
- --pdb pour ouvrir un shell pdb lors d'une erreur

Pytest.ini
----------

Configuration pour pytest pour simplifier l'exécution:

- tests_path pour spécifier le chemin par défaut des tests
- addopts pour spécifier des options par défaut

Fixtures
--------

Rien à voir avec les fixtures de l'écosystème django.

Permet de passer de l'état, des utilitaires ou de faire de l'initialisation ou
du nettoyage avant un test.

Exemple avec unittest:

.. code-block:: python

    import afpyro
    import shutil
    import unittest
    import tmpdir

    class TestLog(unittest.TestCase):
        def setUp():
            self.program_file = tmpdir.mktempfile()

        def tearDown():
            shutil.rmtree(self.program_file)

        def test_write_afpyro_program(self):
            afpyro.write_program('Introduction to pytest', self.program_file)
            with open(self.program_file) as f:
                self.assertEqual(f.read(), 'Introduction to pytest')


Le même code avec une fixture:

.. code-block:: python

    import afpyro
    import shutil
    import tmpdir
    import pytest

    @pytest.fixture
    def program_file():
        f = tmpdri.mktempfile()
        yield f
        # clean
        shutil.rmtree(f)

    def test_write_afpyro_program(program_file):
        afpyro.write_program('Introduction to pytest', program_file)
        with open(program_file) as f:
            assert f.read() == 'Introduction to pytest'

Avantages:

- Fini les 16 niveaux d'héritages sur les classes de tests pour avoir les bonnes
  méthodes et le bon état
- Encapsulation du setup et du teardown dans la même fonction, donc plus de lisibilité
- On sait exactement quel test a besoin de quoi directement dans la signature
  de la fonction

Les fixtures peuvent dépendre les unes des autres:

.. code-block:: python

    @pytest.fixture
    def program_file():
        f = tmpdri.mktempfile()
        yield f
        # clean
        shutil.rmtree(f)

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

On peut donc écrire des fixtures très bas niveau, et les combiner pour faire
des fixtures plus puissantes, sans perdre en souplesse.


Parametrize
-----------

TL;DR: Générer des tests dynamiquements.

Pourquoi ? Éviter de se répêter. Si je reprend mon exemple du début, on voit que
j'ai 4 tests qui font quasiment exactement la même chose.

On pourrait factoriser avec une boucle for:

.. code-block:: python

    def test_afpyro_get_place():
        choices = [
            (1, 'La Boate'),
            (2, 'Zenith'),
            (3, 'Stade Vélodrome'),
            (4, 'Palais du Pharo'),
        ]
        for edition, expected in choices:
            assert afpyro.get_place(edition) == expected

Inconvenients de cette méthode:

- Une boucle à écrire à la main
- Si une des assertions fail, le test plante et les suivantes ne sont pas jouées
- idéalement, un test ne doit tester qu'une seule chose

Parametrize implémente ce pattern de façon transparente, mais en générant
un test pour chaque élément de la boucle:

.. code-block:: python

    # tests/test_afpyro.py
    import afpyro
    import pytest

    @pytest.parametrize('edition,expected', [
        (1, 'La Boate'),
        (2, 'Zenith'),
        (3, 'Stade Vélodrome'),
        (4, 'Palais du Pharo'),
    ])
    def test_afpyro_get_place(edition, expected):
        assert afpyro.get_place(edition) == expected

En interne, pytest va générer 4 tests distincts, un pour chaque ligne
de l'itérable passé en second argument de parametrize.


Plugins utiles
--------------

pytest-sugar
++++++++++++
Affichage de la progression lors de l'exéxution des tests.

pytest-randomy
++++++++++++++

Permet de gérer l'aléatoire proprement et de rejouer les tests avec une seed.
particulière pour reproduire des erreurs liées à l'aléatoire.

.. code-block:: python

    import random

    def test_random():
        assert random.choice(range(10)) < 9

Ce test n'échouera qu'une fois sur 10. Le cas échéant, on pourra copier
la graine pour reproduire l'erreur localement.

pytest-xdist
++++++++++++

Pour paralléliser les tests sur plusieurs process ou machines. Attention,
quand on appelle des services externes types caches ou BDD, l'intégration est
un peu plus sport.

pytest-django
+++++++++++++

Utilitaires pour pytest et django: initialisation de la base de données,
settings, etc. Intégration avec xdist.

pytest-mock
+++++++++++

Mocks simples et efficaces:

.. code-block:: python

    
