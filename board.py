
WALL = '#'
PLAYER = {
    '@' : 'NORMAL',
    '+' : 'ON_GOAL'
}
GOAL = {
    '.' : 'EMPTY',
    '#' : 'FULL'
}
BOX = '$'

DIRECTION = {
    'u' : (0,1),
    'd' : (0,-1),
    'r' : (1,0),
    'l' : (-1,0)
}

from box import Box
from wall import Wall
from player import Player
from goal import Goal

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
                elif char == BOX:
                    box = Box
                elif char in GOAL:
                    goal = Goal(x_index, y_index, GOAL[char])
                    new_board.add_goal(goal)
                elif char in PLAYER:
                    player = Player(x_index, y_index, PLAYER[char])
                    new_board.set_player(player)

    return new_board


class Board(object):

    def __init__(self):
        self.walls = []
        self.goals = []
        self.boxes = []
        self.player = None



    def finished(self):
        for goal in self.goals:
            if goal.state == 'EMPTY':
                return False
        return True


    def moves_available(self):
        x, y = self.player.x, self.player.y
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


    def set_player(self, player):
        self.player = player

    def add_box(self, box):
        self.boxes.append(box)

    def add_goal(self, goal):
       self.goals.append(goal)

    def add_wall(self, wall):
        self.walls.append(wall)

    def deadlock(self):
        # return True / False
        pass

