from block_party_4.solver import solve_str
# easy
board = '''
    . . . . . 
    . . . . 2 
    . . 4 . . 
    3 . . . . 
    . . . . . 
'''
start_vals = [
    (3, 0, 3, 2), # row, column, value, group
    (2, 2, 4, 0),
    (1, 4, 2, 1)
]
regions = [
    '0 0 0 1 1 1 1 2 2 2',
    '0 2 0 3 0 4 1 4 2 4',
    '1 0 2 0 3 0 4 0 4 1',
    '2 1',
    '1 3',
    '3 1 3 2 4 2',
    '2 3 3 3 3 4 4 4',
    '4 3'
]


if __name__ == '__main__':

    solve_str(start_vals, regions, 5, 5)
    print('---------')

#hard
board = '''
    . 3 . . . 7 . . . . 
    . . . 4 . . . . . . 
    . . . . . . . . 2 . 
    . . . 1 . . . . . . 
    6 . 1 . . . . . . . 
    . . . . . . . 3 . 6 
    . . . . . . . . . . 
    . . . . . . . . . . 
    . . . . . . . . . . 
    . . . . . . . . . . 
'''
