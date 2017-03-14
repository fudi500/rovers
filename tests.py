import unittest
from rovers import Rover, Plateau

class TestRoverS(unittest.TestCase):

    def setUp(self):
        self.rover = Rover(1,5,'S')
        self.plateau = Plateau(5,5)

    def testRoverHasCoordinatesX(self):
        assert self.rover.x_coordinates !=None, "coordinates x is None"

    def testRoverHasCoordinatesY(self):
        assert self.rover.y_coordinates !=None, "coordinates y is None"

    def testRoverHasDirection(self):
        assert self.rover.direction !=None, "direction x is None"


    def testRoverSetCoordinatesX(self):
        self.rover.setCoordinatesX(4)
        assert self.rover.x_coordinates == 4, "rover coordinates x did not set correctly"

    def testRoverSetCoordinatesY(self):
        self.rover.setCoordinatesY(3)
        assert self.rover.y_coordinates == 3, "rover coordinates y did not set correctly"

    def testRoverSetdirection(self):
        self.rover.setDirection('S')
        assert self.rover.direction == 'S', "rover Direction did not set correctly"


if __name__=="__main__":
    unittest.main()
