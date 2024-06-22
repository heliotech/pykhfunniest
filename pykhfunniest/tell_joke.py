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


def get_joke_nr(nr):
    joke_max = len(jokes)
    if nr not in range(1, joke_max + 1):
        return random.randint(1, joke_max)
    return nr


def joke(nr_=None, dbg=False):
    """ Telling a random joke """

    nr = get_joke_nr(nr_)
    chosen_as_list = jokes[nr - 1]
    if nr_ is not None and nr_ != nr:
        msg = (f", there is no joke of this number, {nr_}, yet. "
               "Chosen random number.")
    else:
        msg = ""
    for i, sentence in enumerate(chosen_as_list):
        sentence_len = len(chosen_as_list)
        # assuming the punchline is the last one:
        style = "bold italic" if i == (sentence_len - 1) else ""
        cprint(f"\t- {sentence[0]}", style=style)
    if not dbg:
        print(f"\t(joke nr {nr}{msg})")
        return
    return chosen_as_list[1]


def main():
    """ Entry point """

    joke()


if __name__ == "__main__":
    main()
