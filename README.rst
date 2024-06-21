.. -*- coding: utf-8 -*-

-------------
 python joke
-------------

.. raw:: html

  <img src="pykhfunniest/assets/laugh_emoji.png" alt="emoji laugh smile" width="150" />

Small application for learning the packaging of a python project.

Basic structure:

.. code-block:: text

    |-- pykhfunniest
        |-- dist
        |   |-- pykhfunniest-1.0.0-py3-none-any.whl
        |   |-- pykhfunniest-1.0.0.tar.gz
        |
        |-- LICENSE
        |-- poetry.lock
        |-- pykhfunniest
        |   |-- assets
        |   |   |-- laugh_emoji.png
        |   |-- __init__.py
        |   |-- __main__.py
        |   |-- tell_joke.py
        |
        |-- pyproject.toml
        |-- README.rst
        |-- tests
            |-- __init__.py

Table of Contents
-------------------

- `Installation`_
- `Usage`_
- `License`_
- `Contact`_

Installation
-------------


- Clone the repository

    `git clone https://github.com/heliokhaz/pykhfunniest.git`

- Go to the project directory

    `cd pykhfunniest/dist`

- Install with `pip`:

    `pip install pykhfunniest-1.0.0-py3-none-any.whl`

Usage
------

1. REPL

::

   >>> from pykhfunniest import joke
   >>> joke()
       - Why did the scarecrow win an award?
       - Because he was outstanding in his field!

2. Terminal

::

    $ python pykhfunniest
        - What do you get if you cross a snowman and a vampire?
        - Frostbite.

License
--------

This project is licensed under the MIT License - see the `LICENSE <./LICENSE>`_ file for details.

Contact
--------

    pykhaz@o2.pl
