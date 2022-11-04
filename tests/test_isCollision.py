from game import isCollision


def test_isCollision():
    assert isCollision(0, 1, 0, 1)
    assert not isCollision(10, 100, 10, 100)
    assert isCollision(0, -1, 0, -1)
    assert isCollision(-1, 0, -1, 0)
    assert isCollision(0, 29, 0, 39)
    assert not isCollision(0, 31, 0, 41)
