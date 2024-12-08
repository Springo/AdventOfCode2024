import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project
from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d06input.txt")

grid = gdu.convert_to_grid(lines)

dir = 6
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            istart = i
            jstart = j


locs = set()
done = False
ix = istart
jx = jstart
locs.add((ix, jx))
while not done:
    i, j = gdu.grid_project(grid, ix, jx, dir=dir, step=1)
    if i is None:
        done = True
        break
    if grid[i][j] == "#":
        dir = (dir + 2) % 8
    else:
        ix = i
        jx = j
        #grid[ix][jx] = 'X'
        locs.add((i, j))

print(len(locs))


def check_loop(grid, ix, jx):
    locs = set()
    dir = 6
    done = False
    locs.add((ix, jx, dir))
    while not done:
        i, j = gdu.grid_project(grid, ix, jx, dir=dir, step=1)
        if i is None:
            break

        if grid[i][j] == "#":
            dir = (dir + 2) % 8
            if (i, j, dir) in locs:
                return True
            locs.add((i, j, dir))
        else:
            ix = i
            jx = j
            # grid[ix][jx] = 'X'
            if (i, j, dir) in locs:
                return True
            locs.add((i, j, dir))

    return False



count = 0
for il in range(len(grid)):
    for jl in range(len(grid[il])):
        if grid[il][jl] == '.':
            grid[il][jl] = '#'
            if check_loop(grid, istart, jstart):
                count += 1
            grid[il][jl] = '.'

print(count)

