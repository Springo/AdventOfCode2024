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


lines = readFile("d01input.txt")

l1 = []
l2 = []
for line in lines:
    ls = line.split()
    l1.append(int(ls[0]))
    l2.append(int(ls[1]))

l1 = sorted(l1)
l2 = sorted(l2)

total = 0
for i in range(len(l1)):
    total += abs(l1[i] - l2[i])
print(total)



total = 0
i = 0
j = 0
while i < len(l1) and j < len(l2):
    if l2[j] == l1[i]:
        total += l1[i]
        j += 1
    elif l2[j] > l1[i]:
        i += 1
    elif l2[j] < l1[i]:
        j += 1

print(total)

