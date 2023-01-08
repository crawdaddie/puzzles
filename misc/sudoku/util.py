def add_tuples(t1, t2):
    return tuple([v + t2[i] for i, v in enumerate(t1)])

        
def parse_board_str(boardstr):
    board = [int(x) if x != '.' else 0 for x in boardstr.split(' ') if x and x != '\n']
    board = [[board[j + 9 * i] for j in range(9)] for i in range(9)]
    return board

def board_value(coords, board):
    r, c = coords
    return board[r][c]
