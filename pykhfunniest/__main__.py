# __main__.py

from tell_joke import joke, jokes
# from tell_joke import cprint  # for debugging

import argparse

parser = argparse.ArgumentParser(
                                 prog="python pykhfunniest",
                                 description="Prints a random joke",
                                 epilog="(A toy project)")
parser.add_argument("number", nargs="?", type=int,
                    choices=range(1, len(jokes) + 1),
                    metavar=f"number: from 1 to {len(jokes)}",
                    help="Number of the joke to print.")
args = parser.parse_args()
nr = args.number - 0 if args.number is not None else args.number

joke(nr)
