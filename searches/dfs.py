
from copy import deepcopy

def depth_first_search(board, print_steps=None):
    """
    @param board: a Board obj
    @param print_steps: flag to print intermediate steps

    @return (records, board)
        records: a dictionary keeping track of necessary statistics
        board: a copy of the board at the finished state.
            Contains an array of all moves performed.

    Performs a depth first search on the sokoban board. Follows the
    """
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set()
    }

    if print_steps:
        print 'repeat\tseen'

    if board.finished():    # check if initial state is complete
        return records, board

    board_queue = [board]   # initialize queue

    while True:
        if print_steps:
            print "{}\t{}".format(records['repeat'], len(records['explored']))

        if not board_queue: # if empty queue, fail
            print records
            raise Exception('Solution not found.')

        node_board = board_queue.pop(0)
        records['explored'].add(hash(node_board))
        records['fringe'] = len(board_queue)

        if node_board.finished():   # if finished, return
            return records, node_board

        choices = node_board.moves_available()
        if not choices:     # if no options
            board_queue.pop(0)    
        else:               # regular
            for direction, cost in choices:
                records['node'] += 1
                child_board = deepcopy(node_board).move(direction)

                if hash(child_board) not in records['explored'] and child_board not in board_queue:
                    board_queue.insert(0, child_board)
                else:
                    records['repeat'] += 1
