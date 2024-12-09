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


def update_checksum(pos, original, id, amount):
    new_pos = pos
    total = original
    for i in range(amount):
        total += new_pos * id
        new_pos += 1
    return new_pos, total


def merge_space(memory):
    i = 0
    last_space_i = None
    cumul_memory = 0
    while i < len(memory):
        amount, id, is_file = memory[i]
        if is_file:
            if last_space_i is not None:
                memory[last_space_i] = (cumul_memory, 0, False)
                while i > last_space_i + 1:
                    i -= 1
                    memory.pop(i)
                last_space_i = None
        else:
            if last_space_i is None:
                last_space_i = i
                cumul_memory = amount
            else:
                cumul_memory += amount
        i += 1



lines = readFile("d09input.txt")
diskmap = [int(x) for x in lines[0]]


pos = 0
p1 = 0
if len(diskmap) % 2 == 1:
    p2 = len(diskmap) - 1
else:
    p2 = len(diskmap) - 2
p1_id = 0
p2_id = p2 // 2
rem = diskmap[p2]


checksum = 0
while p1 <= p2:
    if p1 == p2:
        pos, checksum = update_checksum(pos, checksum, p1_id, rem)
        p1 += 1
    else:
        if p1 % 2 == 0:
            pos, checksum = update_checksum(pos, checksum, p1_id, diskmap[p1])
        else:
            if rem > diskmap[p1]:
                pos, checksum = update_checksum(pos, checksum, p2_id, diskmap[p1])
                rem -= diskmap[p1]
            else:
                pos, checksum = update_checksum(pos, checksum, p2_id, rem)
                diskrem = diskmap[p1] - rem
                rem = 0
                while diskrem > 0:
                    p2 -= 2
                    p2_id -= 1
                    if diskrem > diskmap[p2]:
                        pos, checksum = update_checksum(pos, checksum, p2_id, diskmap[p2])
                        diskrem -= diskmap[p2]
                    else:
                        pos, checksum = update_checksum(pos, checksum, p2_id, diskrem)
                        rem = diskmap[p2] - diskrem
                        diskrem = 0
            if rem == 0:
                p2 -= 2
                p2_id -= 1
                rem = diskmap[p2]
            p1_id += 1
        p1 += 1


print(checksum)

memory = []
for i in range(len(diskmap)):
    if i % 2 == 0:
        memory.append((diskmap[i], i // 2, True))
    else:
        memory.append((diskmap[i], 0, False))


fill_i = len(memory) - 1
while fill_i > 0:
    fill_amount, fill_id, fill_is_file = memory[fill_i]
    if fill_is_file:
        i = 0
        while i < fill_i:
            amount, id, is_file = memory[i]
            if not is_file:
                if amount >= fill_amount:
                    memory[i] = (amount - fill_amount, 0, False)
                    memory.insert(i, (fill_amount, fill_id, fill_is_file))
                    fill_i += 1
                    memory[fill_i] = (fill_amount, 0, False)
                    merge_space(memory)
                    break
            i += 1
    fill_i -= 1


pos = 0
checksum = 0
for i in range(len(memory)):
    amount, id, is_file = memory[i]
    if is_file:
        pos, checksum = update_checksum(pos, checksum, id, amount)
    else:
        pos += amount
print(checksum)



