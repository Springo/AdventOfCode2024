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


lines = readFile("d07input.txt")
eqs = []
for line in lines:
    ls = line.split(": ")
    ops = [int(x) for x in ls[1].split()]
    eqs.append((int(ls[0]), ops))


total = 0
for target, ops in eqs:
    poss_vals = {ops[0]}
    for i in range(1, len(ops)):
        new_vals = set()
        for val in poss_vals:
            new_vals.add(val + ops[i])
            new_vals.add(val * ops[i])
            new_vals.add(int(str(val) + str(ops[i])))
        poss_vals = new_vals

    if target in poss_vals:
        total += target
print(total)
