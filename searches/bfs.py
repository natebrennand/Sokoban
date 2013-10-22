
from time import sleep
from copy import deepcopy

def breadth_first_search(board):
    visited_nodes = set()
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : visited_nodes,
    }
    current_queue = [(deepcopy(board), move) for move in board.moves_available()]

    return iterate_bfs(current_queue, records)


def iterate_bfs(current_queue, records):

    result = bfs(current_queue, records)
    if isinstance(result[0], bool) and result[0] == True:
        return result[1], result[2]     # records & board
    else:
        queue, records = result
        records['fringe'] = len(queue)

    return iterate_bfs(queue, records)


def bfs(queue, records):
    new_queue = []

    for b, m in queue:
        records['node'] += 1
        b.move(m)

        if b.finished():
            return True, records, b

        next_moves = b.moves_available()
        if next_moves:
            if hash(b) not in records['explored']:
                for move in next_moves:
                    new_queue.append((deepcopy(b), move))
                records['explored'].add(hash(b))
            else:
                records['repeat'] += 1

    return (new_queue, records)

