Apfyro #1
=========


Pytest : Introduction, trucs et astuces
=======================================

Date: 09-02-2018

Présentation disponible ici : https://slides.com/eliotberriot/afpyro-02-2018

Tous les tests utilisés pendant la présentation
sont disponibles dans le dossier tests/pytest. Le code se trouve dans
le dossier afpyro.


Installation
------------

.. code-block:: shell

    git clone git@github.com:EliotBerriot/afpyro-marseille-01-2018.git

    # création du virtualenv
    virtualenv -p `which python3` venv
    source venv/bin/activate

    # installation des dépendances
    pip install -r requirements.txt

Lancement des tests
-------------------

Pour lancer l'intégralité de la suite de tests:

.. code-block:: shell

    pytest

Il y a des failures, c'est tout à fait normal, elles sont là à but pédagogique ;)
