import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project
from copy import copy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_triangles(adj_list):
    triangle_list = []
    keys = list(adj_list.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            for k in range(j + 1, len(keys)):
                k1 = keys[i]
                k2 = keys[j]
                k3 = keys[k]
                if k1 in adj_list[k2] and k1 in adj_list[k3] and k2 in adj_list[k3]:
                    triangle_list.append((k1, k2, k3))
    return triangle_list


def get_cliques(adj_list, R, P, X):
    if len(P) == 0 and len(X) == 0:
        return[copy(R)]
    cliques = []
    pivot = next(iter(P.union(X)))
    P_list = list(P)
    for v in P_list:
        if v not in adj_list[pivot]:
            R_new = copy(R)
            R_new.add(v)
            P_new = P.intersection(adj_list[v])
            X_new = X.intersection(adj_list[v])
            cliques.extend(get_cliques(adj_list, R_new, P_new, X_new))
            P.remove(v)
            X.add(v)
    return cliques






lines = readFile("d23input.txt")
adj_list = dict()
for line in lines:
    ls = line.split('-')
    if ls[0] not in adj_list:
        adj_list[ls[0]] = set()
    if ls[1] not in adj_list:
        adj_list[ls[1]] = set()
    adj_list[ls[0]].add(ls[1])
    adj_list[ls[1]].add(ls[0])


triangles = get_triangles(adj_list)
t_tri = []
for a, b, c in triangles:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        t_tri.append((a, b, c))
print(len(t_tri))


cliques = get_cliques(adj_list, set(), set(adj_list.keys()), set())
largest = 0
l_clique = None
for clique in cliques:
    if len(clique) > largest:
        largest = len(clique)
        l_clique = clique


l_clique = sorted(list(l_clique))
out = ""
for v in l_clique:
    out = "{},{}".format(out, v)
print(out[1:])
