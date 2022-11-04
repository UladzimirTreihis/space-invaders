from game import update_score_and_invaders


def genInvader(x, y, x_change, y_change):
    return {
        "x": x,
        "y": y,
        "x_change": x_change,
        "y_change": y_change
    }


def genBullet(x, y, y_change=3, state="rest"):
    return {
        "x": x,
        "y": y,
        "y_change": y_change,
        "state": state
    }


def test_update_score_and_invaders():
    score = 0
    invader = genInvader(0, 400, 1.3, 50)
    bullet = genBullet(0, 400)
    score2, bullet2, invader2 = update_score_and_invaders(
        score,
        bullet,
        invader
        )
    assert score2 == 1
    assert 64 <= invader2["x"] <= 736
    assert 30 <= invader2["y"] <= 200
    assert invader2["x_change"] == -1.3
    assert bullet2["y"] == 600
    assert bullet2["state"] == "rest"
