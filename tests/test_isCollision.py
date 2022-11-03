from game import isCollision

def test_isCollision():
   assert isCollision(0, 1, 0, 1) == True
   assert isCollision(10, 100, 10, 100) == False
   assert isCollision(0, -1, 0, -1) == True
   assert isCollision(-1, 0, -1, 0) == True     
   assert isCollision(0, 29, 0, 39) == True
   assert isCollision(0, 31, 0, 41) == False