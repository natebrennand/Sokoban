
from map_loader import load_map
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
test_maps = [
    'easy_1',
    'easy_3',
    'moderate_1'
]

def reportit(f):

    def report(*args, **kw):

        t_start = time.time()
        report, board = f(*args, **kw)
        runtime = (time.time()-t_start)

        print """Data for {search_name}\n{moves}
        a)\t{generated}\tNodes generated
        b)\t{repeated}\tNodes repeated
        c)\t{fringe}\tNodes at the fringe of the search
        d)\t{explored}\tnodes explored
        e)\t{runtime} seconds
        """.format( search_name = kw['search_name'],
                    moves       = ','.join(board.moves),
                    generated   = report['node'],
                    repeated    = report['repeat'],
                    fringe      = report['fringe'],
                    explored    = len(report['explored']),
                    runtime     = runtime
        )
    return report


@reportit
def run_search(cli_args=None, puzzle_path=None, search=None, search_name=None):
    board = load_map(get_map_str(puzzle_path))
    results, board = search(board, print_steps=args.steps)
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


def test(args):
    for map_path in test_maps:
        print '{0}\n\tTesting on map {1}\n{0}'.format('-'*64, map_path)

        for search, search_name in searches:
            run_search( cli_args=args,
                puzzle_path='sokoban_boards/{}.txt'.format(map_path),
                search=search,
                search_name=search_name)


def puzzle(args):
    for search, search_name in searches:
        run_search(cli_args=args,
            puzzle_path=args.puzzle,
            search=search,
            search_name=search_name)


if __name__ == '__main__':
    args = get_args()

    if args.puzzle:
        puzzle(args)

    elif args.test:
        test(args)
