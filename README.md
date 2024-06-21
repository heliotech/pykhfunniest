## Python Joke

<img src="pykhfunniest/assets/laugh_emoji.png" alt="emoji laugh smile" width="150" />

Small application for learning the packaging of a Python project.

### Basic Structure

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

### Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

### Installation

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

### Usage

#### 1. REPL

    >>> from pykhfunniest import joke
    >>> joke()
        - Why did the scarecrow win an award?
        - Because he was outstanding in his field!

#### 2. Terminal

    $ python pykhfunniest
        - What do you get if you cross a snowman and a vampire?
        - Frostbite.

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

### Contact

    [email](mailto:pykhaz@o2.pl)

