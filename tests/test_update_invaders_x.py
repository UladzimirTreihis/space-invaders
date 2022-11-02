# import pytest
from game import remove_invaders


def test_remove_invaders():
    invader1 = {
        "x": 100,
        "y": 30
    }

    invader2 = {
        "x": 200,
        "y": 50
    }

    assert remove_invaders(invader1)["y"] == 2000
    assert remove_invaders(invader2)["y"] == 2000
