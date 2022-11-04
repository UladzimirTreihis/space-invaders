from game import bullet_movement


def test_bullet_movement():
    # Generate sample objects
    bullet1 = {
        "x": 45,
        "y": 0,
        "state": "rest"
    }
    bullet2 = {
        "y": 500,
        "y_change": 3,
        "state": "rest"
    }
    bullet3 = {
        "y": -10,
        "state": "fire"
    }
    bullet4 = {
        "x": 45,
        "y": 500,
        "state": "fire",
        "y_change": 3
    }
    assert bullet_movement(bullet1)["y"] == 600
    assert bullet_movement(bullet1)["x"] == 45
    assert bullet_movement(bullet1)["state"] == "rest"
    assert bullet_movement(bullet2)["y"] == 500
    assert bullet_movement(bullet2)["y_change"] == 3
    assert bullet_movement(bullet2)["state"] == "rest"
    assert bullet_movement(bullet3)["y"] == 600
    assert bullet_movement(bullet3)["state"] == "rest"
    assert bullet_movement(bullet4)["y"] == 497
