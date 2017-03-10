
class Rover(object):

    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.dire = d

    def turn(self,d):
        if d=='R':
            if self.dire == 'N':
                self.dire = 'E'
            elif self.dire == 'E':
                self.dire = 'S'
            elif self.dire == 'S':
                self.dire = 'W'
            elif self.dire == 'W':
                self.dire = 'N'

        if d=='L':
            if self.dire == 'N':
                self.dire = 'W'
            elif self.dire == 'W':
                self.dire = 'S'
            elif self.dire == 'S':
                self.dire = 'E'
            elif self.dire == 'E':
                self.dire = 'N'
    def move(self):
        if self.dire == 'N':
            self.y += 1
        elif self.dire == 'E':
            self.x += 1
        elif self.dire == 'S':
            self.y -= 1
        elif self.dire == 'W':
            self.x -= 1

    def position(self):
        return str(self.x) + " " + str(self.y) + " " + self.dire
