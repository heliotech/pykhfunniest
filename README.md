# Python Joke

<img src="pykhfunniest/assets/laugh_emoji.png" alt="emoji laugh smile" width="150" />

Small application for learning the packaging of a Python project.

[![CI](https://github.com/heliotech/pykhfunniest/actions/workflows/ci.yml/badge.svg)](https://github.com/heliotech/pykhfunniest/actions/workflows/ci.yml)
![Uses YAML](https://img.shields.io/badge/Uses-YAML-ff69b4)
![Built with Poetry](https://img.shields.io/badge/Built%20with-Poetry-60c7a8)
![Python version](https://img.shields.io/badge/Python-3.10-blue)

## Table of Contents

- [Basic Structure](#basic-structure)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Basic Structure

    └── pykhfunniest
        ├── pykhfunniest
        │   ├── assets
        │   │   └── laugh_emoji.png
        │   ├── __init__.py
        │   ├── __main__.py
        │   └── tell_joke.py
        └── tests
            ├── __init__.py
            └── test_get_joke_nr.py

## Installation

- Clone the repository:

    ```bash
    git clone https://github.com/heliokhaz/pykhfunniest.git
    ```

- Go to the project directory:

    ```bash
    cd pykhfunniest/dist
    ```

- Install with `pip`:

    ```bash
    pip install pykhfunniest-1.0.0-py3-none-any.whl
    ```

## Usage

### 1. REPL

    >>> from pykhfunniest import joke
    >>> joke()
        - What do you call fake spaghetti?
        - An impasta!
        (joke nr 3)
    >>> joke(1)
        - Why don’t scientists trust atoms?
        - Because they make up everything!
        (joke nr 1)

### 2. Terminal

    $ cd pykhfunniest
    $ python pykhfunniest
        - Why don’t scientists trust atoms?
        - Because they make up everything!
        (joke nr 1)
    $ python pykhfunniest 3
        - What do you call fake spaghetti?
        - An impasta!
        (joke nr 3)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Contact

    pykhaz@o2.pl

