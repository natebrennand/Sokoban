
class Goal(object):

    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y


    def __str__(self):
        return "EMPTY GOAL @ ({},{})".format(self.x, self.y)


