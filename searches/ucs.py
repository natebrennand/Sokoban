
from copy import deepcopy
from priority_cost_queue import Priority_Cost_Queue

def uniform_cost_search(board, print_steps=False):
    """
    @param board: a Board object
    @param print_steps: flag to print intermediate steps

    @return (records, board)
        records: a dictionary keeping track of necessary statistics
        board: a copy of the board at the finished state.
            Contains an array of all moves performed.

    Performs a uniform cost search on the sokoban board. Follows the
        implementation on pg 84 of AIMA closely.
    """
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set()
    }

    if board.finished():    # check if initial state is complete
        return records, board

    board_queue = Priority_Cost_Queue()  # initialize queue
    board_queue.push(0, board)
    records['node'] += 1

    while True:

        records['fringe'] = len(board_queue)
        if not board_queue:     # fail if no options left
            print records
            raise Exception('Solution not found.')

        node_cost, node_board = board_queue.pop()

        if node_board.finished():   # return if solved
            return records, node_board
        records['explored'].add(hash(node_board))   # log board

        for direction, cost in node_board.moves_available():

            child_board = deepcopy(node_board).move(direction) # copy & move
            records['node'] += 1

            if hash(child_board) not in records['explored']:    # if not explored
                if not child_board in board_queue:              # if not in queue
                    board_queue.push(node_cost+cost, child_board)
                else:                                           # check if cost can be made lower
                    board_queue.update_cost(node_cost+cost, child_board)
                    records['repeat'] += 1
            else:                                               # log repeat if already explored
                records['repeat'] += 1
