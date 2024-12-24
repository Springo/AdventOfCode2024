import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def bfs(grid, start_i, start_j, end_i, end_j, allowed_cuts=0):
    explored = dict()
    q = [(start_i, start_j, 0, 2, allowed_cuts)]
    explored[(start_i, start_j)] = True
    while len(q) > 0:
        i, j, dist, cut_tiles, cut_times = q.pop(0)
        if i == end_i and j == end_j:
            return dist
        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if (i2, j2) not in explored:
                if grid[i2][j2] == '.' or grid[i2][j2] == 'E':
                    if cut_tiles != 2:
                        cut_times = 0
                    q.append((i2, j2, dist + 1, cut_tiles, cut_times))
                elif grid[i2][j2] == '#':
                    if cut_times > 0 and cut_tiles > 0:
                        q.append((i2, j2, dist + 1, cut_tiles - 1, cut_times))
                explored[(i2, j2)] = True
    return -1


def bfs_broad(grid, start_i, start_j, end_i, end_j):
    explored = dict()
    dists = dict()
    q = [(start_i, start_j, 0)]
    explored[(start_i, start_j)] = True
    dirs = [0, 2, 4, 6]
    while len(q) > 0:
        i, j, dist = q.pop(0)

        for dir in dirs:
            i2, j2 = gdu.grid_project(grid, i, j, dir, step=1)
            if i2 is None:
                continue

            if grid[i2][j2] == '#':
                i3, j3 = gdu.grid_project(grid, i, j, dir, step=2)
                if i3 is None:
                    continue

                if grid[i3][j3] == '.':
                    new_dist = dist + bfs(grid, i3, j3, end_i, end_j)
                    if new_dist not in dists:
                        dists[new_dist] = 0
                    dists[new_dist] += 1
                else:
                    i4, j4 = gdu.grid_project(grid, i, j, dir, step=3)
                    if i4 is None:
                        continue

                    if grid[i4][j4] == '.':
                        new_dist = dist + bfs(grid, i4, j4, end_i, end_j)
                        if new_dist not in dists:
                            dists[new_dist] = 0
                        dists[new_dist] += 1

        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if (i2, j2) not in explored:
                if grid[i2][j2] == '.':
                    q.append((i2, j2, dist + 1))
                explored[(i2, j2)] = True
    return dists


lines = readFile("d20input.txt")

grid = gdu.convert_to_grid(lines)
si = 0
sj = 0
ei = 0
ej = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            si = i
            sj = j
        if grid[i][j] == 'E':
            ei = i
            ej = j

base = bfs(grid, si, sj, ei, ej)
dists = bfs_broad(grid, si, sj, ei, ej)

total = 0
for dist in dists:
    if base - dist >= 100:
        total += dists[dist]
print(total)
