
from copy import deepcopy

def breadth_first_search(board, print_steps=False):
    """
    @param board: a Board obj
    @param print_steps: flag to print intermediate steps

    @return 
    """
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set([])
    }
    if print_steps:
        print 'repeat\tseen'

    if board.finished():
        return records, board

    board_queue = [board]

    while True:
        if print_steps:
            print "{}\t{}".format(records['repeat'], len(records['explored']))

        if not board_queue:
            raise Exception('Solution not found.')

        node_board = board_queue.pop(0)
        records['explored'].add(hash(node_board))
        records['fringe'] = len(board_queue)

        for direction, cost in node_board.moves_available():
            # copy the board and perform the move
            child_board = deepcopy(node_board).move(direction)
            records['node'] += 1

            if hash(child_board) not in records['explored'] and child_board not in board_queue:
                if child_board.finished():  # if the board is solved
                    return records, child_board
                board_queue.append(child_board) # else, add to the queue
            else:   # child board is a repeat
                records['repeat'] += 1
