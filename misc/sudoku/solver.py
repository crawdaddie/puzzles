import collections

from .util import add_tuples, parse_board_str



sub_square = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
full_set = set([1,2,3,4,5,6,7,8,9])

regions = [
    sub_square,
    [add_tuples(e, (0, 3)) for e in sub_square],
    [add_tuples(e, (0, 6)) for e in sub_square],
    [add_tuples(e, (3, 0)) for e in sub_square],
    [add_tuples(e, (3, 3)) for e in sub_square],
    [add_tuples(e, (3, 6)) for e in sub_square],
    [add_tuples(e, (6, 0)) for e in sub_square],
    [add_tuples(e, (6, 3)) for e in sub_square],
    [add_tuples(e, (6, 6)) for e in sub_square],
]


def is_valid(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key = (r /3, c /3)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    # for r in regions:
    #     if set([board_value(e, board) for e in r]) != full_set:
    #         return False
    # for r in board:
    #     if set(r) != full_set:
    #         return False
    # for c in [[board[i][j] for i in range(9)] for j in range(9)]:
    #     if set(c) != full_set:
    #         return False
    return True

def solve(board):
    for r in range(9):
        for c in range(9):
            print(board[r][c])

    return []

def solve_str(boardstr):
    board = parse_board_str(boardstr)
    if not is_valid(board):
        raise Exception('invalid board input')
    solution = solve(board)
    print(boardstr, solution)

