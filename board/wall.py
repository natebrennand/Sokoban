
class Wall(object):

    def __init__(self, (pos_x, pos_y)):
        self.x = pos_x
        self.y = pos_y


    def symbol(self):
        return '#'


    def __str__(self):
        return "({},{})".format(self.x, self.y)


    def __hash__(self):
        return hash((self.x, self.y))

