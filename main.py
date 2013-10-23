
from board import load_map
from copy import deepcopy
from sys import exit
import argparse
import time

from searches import breadth_first_search as bfs
from searches import depth_first_search as dfs
from searches import uniform_cost_search as ucs

searches = [
    (bfs, 'breadth first search'),
    (dfs, 'depth first search'),
    (ucs, 'uniform cost search'),
]

def reportit(f):

    def report(*args, **kw):

        t_start = time.time()
        report, board = f(*args, **kw)
        runtime = (time.time()-t_start)

        print
        print 'Data for {}'.format(kw['name'])
        print ','.join(board.moves)
        print "a)\t{}\tNodes generated".format(report['node'])
        print "b)\t{}\tNodes repeated".format(report['repeat'])
        print 'c)\t{}\tNodes at the fringe of the search'.format(report['fringe'])
        print 'd)\t{}\tnodes explored'.format(len(report['explored']))
        print 'e)\t{}\t'.format(runtime)

    return report


@reportit
def run_search(board, search, steps, name=None):
    results, board = search(board, steps)
    return results, board


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
    parser.add_argument('--steps', dest='steps', action='store_const',
                        const=True, default=False)
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
        for search, search_name in searches:
            run_search(deepcopy(board), search, args.steps, name=search_name)

    elif args.test:
        print 'running tests...'
        pass
