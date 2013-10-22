
from copy import deepcopy

def breath_first_search(board):
    visited_nodes = set()
    records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : visited_nodes,
    }
    current_queue = [(deepcopy(board), move) for move in board.moves_available()]

    return iterate_dfs(board, current_queue, records)


def iterate_bfs(current_queue, records):

    next_queue = dfs(current_queue)
    queue = []


    records['fringe'] = len(next_queue)
    for board, move in next_queue:
        board_hash = hash(board)
        records['node'] += 1
        if board_hash in records[explored]:        
            records['repeat'] += 1
        else:
            records['explored'].add(board_hash)

        if board.finished():
            return records

        queue += [(deepcopy(board), next_move) for next_move in board.moves_available()]


    return iterate_dfs(queue, records)


def bfs(queue):
    new_queue = []

    for b, m in queue:
        b.move(m)
        next_moves = b.moves_available()
        if next_moves:
            for move in next_moves:
                new_queue += (b, move)

    return new_queue

