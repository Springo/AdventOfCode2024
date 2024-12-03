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


lines = readFile("d03input.txt")

total = 0
total_2 = 0
enabled = True
for line in lines:
    ls = line.split("mul(")
    for item in ls[1:]:
        stage = 0
        last_idx = 0
        n1 = None
        n2 = None
        for i in range(len(item)):
            if 48 <= ord(item[i]) <= 57:
                continue
            elif item[i] == "," and stage == 0:
                n1 = int(item[last_idx:i])
                last_idx = i + 1
                stage += 1
            elif item[i] == ")" and stage == 1:
                n2 = int(item[last_idx:i])
                stage += 1
            else:
                break
        if n1 is not None and n2 is not None:
            total += n1 * n2
            if enabled:
                total_2 += n1 * n2

        en_idx = item.find("do()")
        dis_idx = item.find("don't()")
        if en_idx > dis_idx:
            enabled = True
        elif dis_idx > en_idx:
            enabled = False


print(total)
print(total_2)
