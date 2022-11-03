from game import remove_invaders, play_sound

def test_remove_invaders():
    invader1 = {
        "x": 100,
        "y": 30
    }

    invader2 = {
        "x": 100,
        "y": 50
    }

    assert remove_invaders([invader1])[0]["y"] == 2000
    assert remove_invaders([invader2])[0]["y"] == 2000