
SYMBOL = {
    'OFF' : '$',
    'ON'  : '*'
}

class Box(object):

    def __init__(self, (pos_x, pos_y), current_state):
        self.x = pos_x
        self.y = pos_y
        # OFF / ON
        self.state = current_state


    def __str__(self):
        return "{} BOX @ ({},{})".format(self.state, self.x, self.y)


    def symbol(self):
        return SYMBOL[self.state]

