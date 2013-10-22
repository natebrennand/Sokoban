
import board
from player import Player


def make_move(current_board, move):
    current_board.move(move)
    print current_board
    print current_board.moves_available()
    print current_board.finished()


with open('boards/easy_1.txt') as f:
    map_str = f.read()

new_board = board.load_map(map_str)

# test moves_available
assert new_board.moves_available() == ['u','r','d','l']


for move in ['u', 'l', 'l', 'l', 'l', 'l', 'd', 'r', 'r', 'r', 'r']:
    make_move(new_board, move)





