import pytest
from game import show_bullet


def test_show_bullet():

    bullet1 = {
        "x": 45,
        "y": 0,
        "state": "rest"
    }
    bullet2 = {
        "x": 0,
        "y": 0,
        "state": "rest"
    }
    bullet3 = {
        "x": 70,
        "y": 20,
        "state": "fire"
    }
    bullet4 = {
        "x": 90,
        "y": 10,
        "state": "fire"
    }

    assert show_bullet(bullet1)["state"] == "fire"
    assert show_bullet(bullet2)["state"] == "fire"
    assert show_bullet(bullet3)["state"] == "fire"
    assert show_bullet(bullet4)["state"] == "fire"
