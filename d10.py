import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project
import heapq


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def bfs(grid, start_i, start_j):
    explored = dict()
    q = [(start_i, start_j)]
    explored[(start_i, start_j)] = True
    score = 0
    while len(q) > 0:
        i, j = q.pop(0)
        if grid[i][j] == 9:
            score += 1
        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if (i2, j2) not in explored:
                if grid[i2][j2] - grid[i][j] == 1:
                    q.append((i2, j2))
                    explored[(i2, j2)] = True
    return score


def bfs_2(grid, start_i, start_j):
    explored = dict()
    q = [(0, start_i, start_j)]
    explored[(start_i, start_j)] = 1
    score = 0
    while len(q) > 0:
        alt, i, j = heapq.heappop(q)
        if grid[i][j] == 9:
            score += explored[(i, j)]
        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if grid[i2][j2] - alt == 1:
                if (i2, j2) not in explored:
                    heapq.heappush(q, (grid[i2][j2], i2, j2))
                    explored[(i2, j2)] = explored[(i, j)]
                else:
                    explored[(i2, j2)] += explored[(i, j)]

    return score


lines = readFile("d10input.txt")
grid = gdu.convert_to_grid(lines)

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            total += bfs(grid, i, j)
print(total)

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            total += bfs_2(grid, i, j)
print(total)


