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

    git clone git@github.com:EliotBerriot/afpyro-marseille-01-2018.git
    # création du virtualenv
    virtualenv -p `which python3` venv

    source venv/bin/activate
    pip install -r requirements.txt


Premier test (1)
----------------

Lancement::

    pytest

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

Fixtures (4)
------------

Rien à voir avec les fixtures de l'écosystème django.

Permet de passer de l'état, des utilitaires ou de faire de l'initialisation ou
du nettoyage avant un test.

Exemple avec unittest:

Le même code avec une fixture:

Avantages:

- Fini les 16 niveaux d'héritages sur les classes de tests pour avoir les bonnes
  méthodes et le bon état
- Encapsulation du setup et du teardown dans la même fonction, donc plus de lisibilité
- On sait exactement quel test a besoin de quoi directement dans la signature
  de la fonction

Les fixtures peuvent dépendre les unes des autres

On peut donc écrire des fixtures très bas niveau, et les combiner pour faire
des fixtures plus puissantes, sans perdre en souplesse.


Parametrize (5)
---------------

TL;DR: Générer des tests dynamiquements.

Pourquoi ? Éviter de se répêter. Si je reprend mon exemple du début, on voit que
j'ai 4 tests qui font quasiment exactement la même chose.

On pourrait factoriser avec une boucle for:

Inconvenients de cette méthode:

- Une boucle à écrire à la main
- Si une des assertions fail, le test plante et les suivantes ne sont pas jouées
- idéalement, un test ne doit tester qu'une seule chose

Parametrize implémente ce pattern de façon transparente, mais en générant
un test pour chaque élément de la boucle:
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
