from game import move_next_line

def test_move_next_line():
    def genInvader(x, y, x_change, y_change):
        return {
            "x": x,
            "y": y,
            "x_change": x_change,
            "y_change": y_change
        }

    invader1 = genInvader(50, 50, 1.2, 50)
    invader2 = genInvader(0, 50, -1.2, 50)
    invader3 = genInvader(0, 100, 1.2, 50)
    invader4 = genInvader(735, 10, 1.2, 5)
    invader5 = genInvader(735, 15, -1.2, 5)
    invader6 = genInvader(1, 10, 1.2, 5)
    invader7 = genInvader(734, 10, 1.2, 5)
    assert move_next_line(invader1) == invader1
    assert move_next_line(invader2) == invader3
    assert move_next_line(invader4) == invader5
    assert move_next_line(invader6) == invader6
    assert move_next_line(invader7) == invader7
    print("All Tests Passed Successfully")