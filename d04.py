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


lines = readFile("d04input.txt")

grid = gdu.convert_to_grid(lines)


count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 'X':
            for dir in range(8):
                if gdu.grid_project(grid, i, j, dir, step=3)[0] is None:
                    continue
                i2, j2 = gdu.grid_project(grid, i, j, dir, step=1)
                if grid[i2][j2] != 'M':
                    continue
                i2, j2 = gdu.grid_project(grid, i, j, dir, step=2)
                if grid[i2][j2] != 'A':
                    continue
                i2, j2 = gdu.grid_project(grid, i, j, dir, step=3)
                if grid[i2][j2] != 'S':
                    continue
                count += 1


print(count)

count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 'A':
            lets = ""
            i2, j2 = gdu.grid_project(grid, i, j, 1, step=1)
            if i2 is None or (grid[i2][j2] != 'S' and grid[i2][j2] != 'M'):
                continue
            else:
                lets += grid[i2][j2]
            i2, j2 = gdu.grid_project(grid, i, j, 3, step=1)
            if i2 is None or (grid[i2][j2] != 'S' and grid[i2][j2] != 'M'):
                continue
            else:
                lets += grid[i2][j2]
            i2, j2 = gdu.grid_project(grid, i, j, 5, step=1)
            if i2 is None or (grid[i2][j2] != 'S' and grid[i2][j2] != 'M'):
                continue
            else:
                lets += grid[i2][j2]
            i2, j2 = gdu.grid_project(grid, i, j, 7, step=1)
            if i2 is None or (grid[i2][j2] != 'S' and grid[i2][j2] != 'M'):
                continue
            else:
                lets += grid[i2][j2]
            if lets == "SSMM" or lets == "SMMS" or lets == "MMSS" or lets == "MSSM":
                count += 1

print(count)
