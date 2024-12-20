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


def factor(pos):
    nums = [0, 0, 0, 0]
    for i in range(len(pos)):
        x, y = pos[i]
        if x < 50 and y < 51:
            nums[0] += 1
        elif x < 50 and y > 51:
            nums[1] += 1
        elif x > 50 and y < 51:
            nums[2] += 1
        elif x > 50 and y > 51:
            nums[3] += 1
    return nums[0] * nums[1] * nums[2] * nums[3]


lines= readFile("d14input.txt")
pos = []
vel = []
for line in lines:
    ls = line.split()
    ls1 = ls[0][2:].split(',')
    ls2 = ls[1][2:].split(',')
    pos.append((int(ls1[0]), int(ls1[1])))
    vel.append((int(ls2[0]), int(ls2[1])))

grid = [['.'] * 101 for _ in range(103)]
for i in range(len(grid)):
    x, y = pos[i]
    grid[y][x] = '@'

for step in range(11000):
    min_x = 101
    max_x = -1
    for i in range(len(pos)):
        x, y = pos[i]
        grid[y][x] = '.'
        vx, vy = vel[i]
        pos[i] = ((x + vx) % 101, (y + vy) % 103)
        grid[(y + vy) % 103][(x + vx) % 101] = '@'
    if step == 110:
    if step % 101 == 17:
        gdu.print_grid(grid)
        print(step + 1)




print(factor(pos))
