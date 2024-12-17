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
    adj_list = dict()
    q = [(start_i, start_j)]
    explored = dict()
    explored[(start_i, start_j)] = True
    while len(q) > 0:
        i, j = q.pop(0)
        neigh = gdu.get_neighbors(grid, i, j, orth=True)
        new_node = False
        for k in range(len(neigh)):
            if neigh[k] == neigh[(k - 1) % len(neigh)] and neigh[k] == '.':
                new_node = True
            elif grid[i][j] == 'E' or grid[i][j] == 'S':
                new_node = True

        if new_node:
            adj_list[(i, j)] = dict()

        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True):
            if grid[i2][j2] == '.' or grid[i2][j2] == 'E':
                if (i2, j2) not in explored:
                    q.append((i2, j2))
                    explored[(i2, j2)] = True

    dirs = [0, 2, 4, 6]
    for i, j in adj_list:
        for dir in dirs:
            step = 1
            done = False
            while not done:
                i2, j2 = gdu.grid_project(grid, i, j, dir, step)
                if i2 is None:
                    done = True
                elif grid[i2][j2] == '#':
                    done = True
                elif (i2, j2) in adj_list:
                    vert = False
                    if dir == 2 or dir == 6:
                        vert = True
                    adj_list[(i, j)][(i2, j2)] = (step, vert)
                    adj_list[(i2, j2)][(i, j)] = (step, vert)
                    done = True
                step += 1

    return adj_list


def dijkstra(adj_list, start_i, start_j):
    q = [(0, start_i, start_j, False)]
    dist = dict()
    best_cost = dict()
    best_cost[(start_i, start_j, False)] = 0
    trail = dict()
    explored = dict()
    explored[(start_i, start_j, False)] = True

    while len(q) > 0:
        cost, i, j, vertical = heapq.heappop(q)
        if (i, j) not in dist:
            dist[(i, j)] = cost
        for ni, nj in adj_list[(i, j)]:
            n_cost, n_vert = adj_list[(i, j)][(ni, nj)]
            n_cost += cost
            if vertical != n_vert:
                n_cost += 1000

            if (ni, nj, n_vert) not in explored:
                heapq.heappush(q, (n_cost, ni, nj, n_vert))
                if (ni, nj, n_vert) in best_cost:
                    if n_cost < best_cost[(ni, nj, n_vert)]:
                        trail[(ni, nj, n_vert)] = {(i, j, vertical)}
                        best_cost[(ni, nj, n_vert)] = n_cost
                    elif n_cost == best_cost[(ni, nj)]:
                        trail[(ni, nj, n_vert)].add((i, j, vertical))
                else:
                    trail[(ni, nj, n_vert)] = {(i, j, vertical)}
                    best_cost[(ni, nj, n_vert)] = n_cost
                explored[(ni, nj, n_vert)] = True
            else:
                for k in range(len(q)):
                    f_cost, fi, fj, f_vert = q[k]
                    if fi == ni and fj == nj and f_vert == n_vert:
                        if n_cost < f_cost:
                            q[k] = (n_cost, fi, fj, f_vert)
                            heapq.heapify(q)
                            trail[(ni, nj, n_vert)] = {(i, j, vertical)}
                            best_cost[(ni, nj, n_vert)] = n_cost
                        elif n_cost == f_cost:
                            trail[(ni, nj, n_vert)].add((i, j, vertical))
    return dist, best_cost, trail


def count_path_tiles(adj_list, paths, source):
    q = [(source)]
    explored = set()
    added_nodes = {(source[0], source[1])}
    added_paths = set()
    total = 1
    while len(q) > 0:
        i, j, vert = q.pop(0)
        if (i, j, vert) in paths:
            for i2, j2, vert2 in paths[(i, j, vert)]:
                if (i2, j2, vert2) not in explored:
                    explored.add((i2, j2, vert2))
                    q.append((i2, j2, vert2))

                if (i, j, i2, j2) not in added_paths and (i2, j2, i, j) not in added_paths:
                    total += adj_list[(i, j)][(i2, j2)][0]
                    added_paths.add((i, j, i2, j2))

                    if (i2, j2) in added_nodes:
                        total -= 1
                    else:
                        added_nodes.add((i2, j2))
    return total







lines = readFile("d16input.txt")
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
        elif grid[i][j] == 'E':
            ei = i
            ej = j

adj_list = bfs(grid, si, sj)
dist, best_cost, trail = dijkstra(adj_list, si, sj)
print(dist[(ei, ej)])

evert = False
if (ei, ej, True) in best_cost:
    if (ei, ej, False) not in best_cost or best_cost[(ei, ej, True)] < best_cost[(ei, ej, False)]:
        evert = True

print(count_path_tiles(adj_list, trail, (ei, ej, evert)))

