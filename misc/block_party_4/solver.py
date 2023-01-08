
from collections import defaultdict


def parse_board(boardstr, rows, cols):
    board = [int(x) if x != '.' else 0 for x in boardstr.split(' ') if x and x != '\n']
    board = [[board[j + rows * i] for j in range(cols)] for i in range(rows)]
    return board

def parse_regions(regionstrs, rows, cols):
    regions = {}
    i = 0
    for r in regionstrs:
        rsplit = r.split(' ')
        regions[i] = [
                       (int(rsplit[r * 2]), int(rsplit[(2 * r) + 1])) for r in range(len(rsplit) // 2)
                       ]
        i += 1
    return regions

def add_tuples(t1, t2):
    return tuple([t1[i] + t2[i] for i, v in enumerate(t1)])

def nearest_k(k, r, col, rows, cols):
    candidates = set()
    for i in range(k + 1):
        c = (r + i, col + k - i)
        if c[0] >= 0 and c[0] < rows and c[1] >= 0 and c[1] < cols:
            candidates.add(c)

        c = (r - i, col + k - i)
        if c[0] >= 0 and c[0] < rows and c[1] >= 0 and c[1] < cols:
            candidates.add(c)

        c = (r + i, col + i - k)
        if c[0] >= 0 and c[0] < rows and c[1] >= 0 and c[1] < cols:
            candidates.add(c)


        c = (r - i, col + i - k)
        if c[0] >= 0 and c[0] < rows and c[1] >= 0 and c[1] < cols:
            candidates.add(c)

    return candidates

def debug_neighbors(start_val, regions, rows, cols):
    val, r, c = start_val
    grid = [[None] * cols for _ in range(rows)]
    grid[r][c] = val
    neighbors = nearest_k(val, r, c, rows, cols)
    for x in neighbors:
        for reg in regions:
            if x in regions[reg]:
                grid[x[0]][x[1]] = reg 

        
    
    debug = ''
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            str_v = str(v) if v is not None else '.'
            debug += str_v + ' ' 
        debug += '\n'

    print(debug)


def solve(start_vals, regions, rows, cols):
    grid = [[None] * cols for _ in range(rows)]
    for reg in regions:
        if len(regions[reg]) == 1:
            cell = regions[reg][0]
            start_vals.append((cell[0], cell[1], 1, reg))


    symbols = {}
    for reg in regions:
        l = len(regions[reg])
        for x in range(1, l + 1):
            t = symbols.get(x, 0)
            symbols[x] = t + 1 


        
    start_vals.sort(reverse=True, key=lambda x: x[2])


    for r, c, v, g in start_vals:
        symbols[v] -= 1
        grid[r][c] = v 
        
    print(symbols)


    def get_region_vals(grid, region):
        return [grid[r][c] for r, c in region]

    def get_region(coords, grid):
        for reg in regions:
            if coords in regions[reg]:
                return [(r, c, grid[r][c]) for r, c in regions[reg]]
        return None

    # for v, r, c, g in start_vals:
    #     grid[r][c] = v 
    #     neighbors = nearest_k(v, r, c, rows, cols)
    #     for neighbor in neighbors:
    #         for group_key in regions:
    #             if group_key == g:
    #                 continue
    #             print(v, get_region_vals(grid, regions[group_key]))

    get_neighbors = lambda v, r, c: nearest_k(v, r, c, rows, cols)


    # visited = set()
    # for r, c, v, g in start_vals:
    #     neighbors = get_neighbors(v, r, c)
    #     for neighbor in neighbors:
    #         group = get_region(neighbor, grid)
    #         if not group:
    #             continue
    #    
    #         if v > len(group) or (r, c, v) in group:
    #             continue
    #
    #         if v in set([v for r, c, v in group]):
    #             continue
    #
    #         nr, nc = neighbor
    #         if not grid[nr][nc]:
    #             grid[nr][nc] = v
    #             visited.add((nr, nc))

    # visited = set()
    # for r in range(rows):
    #     for c in range(cols):
    #         v = grid[r][c]
    #         if v:
    #             continue
    #         if (r, c) in visited:
    #             continue
    #         group = get_region((r, c), grid)
            # print(r, c, v, group)


            # neighbors = get_neighbors(cell_val, r, c)
            # for neighbor in neighbors:
            #
            #     group, key = get_region(neighbor)
            #
            #     if not group:
            #         continue
            #
            #     if cell_val > len(group) or (r, c, cell_val) in group:
            #         continue

                # if not neighbor in visited:
                #     grid[neighbor[0]][neighbor[1]] = cell_val
                #     visited.add(neighbor)

                # grid[neighbor[0]][neighbor[1]] = cell_val
                # visited.add((neighbor[0], neighbor[1]))

                



    return grid

def solve_str(start_vals, regions_str, rows, cols):
    regions = parse_regions(regions_str, rows, cols)
    grid = solve(start_vals, regions, rows, cols)


            


    debug = ''
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            str_v = str(v) if v is not None else '.'
            debug += str_v + ' ' 
        debug += '\n'

    print(debug)
    return


