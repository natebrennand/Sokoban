
class Goal(object):

    def __init__(self, pos_x, pos_y, current_state):
        self.x = pos_x
        self.y = pos_y
        self.state = current_state


    def __str__(self):
        return "{} GOAL @ ({},{})".format(self.x, self.y)



