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


def convert_to_locs(pad):
    locs = dict()
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if pad[i][j] != '_':
                locs[str(pad[i][j])] = (i, j)
    return locs


keypad = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ['_', 0, 'A']
]
dirpad = [
    ['_', '^', 'A'],
    ['<', 'v', '>']
]
key_locs = convert_to_locs(keypad)
dir_locs = convert_to_locs(dirpad)


def code_to_ins(code):
    cur = 'A'
    ins = []
    for c in code:
        y1, x1 = key_locs[cur]
        y2, x2 = key_locs[c]
        if y1 == 3 and x2 == 0:
            ins.append(('^', y1 - y2))
            ins.append(('<', x1 - x2))
        elif x1 == 0 and y2 == 3:
            ins.append(('>', x2 - x1))
            ins.append(('v', y2 - y1))
        else:
            if x1 > x2:
                ins.append(('<', x1 - x2))
                if y2 > y1:
                    ins.append(('v', y2 - y1))
                elif y1 > y2:
                    ins.append(('^', y1 - y2))
            else:
                if y2 > y1:
                    ins.append(('v', y2 - y1))
                elif y1 > y2:
                    ins.append(('^', y1 - y2))
                if x2 > x1:
                    ins.append(('>', x2 - x1))
        ins.append(('A', 1))
        cur = c
    return ins


def ins_to_ins(ins):
    cur = 'A'
    new_ins = []
    for b, steps in ins:
        y1, x1 = dir_locs[cur]
        y2, x2 = dir_locs[b]
        if y1 == 0 and x2 == 0:
            new_ins.append(('v', y2 - y1))
            new_ins.append(('<', x1 - x2))
        elif x1 == 0 and y2 == 0:
            new_ins.append(('>', x2 - x1))
            new_ins.append(('^', y1 - y2))
        else:
            if x1 > x2:
                new_ins.append(('<', x1 - x2))
                if y2 > y1:
                    new_ins.append(('v', y2 - y1))
                elif y1 > y2:
                    new_ins.append(('^', y1 - y2))
            else:
                if y2 > y1:
                    new_ins.append(('v', y2 - y1))
                elif y1 > y2:
                    new_ins.append(('^', y1 - y2))
                if x2 > x1:
                    new_ins.append(('>', x2 - x1))
        new_ins.append(('A', steps))
        cur = b
    return new_ins


def convert_to_memo(ins):
    memo = dict()
    a = 0
    last_ins = ""
    for b, steps in ins:
        if b == 'A':
            memo[last_ins] = memo.get(last_ins, 0) + 1
            last_ins = ""
            a += steps
        else:
            cur = ""
            for s in range(steps):
                cur += b
            last_ins += cur
    return memo, a


def next_ins_memo(memo, a):
    def _str_to_ins(x):
        ins_list = []
        cur = x[0]
        steps = 1
        for c in x[1:]:
            if c == cur:
                steps += 1
            else:
                ins_list.append((cur, steps))
                cur = c
                steps = 1
        ins_list.append((cur, steps))
        ins_list.append(('A', 0))
        return ins_list

    new_memo = dict()
    new_a = a
    for key in memo:
        mult = memo[key]
        ins_list = _str_to_ins(key)
        ins_list = ins_to_ins(ins_list)
        ins_memo, ins_a = convert_to_memo(ins_list)
        for new_key in ins_memo:
            new_memo[new_key] = new_memo.get(new_key, 0) + mult
        new_a += ins_a * mult

    return new_memo, new_a


def count_steps(code, robots):
    start_ins = code_to_ins(code)
    ins = ins_to_ins(start_ins)
    memo, a = convert_to_memo(ins)
    for i in range(robots):
        memo, a = next_ins_memo(memo, a)
    return a


lines = readFile("d21input.txt")
codes = []
for line in lines:
    codes.append(line)


total_1 = 0
total_2 = 0
for code in codes:
    id = int(code[:-1])
    total_1 += id * count_steps(code, 2)
    total_2 += id * count_steps(code, 25)
print(total_1)
print(total_2)


