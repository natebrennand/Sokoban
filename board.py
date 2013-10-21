
EMPTY_GOAL = '.'
FULL_GOAL = '#'
PLAYER_ON_GOAL = '+'
PLAYER = '@'
BOX = '$'
WALL = '#'


def load_map(map_str):
    new_board = Board()
    
    map_lines = map_str.split('\n')
    num_lines = map_lines[0]

    for y_index, line in enumerate(map_lines[1:]):
        line = line.replace('\n', '')
        if line:
            for x_index, char in enumerate(line):
                if char == WALL:
                    block = Wall(x_index, y_index)
                    new_board.add_wall(block)

    return new_board


class Board(object):

    def __init__(self):
        self.walls = []

    
    def add_wall(self, wall):
        self.walls.append(wall)


    def moves_available(self, x, y):
        moves = [('u', (x, y-1)), ('r', (x+1, y)),
                 ('d', (x, y+1)), ('l', (x-1, y))]

        for block in self.walls:
            options = [(i, m, p) for i, (m, p) in enumerate(moves)]
            for index, move, pos in reversed(options):
                if pos == (block.x, block.y):
                    del moves[index]

            if not moves:   # no moves available
                return []

        return [move for move, pos in moves]


    def deadlock(self):
        # return True / False
        pass


class Wall(object):

    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y


    def __str__(self):
        return "({},{})".format(self.x, self.y)


