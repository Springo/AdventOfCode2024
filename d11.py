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


def stone_rule(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [str(int(stone[:len(stone) // 2])), str(int(stone[len(stone) // 2:]))]
    else:
        return [str(int(stone) * 2024)]


lines = readFile("d11input.txt")

stones = lines[0].split()

s_dict = dict()
for stone in stones:
    s_dict[stone] = 1
for i in range(75):
    new_stones = dict()
    for stone in s_dict:
        out_stone = stone_rule(stone)
        for stone_2 in out_stone:
            if stone_2 not in new_stones:
                new_stones[stone_2] = 0
            new_stones[stone_2] += s_dict[stone]
    s_dict = new_stones

total = 0
for key in s_dict:
    total += s_dict[key]
print(total)
