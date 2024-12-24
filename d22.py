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


def next_num(num):
    n1 = num * 64
    num = (n1 ^ num) % 16777216
    n2 = num // 32
    num = (n2 ^ num) % 16777216
    n3 = num * 2048
    num = (n3 ^ num) % 16777216
    return num


lines = readFile("d22input.txt")
starts = []
for line in lines:
    starts.append(int(line))

total = 0
prices = dict()
for start in starts:
    num = start
    prev_num = start
    prev = []
    seen = set()
    for i in range(2000):
        num = next_num(num)
        prev.append((num % 10) - (prev_num % 10))
        prev_num = num
        if len(prev) == 4:
            key = tuple(prev)
            if key not in seen:
                prices[key] = prices.get(key, 0) + (num % 10)
                seen.add(key)
            prev.pop(0)
    total += num

print(total)
print(max(prices.values()))
