# test_get_joke_nr.py

from pykhfunniest.tell_joke import get_joke_nr, joke, jokes
from random import randint

joke_max = len(jokes)

# def test_always_true():

#     assert 1 == 1


def test_get_joke_nr():
    for _ in range(10000):
        nr_ = randint(-100, 100)
        nr = get_joke_nr(nr_)
        print(f"DBG: {_}. {nr_ = }, {nr = }")

        assert nr in range(1, joke_max + 1)


def test_joke():
    punchlines = [j[1] for j in jokes]
    for _ in range(1000):
        result = joke(dbg=True)
        print(f"DBG: {result = }, {punchlines = }")
        assert result in punchlines
