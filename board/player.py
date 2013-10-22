
SYMBOL = {
    'NORMAL': '@',
    'ON_GOAL': '+'
}


class Player(object):

    def __init__(self, (pos_x, pos_y), current_state):
        self.x = pos_x
        self.y = pos_y
        # NORMAL / ON_GOAL
        self.state = current_state


    def __str__(self):
        return "{} PLAYER @ ({},{})".format(self.x, self.y)


    def symbol(self):
        return SYMBOL[self.state]


