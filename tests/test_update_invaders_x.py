from game import update_invaders_x


def test_update_invaders():
    def genInvader(x, y, x_change, y_change):
        return {
            "x": x,
            "y": y,
            "x_change": x_change,
            "y_change": y_change
        }
    # Generate sample invaders
    invader1 = genInvader(50, 50, 3, 50)
    invader2 = genInvader(0, 50, -1, 50)
    invader3 = genInvader(0, 100, 8, 50)
    invader4 = genInvader(735, 10, 1, 5)

    # First time
    assert update_invaders_x([invader1, invader2])[0]["x"] == 50 + 3
    assert update_invaders_x([invader3, invader4])[0]["x"] == 0 + 8
    # Second time
    assert update_invaders_x([invader1, invader2])[1]["x"] == 0 - 1 - 1
    assert update_invaders_x([invader3, invader4])[1]["x"] == 735 + 1 + 1
