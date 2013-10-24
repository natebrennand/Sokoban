
WALL    = set(['#'])
PLAYER  = set(['@', '+'])
GOAL    = set(['.', '+', '*'])
BOX     = set(['$','*'])

from board import Board

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

