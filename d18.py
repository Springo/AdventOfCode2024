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


def bfs(grid, start_i, start_j, end_i, end_j):
    explored = dict()
    q = [(start_i, start_j, 0)]
    explored[(start_i, start_j)] = True
    while len(q) > 0:
        i, j, dist = q.pop(0)
        if i == end_i and j == end_j:
            return dist
        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if (i2, j2) not in explored:
                if grid[i2][j2] == '.':
                    q.append((i2, j2, dist + 1))
                    explored[(i2, j2)] = True
    return -1


lines = readFile("d18input.txt")
end = 70
b_cutoff = 1024

grid = [['.'] * (end + 1) for _ in range(end + 1)]
bl = []
for line in lines:
    ls = line.split(',')
    bl.append((int(ls[0]), int(ls[1])))


for i in range(b_cutoff):
    y, x = bl[i]
    grid[y][x] = '#'

print(bfs(grid, 0, 0, end, end))


for i in range(b_cutoff, len(bl)):
    y, x = bl[i]
    grid[y][x] = '#'
    if bfs(grid, 0, 0, end, end) == -1:
        print('{},{}'.format(y, x))
        break


