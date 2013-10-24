
class Position:

    def __init__(self, cord_x, cord_y):
        self.x = cord_x
        self.y = cord_y


    def __add__(self, pos_2):
        return Position(self.x + pos_2.x, self.y + pos_2.y)


    def mult(self,cons):
        return Position(self.x*cons, self.y*cons)


    def __str__(self):
        return "({},{})".format(self.x, self.y)


    def dist(self, pos_2):
        return abs(self.x - pos_2.x)+ abs(self.y - pos_2.y)


    def __eq__(self, pos_2):
        return self.x == pos_2.x and self.y == pos_2.y


    def __ne__(self, pos_2):
        return self.x != pos_2.x or self.y != pos_2.y


    def __hash__(self):
        return hash((self.x, self.y))
