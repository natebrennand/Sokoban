
from copy import deepcopy

def breadth_first_search(board, print_steps=False):
    """
    @param board: a Board obj
    @param print_steps: flag to print intermediate steps

    @return (records, board)
        records: a dictionary keeping track of necessary statistics
        board: a copy of the board at the finished state.
            Contains an array of all moves performed.
    """
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set([])
    }
    if print_steps:
        print 'repeat\tseen'

    if board.finished():    # check if initial state is complete
        return records, board

    board_queue = [board]   # initialize queue

    while True:
        if print_steps:
            print "{}\t{}".format(records['repeat'], len(records['explored']))

        if not board_queue: # fail if no options left
            print records
            raise Exception('Solution not found.')

        node_board = board_queue.pop(0)             # move to next node in array
        records['explored'].add(hash(node_board))   # add hash to explored
        records['fringe'] = len(board_queue)        # 

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
