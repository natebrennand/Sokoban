
import board
from player import Player

with open('boards/easy_1.txt') as f:
    map_str = f.read()

new_board = board.load_map(map_str)

# test moves_available
assert new_board.moves_available() == ['u','r','d','l']

new_board.player = Player(1,1,'NORMAL') # reset player location
# test moves_available when in corner
assert new_board.moves_available() == ['r','d']


