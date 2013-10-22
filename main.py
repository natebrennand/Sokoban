
from board import load_map
from timer import timeit
from copy import deepcopy
import argparse
from sys import exit

from searches import breadth_first_search as bfs
from searches import depth_first_search as dfs

searches = [dfs]


def report(r, b):
    print "{} nodes visited".format(r['node'])
    print "{} nodes repeated".format(r['repeat'])
    print '{} nodes at the fringe of the search'.format(r['fringe'])
    print '{} nodes explored'.format(len(r['explored']))
    print 'Here are the moves made for the solution:'
    print '\t{}'.format(b.moves)


@timeit
def run_search(board, search):
    results, board = search(board)
    report(results, board)


def get_map_str(path):
    map_str = ''
    with open(path, 'r') as f:
        map_str = f.read()
    return map_str


def get_args():
    parser = argparse.ArgumentParser(
        description='Get input for the sokoban program.')
    parser.add_argument('puzzle', metavar='P', nargs='?',
                        help='Puzzle to be solved by sokoban')
    parser.add_argument('--test', dest='test', action='store_const',
                        const=True, default=False,
                        help='Run the suite of tests')
    args = parser.parse_args()

    if not args.test and not args.puzzle:
        print 'Please use a parameter with this program.'
        print "\tRerun the program with the '--help' flag for more details."
        exit(1)

    return args


if __name__ == '__main__':
    args = get_args()

    if args.puzzle:
        board = load_map(get_map_str(args.puzzle))
        for search in searches:
            (res, time) = run_search(deepcopy(board), search)
            print "{} seconds".format(time)

    elif args.test:
        print 'running tests...'
        pass


