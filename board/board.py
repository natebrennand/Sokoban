
from position import Position

WALL    = set(['#'])
PLAYER  = set(['@', '+'])
GOAL    = set(['.', '+', '*'])
BOX     = set(['$','*'])

DIRECTION = {
    'u' : Position(0,-1),
    'd' : Position(0, 1),
    'r' : Position(1, 0),
    'l' : Position(-1,0)
}

def load_map(map_str):
    """
    @param map_str: A file containing an ascii sokoban puzzle.
    @return: a Board obj representing the map

    Constructs a sokoban board object and returns it.

    Map specifications
        1st line contains the # of lines.
            @ : player on ground
            + : player on goal
            # : wall
            $ : box off goal
            * : box on goal
    """
    new_board = Board()
    
    map_lines = map_str.split('\n')
    new_board.num_lines = int(map_lines[0].strip())

    for y, line in enumerate(map_lines[1:]):
        line = line.replace('\n', '')
        if line:
            for x, char in enumerate(line):
                pos = (x, y)

                if char in WALL:
                    new_board.add_wall(pos)
                if char in GOAL:
                    new_board.add_goal(pos)
                if char in BOX:
                    new_board.add_box(pos)
                if char in PLAYER:
                    new_board.add_player(pos)

    return new_board


class Board(object):
    """
    Keeps track of all elements of a board:
        walls, goals, boxes, the player and moves

    - moves_available: returns which moves are possible for the player
        in it's current position
    - move: moves the player in the specified direction and adjusts
        other elements accordingly
    - hash: only depends on the placement of boxes and the player.
    """

    def __init__(self):
        """ Contructor """
        self.num_lines = 0
        self.walls = set()      # all the walls
        self.goals = set()      # all the goals
        self.boxes = set()      # all the boxes w/ their states
        self.player = None      # the player with their state
        self.moves = []         # array of moves made


    def move(self, direction):
        """
        @param direction: a direction in the set [u,r,d,l]
            (assumes this is a valid movement)

        Adjusts the board object given a movement.
        """
        pos1 = self.player + DIRECTION[direction]
        pos2 = self.player + DIRECTION[direction].mult(2)

        if pos1 in self.boxes:          # move box if in path
            self.boxes.remove(pos1)
            self.boxes.add(pos2)

        self.player = pos1              # reset player position
        self.moves.append(direction)    # log the move

        return self


    def finished(self):
        """
        Return  True: if all boxes are on goals.
                False: Otherwise
        """
        if not self.goals.difference(self.boxes):     # if no overlap
            return True
        return False


    def moves_available(self):
        """
        @return array (move, cost)
            move: available moves in [u,r,d,l]
            cost:   2 if pushing a box,
                    1 otherwise

        Checks that moves that involve pushing a block are possible given the
        placement of walls.
        """
        theoretical_moves = ['u', 'r', 'd', 'l']
        possible_moves = []

        for direction in theoretical_moves:
            # position the player would be in
            new_pos     = self.player+DIRECTION[direction]
            # position the box the player pushes would be
            next_pos    = self.player+DIRECTION[direction].mult(2)

            if new_pos in self.walls:   # blocked by walls
                continue
            elif new_pos in self.boxes: # pushing a box
                if next_pos in self.walls.union(self.boxes):   # into a wall/box
                    continue
                possible_moves.append((direction, 2))
            else:                       # regular movement
                possible_moves.append((direction, 1))

        return possible_moves


    def add_player(self, (x, y)):
        """ sets the player """
        self.player = Position(x,y)


    def add_box(self, (x, y)):
        """ adds a box """
        self.boxes.add(Position(x,y))


    def add_goal(self, (x, y)):
        """ adds a goal """
        self.goals.add(Position(x,y))


    def add_wall(self, (x, y)):
        """ adds a wall to the board """
        self.walls.add(Position(x,y))


    def deadlock(self):
        """ TO BE IMPLEMENTED/USED """
        pass

    
    def __hash__(self):
        """ hashes the board object """
        return hash((
            hash(frozenset(self.boxes)),
            hash(self.player)
        ))


    def __str__(self):
        """
        Returns a string representation like the input files
        """
        str_board = []
        for y in range(self.num_lines):
            str_board.append([' ']*20)  # 20 is an abitrary width

        for wall in self.walls:                         # walls
            str_board[wall.y][wall.x] = '#'

        for box in self.boxes.difference(self.goals):   # boxes - goals
            str_board[box.y][box.x] = '$'

        for box in self.goals.union(self.boxes):        # boxes & goals
            str_board[box.y][box.x] = '*'

        for goal in self.goals.difference(self.boxes):  # goals - boxes
            str_board[goal.y][goal.x] = '.'

        if self.player in self.goals:                   # player on goal
            str_board[self.player.y][self.player.x] = '@'
        else:                                           # player off goal
            str_board[self.player.y][self.player.x] = '+'

        return '\n'.join([''.join(line) for line in str_board])

