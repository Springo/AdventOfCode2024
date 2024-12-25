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


def bfs(grid, start_i, start_j):
    explored = dict()
    path = dict()
    q = [(start_i, start_j, 0)]
    explored[(start_i, start_j)] = True
    while len(q) > 0:
        i, j, dist = q.pop(0)
        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if (i2, j2) not in explored:
                if grid[i2][j2] in {'.', 'E', 'S'}:
                    q.append((i2, j2, dist + 1))
                    path[(i2, j2)] = ((i, j), dist + 1)
                explored[(i2, j2)] = True
    return path


def search_shortcut(path, cheat, start_i, start_j):
    i = start_i
    j = start_j
    base = path[(i, j)][1]
    traveled = 0
    total = 0
    saved_dict = dict()
    seen = set()
    while (i, j) in path:
        (ni, nj), dist = path[(i, j)]
        for (csi, csj) in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            for cei in range(csi - (cheat - 1), csi + (cheat - 1) + 1):
                rem_cheat = (cheat - 1) - abs(csi - cei)
                for cej in range(csj - rem_cheat, csj + rem_cheat + 1):
                    if (i, j, cei, cej) not in seen:
                        if (cei, cej) in path:
                            _, cd = path[(cei, cej)]
                            new_dist = traveled + cd + abs(i - cei) + abs(j - cej)
                            if new_dist < base:
                                saved = base - new_dist
                                if saved > 0:
                                    saved_dict[saved] = saved_dict.get(saved, 0) + 1
                                if saved >= 100:
                                    total += 1
                        seen.add((i, j, cei, cej))
        i = ni
        j = nj
        traveled += 1
    return total, saved_dict



lines = readFile("d20input.txt")
#lines = readFile("test.txt")

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

paths = bfs(grid, ei, ej)
paths[(ei, ej)] = ((-1, -1), 0)
total, cuts = search_shortcut(paths, 2, si, sj)
print(total)
total, cuts = search_shortcut(paths, 20, si, sj)
print(total)
