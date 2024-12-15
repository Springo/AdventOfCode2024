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


class Box:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def get_opposite_coords(self, dir):
        if dir == 0:
            return [(self.i, self.j + 2)]
        elif dir == 2:
            return [(self.i + 1, self.j), (self.i + 1, self.j + 1)]
        elif dir == 4:
            return [(self.i, self.j - 1)]
        elif dir == 6:
            return [(self.i - 1, self.j), (self.i - 1, self.j + 1)]

    def move_coord(self, dir):
        if dir == 0:
            return [(self.i, self.j + 1), (self.i, self.j + 2)]
        elif dir == 2:
            return [(self.i + 1, self.j), (self.i + 1, self.j + 1)]
        elif dir == 4:
            return [(self.i, self.j - 1), (self.i, self.j)]
        elif dir == 6:
            return [(self.i - 1, self.j), (self.i - 1, self.j + 1)]

    def check_push(self, dir, grid):
        opp_coords = self.get_opposite_coords(dir)
        for i, j in opp_coords:
            if grid[i][j] == '#':
                return False
            elif isinstance(grid[i][j], Box):
                if not grid[i][j].check_push(dir, grid):
                    return False
        return True

    def push(self, dir, grid):
        if not self.check_push(dir, grid):
            return False

        opp_coords = self.get_opposite_coords(dir)
        for i, j in opp_coords:
            if isinstance(grid[i][j], Box):
                grid[i][j].push(dir, grid)
        grid[self.i][self.j] = '.'
        grid[self.i][self.j + 1] = '.'
        nc = self.move_coord(dir)
        grid[nc[0][0]][nc[0][1]] = self
        grid[nc[1][0]][nc[1][1]] = self
        self.i = nc[0][0]
        self.j = nc[0][1]
        return True

    def __repr__(self):
        return "B"



lines = readFile("d15input.txt")

dir_map = {
    '>': 0,
    'v': 2,
    '<': 4,
    '^': 6
}

grid_lines = []
instructions = []
phase = 0
for line in lines:
    if phase == 0:
        if len(line) == 0:
            phase = 1
        else:
            grid_lines.append(line)
    else:
        instructions.extend("".join(line))

grid = gdu.convert_to_grid(grid_lines)
instructions = [dir_map[x] for x in instructions]

ri = 0
rj = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            grid[i][j] = '.'
            ri = i
            rj = j


for dir in instructions:
    found = False
    steps = 1
    while not found:
        i, j = gdu.grid_project(grid, ri, rj, dir=dir, step=steps)
        if grid[i][j] == '.':
            found = True
            grid[i][j] = 'O'
            ri, rj = gdu.grid_project(grid, ri, rj, dir=dir, step=1)
            grid[ri][rj] = '.'
        elif grid[i][j] == '#':
            found = True
        steps += 1


total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'O':
            total += 100 * i + j

print(total)


raw_grid = gdu.convert_to_grid(grid_lines)
grid = []
i = 0
j = 0
ri = 0
rj = 0
for line in raw_grid:
    new_line = []
    for c in line:
        if c == '.':
            new_line.append('.')
            new_line.append('.')
        elif c == '#':
            new_line.append('#')
            new_line.append('#')
        elif c == 'O':
            new_box = Box(i, j)
            new_line.append(new_box)
            new_line.append(new_box)
        elif c == '@':
            ri = i
            rj = j
            new_line.append('.')
            new_line.append('.')
        j += 2
    grid.append(new_line)
    i += 1
    j = 0


for dir in instructions:
    i, j = gdu.grid_project(grid, ri, rj, dir=dir, step=1)
    if grid[i][j] == '.':
        ri = i
        rj = j
    elif isinstance(grid[i][j], Box):
        if grid[i][j].push(dir, grid):
            ri = i
            rj = j


total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if isinstance(grid[i][j], Box):
            if j == grid[i][j].j:
                total += 100 * i + j
print(total)



