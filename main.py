
from board import load_map
from searches import breadth_first_search
import argparse





def get_args():
    parser = argparse.ArgumentParser(
        description='Get input for the sokoban program.')
    parser.add_argument('puzzle', metavar='P', type=str, nargs='?',
                        help='Puzzle to be solved by sokoban')
    parser.add_argument('--test', dest='test', action='store_const',
                        const=True, default=False,
                        help='Run the suite of tests')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    print args.puzzle
    print args.test

