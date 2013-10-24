
from copy import deepcopy, copy
from board import load_map, Position
from sys import exit

def make_move(current_board, move):
    current_board.move(move)
    #print current_board
    print current_board.moves_available()
    print 'DONE:', current_board.finished()


with open('sokoban_boards/easy_1.txt') as f:
    map_str = f.read()

new_board = load_map(map_str)

print new_board

print new_board.moves_available()
new_board.add_player((1,1))
print new_board.moves_available()

print Position(0,0) in new_board.walls

exit(0)



# test moves_available
assert new_board.moves_available() == ['u','r','d','l']

board_copy = deepcopy(new_board)
hash1 = hash(board_copy)
board_copy.move('d')
x = copy(board_copy)
assert hash(x)==hash(board_copy)
board_copy.move('u')
assert hash(x)!=hash(board_copy)
hash2 = hash(board_copy)
assert hash1==hash2

move_set = ['u', 'l', 'l', 'l', 'l', 'l', 'd', 'r', 'r', 'r', 'r']

print new_board
for move in move_set:
    make_move(new_board, move)

print new_board.moves 
print move_set
assert new_board.moves == move_set

