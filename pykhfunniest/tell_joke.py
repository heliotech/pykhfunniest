# tell_joke.py

from rich.console import Console
import random

cprint = Console().print

jokes = [
            [["Why don’t scientists trust atoms?"],
             ["Because they make up everything!"]],

            [["Why did the scarecrow win an award?"],
             ["Because he was outstanding in his field!"]],

            [["What do you call fake spaghetti?"],
             ["An impasta!"]],

            [["Why don’t skeletons fight each other?"],
             ["They don’t have the guts."]],

            [["What do you get if you cross a snowman and a vampire?"],
             ["Frostbite."]],

            [["Why did the bicycle fall over?"],
             ["Because it was two-tired!"]]
]


def joke(nr=None):
    """ Telling a random joke """

    nr = nr if nr else random.randint(0, len(jokes) - 1)
    chosen_as_list = jokes[nr]
    for i, sentence in enumerate(chosen_as_list):
        sentence_len = len(chosen_as_list)
        # assuming the punchline is the last one:
        style = "bold italic" if i == (sentence_len - 1) else ""
        cprint(f"\t- {sentence[0]}", style=style)


def main():
    """ Entry point """

    joke()


if __name__ == "__main__":
    main()
