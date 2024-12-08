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


def check_valid(x, y, cap_x, cap_y):
    if x < 0 or x >= cap_x:
        return False
    if y < 0 or y >= cap_y:
        return False
    return True


lines = readFile("d08input.txt")
grid = gdu.convert_to_grid(lines, convert_numeric=False)

antenna = dict()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            if grid[i][j] not in antenna:
                antenna[grid[i][j]] = []
            antenna[grid[i][j]].append((i, j))


antinodes = set()
cap_x = len(grid)
cap_y = len(grid[0])
for ant in antenna:
    for i in range(len(antenna[ant]) - 1):
        for j in range(i + 1, len(antenna[ant])):
            x, y = antenna[ant][i]
            x2, y2 = antenna[ant][j]
            diff_x = x2 - x
            diff_y = y2 - y
            if check_valid(x - diff_x, y - diff_y, cap_x, cap_y):
                antinodes.add((x - diff_x, y - diff_y))
            if check_valid(x2 + diff_x, y2 + diff_y, cap_x, cap_y):
                antinodes.add((x2 + diff_x, y2 + diff_y))

print(len(antinodes))


antinodes = set()
for ant in antenna:
    for i in range(len(antenna[ant]) - 1):
        for j in range(i + 1, len(antenna[ant])):
            x, y = antenna[ant][i]
            x2, y2 = antenna[ant][j]
            diff_x = x2 - x
            diff_y = y2 - y

            antinodes.add((x, y))
            antinodes.add((x2, y2))

            done = False
            new_x = x
            new_y = y
            while not done:
                new_x = new_x - diff_x
                new_y = new_y - diff_y
                if check_valid(new_x, new_y, cap_x, cap_y):
                    antinodes.add((new_x, new_y))
                else:
                    done = True

            done = False
            new_x = x2
            new_y = y2
            while not done:
                new_x = new_x + diff_x
                new_y = new_y + diff_y
                if check_valid(new_x, new_y, cap_x, cap_y):
                    antinodes.add((new_x, new_y))
                else:
                    done = True


print(len(antinodes))



