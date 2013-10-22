
from copy import deepcopy

def breadth_first_search(board):
    """
    @param board: a Board obj
    @return: return iterate_bfs fn call
    """
    visited_nodes = set()
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : visited_nodes,
    }
    current_queue = [(deepcopy(board), move) for move in board.moves_available()]

    print 'repeat\tseen'
    return iterate_bfs(current_queue, records)


def iterate_bfs(queue, records):
    """
    @param queue: A queue of boards & their next slated move
    @param records: a dictionary with various logs that need to be kept
    """

    while True:
        print "{}\t{}".format(records['repeat'], len(records['explored']))

        result = bfs(queue, records)
        if isinstance(result[0], bool) and result[0] == True:
            return result[1], result[2]     # records & board
        else:
            queue, records = result
            records['fringe'] = len(queue)

        if len(queue) == 0:
            break

    print 'failure'


def bfs(queue, records):
    """
    @param queue: The queue of boards & moves to be evalutated
    @param records: records to be updated

    @return: new_queue, records: updated versions of each
    """
    new_queue = []
    in_queue = set([])

    # iterates over boards w/ their moves
    for b, m in queue:
        records['node'] += 1
        b.move(m)   # performs move
        if b.finished():    # checks if done
            return True, records, b

        next_moves = b.moves_available()

        if next_moves:
            if hash(b) not in records['explored']:
                for move in next_moves:
                    move_hash = hash((hash(b),move))
                    if move_hash not in in_queue:
                        new_queue.append((deepcopy(b), move))
                        in_queue.add(move_hash)
                records['explored'].add(hash(b))
            else:
                records['repeat'] += 1

    return (new_queue, records)

