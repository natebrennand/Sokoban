
from copy import deepcopy

def uniform_cost_search(board, steps):
    """
    @param board: a Board obj
    @return: return iterate_bfs fn call
    """
    
    global print_steps
    print_steps = True if steps else False

    cq = [(deepcopy(board), move, cost) for move, cost in board.moves_available()]
    cq.sort(key=lambda tup: tup[2])  # sort by cost
    cqh = {}
    for b,m,c in cq:
        cqh[hash((hash(b),m))] = c

    records = {
        'node' : len(cq),
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set()
    }

    return iterate_ucs(cq, cqh, records)


def iterate_ucs(queue, qh, records):
    """
    @param queue: A queue of boards & their next slated move
    @param records: a dictionary with various logs that need to be kept
    """

    global print_steps
    if print_steps:
        print 'repeat\tseen'

    while True:
        if print_steps:
            print "{}\t{}".format(records['repeat'], len(records['explored']))

        result = ufs(queue, qh, records)
        if isinstance(result[0], bool) and result[0] == True:
            return result[1], result[2]     # records & board
        else:
            queue, records = result
            records['fringe'] = len(queue)


def ufs(queue, queue_hash, records):
    """
    @param queue: The queue of boards & moves to be evalutated
    @param records: records to be updated

    @return: new_queue, records: updated versions of each
    """
    new_queue = []
    board, m, cost = queue.pop(0)
    del queue_hash[hash((hash(board),m))]
    board.move(m)
    records['explored'].add(hash(board))
    if board.finished():
        return True, records, board

    new_moves = board.moves_available()
    new_queue = [(deepcopy(board), m, c+cost) for (m, c) in new_moves]
    to_be_added = []
    to_be_replaced = []

    for b,m,c in new_queue:
        records['node'] += 1
        move_hash = hash((hash(b),m))
        if move_hash in queue_hash:
            records['repeat'] += 1
            if queue_hash[move_hash] > c and move_hash not in records['explored']:
                queue_hash[move_hash] = c
                to_be_replaced.append((b,m,c))
        else:
            queue_hash[move_hash] = c
            to_be_added.append((b,m,c))

    for index, (b,m,c) in enumerate(queue):
        for rb,rm,rc in to_be_replaced:
            if hash((hash(b),m)) == hash((hash(rb),rm)):
                queue[index] = (rb,rm,rc)
    queue = queue + to_be_added
    queue.sort(key=lambda tup: tup[2])

    return queue, records
