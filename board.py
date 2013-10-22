
WALL = '#'
PLAYER = {
    '@' : 'NORMAL',
    '+' : 'ON_GOAL'
}
GOAL = '.'
BOX = {
    '$' : 'OFF',
    '*' : 'ON'
}
DIRECTION = {
    'u' : (0,-1),
    'd' : (0,1),
    'r' : (1,0),
    'l' : (-1,0)
}

from box    import Box
from wall   import Wall
from player import Player
from goal   import Goal


def load_map(map_str):
    new_board = Board()
    
    map_lines = map_str.split('\n')
    new_board.num_lines = int(map_lines[0].strip())

    for y_index, line in enumerate(map_lines[1:]):
        line = line.replace('\n', '')
        if line:
            for x_index, char in enumerate(line):
                if char == WALL:
                    block = Wall((x_index, y_index))
                    new_board.add_wall(block)
                elif char == GOAL:
                    goal = Goal((x_index, y_index))
                    new_board.add_goal(goal)
                elif char in BOX:
                    box = Box((x_index, y_index), BOX[char])
                    new_board.add_box(box)
                elif char in PLAYER:
                    player = Player((x_index, y_index), PLAYER[char])
                    new_board.set_player(player)

    return new_board


class Board(object):

    def __init__(self):
        self.num_lines = 0
        self.walls = {}
        self.goals = {}
        self.boxes = {}
        self.player = None

    def move(self, direction):
        x_diff, y_diff = DIRECTION[direction]
        pos1 = self.player.x + x_diff, self.player.y + y_diff
        pos2 = self.player.x + 2*x_diff, self.player.y + 2*y_diff

        # move box if in path
        if pos1 in self.boxes:
            self.boxes[pos2] = Box(pos2, None)
            if pos2 in self.goals:
                del self.goals[pos2]
                self.boxes[pos2].state = 'ON'
            else:
                self.boxes[pos2].state = 'OFF'
            del self.boxes[pos1]


        # if player was on goal, re-add to dict
        if self.player.state == 'ON_GOAL':
            x, y = self.player.x, self.player.y
            self.goals[(x, y)] = Goal((x, y))

        # if player is now on a goal
        if pos1 in self.goals:
            self.player = Player(pos1, 'ON_GOAL')
            del self.goals[pos1]
        else:
            self.player = Player(pos1, 'NORMAL')


        return self


    def finished(self):
        for box in self.boxes.values():
            if box.state == 'OFF':
                return False
        return True


    def moves_available(self):
        x, y = self.player.x, self.player.y
        moves = [('u', (0, -1)), ('r', (1, 0)),
                 ('d', (0, 1)), ('l', (-1, 0))]

        move_options = [(i, m, p) for i, (m, p) in enumerate(moves)]
        for index, move, (pos_x, pos_y) in reversed(move_options):
            # if a wall blocks the path
            if (x+pos_x, y+pos_y) in self.walls:
                del moves[index]
            # if the box's movement is blocked by a wall/box
            elif (x+pos_x, y+pos_y) in self.boxes:
                next_pos = (x+2*pos_x, y+2*pos_y)
                if next_pos in self.walls or next_pos in self.boxes:
                    del moves[index]

            if not moves:   # no moves available, stop iterating
                return []

        return [move for move, pos in moves]


    def set_player(self, player):
        self.player = player

    def add_box(self, box):
        self.boxes[(box.x, box.y)] = box

    def add_goal(self, goal):
       self.goals[(goal.x, goal.y)] = goal

    def add_wall(self, wall):
        self.walls[(wall.x, wall.y)] = wall

    def deadlock(self):
        # return True / False
        pass

    def __str__(self):
        str_board = []
        for y in range(self.num_lines):
            str_board.append([' ']*20)

        for piece_set in [self.walls, self.goals, self.boxes]:
            for (pos_x, pos_y) in piece_set.keys():
                str_board[pos_y][pos_x] = piece_set[(pos_x, pos_y)].symbol()

        str_board[self.player.y][self.player.x] = self.player.symbol()

        str_board = [''.join(line) for line in str_board]
        return '\n'.join(str_board)



