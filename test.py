
from board import load_map

def make_move(current_board, move):
    current_board.move(move)
    #print current_board
    print current_board.moves_available()
    print 'DONE:', current_board.finished()


with open('sokoban_boards/easy_1.txt') as f:
    map_str = f.read()

new_board = load_map(map_str)

# test moves_available
assert new_board.moves_available() == ['u','r','d','l']


hash1 = hash(new_board)
new_board.move('d')
new_board.move('u')
hash2 = hash(new_board)
assert hash1==hash2

print new_board
for move in ['u', 'l', 'l', 'l', 'l', 'l', 'd', 'r', 'r', 'r', 'r']:
    make_move(new_board, move)


