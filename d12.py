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


def bfs(grid, start_i, start_j, explored):
    if grid[start_i][start_j] == 'T':
        check = True
    else:
        check = False
    q = [(start_i, start_j)]
    explored[(start_i, start_j)] = True
    borders = dict()
    sides = 0
    area = 0
    perim = 0
    while len(q) > 0:
        i, j = q.pop(0)
        area += 1
        border_dirs = set()
        invalid_dirs = []
        dirs = [0, 2, 4, 6]
        k = 0
        for i2, j2 in gdu.get_neighbors(grid, i, j, orth=True, indices=True, default=(None, None)):
            if i2 is None:
                perim += 1
                border_dirs.add(dirs[k])
            else:
                if grid[i2][j2] == grid[i][j]:
                    if (i2, j2) not in explored:
                        q.append((i2, j2))
                        explored[(i2, j2)] = True
                    else:
                        if (i2, j2) in borders:
                            invalid_dirs.extend(list(borders[(i2, j2)]))
                else:
                    perim += 1
                    border_dirs.add(dirs[k])
            k += 1
        borders[(i, j)] = border_dirs
        sides += len(border_dirs)
        for dir in invalid_dirs:
            if dir in border_dirs:
                sides -= 1
        #sides += len(border_dirs.difference(invalid_dirs))
        if check:
            for dir in border_dirs.difference(invalid_dirs):
                print("({}, {}): {}".format(i + 1, j + 1, dir // 2))
    if check:
        print("SIDES: {}".format(sides))
    return area, perim, sides




lines = readFile("d12input.txt")
#lines = readFile("test.txt")
grid = gdu.convert_to_grid(lines)


total = 0
total_2 = 0
explored = dict()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) not in explored:
            area, perim, sides = bfs(grid, i, j, explored)
            total += area * perim
            total_2 += area * sides

            #print("{}: {}".format(grid[i][j], sides))

print(total)
print(total_2)
