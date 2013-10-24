
class Position:
    """
    Keeps track of board positions.
    Advantages over simple tuples come when using operations such as +, in, hash
    """

    def __init__(self, cord_x, cord_y):
        self.x = cord_x
        self.y = cord_y


    def __add__(self, pos_2):
        return Position(self.x + pos_2.x, self.y + pos_2.y)


    def __str__(self):
        return "({},{})".format(self.x, self.y)


    def __eq__(self, pos_2):
        return self.x == pos_2.x and self.y == pos_2.y


    def __ne__(self, pos_2):
        return self.x != pos_2.x or self.y != pos_2.y


    def __hash__(self):
        return hash((self.x, self.y))


    def mult(self,cons):
        """
        @param cons: integer to multiply a position
        @return: returns a multiplied position
        
        cons: must be an integer
        self: must be (+/-1,0) or (0,+/-1)
        """
        if not isinstance(cons, int):
            raise Exception('Passed in constant not an integer')
        if not (not self.x) ^ (not self.y):
            raise Exception('Neither position coordinates == 0')
        return Position(self.x*cons, self.y*cons)


    def dist(self, pos_2):
        """
        @param pos_2: another Position
        @return: Manhattan distance between the two Positions
        """
        return abs(self.x - pos_2.x)+ abs(self.y - pos_2.y)
