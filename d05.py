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


def check_error(nl, adj_list):
    for i in range(len(nl) - 1):
        for j in range(i + 1, len(nl)):
            if nl[i] in adj_list[nl[j]]:
                return i, j
    return None, None


lines = readFile("d05input.txt")

adj_list = dict()
mode = 0
num_lists = []
for line in lines:
    if len(line) == 0:
        mode += 1
        continue

    if mode == 0:
        ls = line.split('|')
        ls = [int(x) for x in ls]
        if ls[0] not in adj_list:
            adj_list[ls[0]] = set()
        if ls[1] not in adj_list:
            adj_list[ls[1]] = set()
        adj_list[ls[0]].add(ls[1])
    else:
        ls = line.split(',')
        num_lists.append([int(x) for x in ls])


count = 0
count_2 = 0
s_order = gu.top_sort(adj_list)
for nl in num_lists:
    fail = False
    for i in range(len(nl) - 1):
        for j in range(i + 1, len(nl)):
            if nl[i] in adj_list[nl[j]]:
                fail = True
    if not fail:
        count += nl[len(nl) // 2]
    else:

        new_nl = nl[:]
        done = False
        while not done:
            i2, j2 = check_error(new_nl, adj_list)
            if i2 is None:
                done = True
            else:
                temp = new_nl[i2]
                new_nl[i2] = new_nl[j2]
                new_nl[j2] = temp

        print(nl)
        print(new_nl)
        count_2 += new_nl[len(new_nl) // 2]

print(count)
print(count_2)


