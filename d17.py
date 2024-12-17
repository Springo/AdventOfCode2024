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


def combo(op, a, b, c):
    if op <= 3:
        return op
    elif op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c


def run_program(program, a, b, c):
    p = 0
    out = []
    while p < len(program):
        ins = program[p]
        arg = program[p + 1]

        if ins == 0:
            num = a
            denom = 2 ** combo(arg, a, b, c)
            a = num // denom
        elif ins == 1:
            b = b ^ arg
        elif ins == 2:
            b = combo(arg, a, b, c) % 8
        elif ins == 3:
            if a != 0:
                p = arg - 2
        elif ins == 4:
            b = b ^ c
        elif ins == 5:
            out.append(combo(arg, a, b, c) % 8)
        elif ins == 6:
            num = a
            denom = 2 ** combo(arg, a, b, c)
            b = num // denom
        elif ins == 7:
            num = a
            denom = 2 ** combo(arg, a, b, c)
            c = num // denom
        p += 2

    return out


def translated_program(a, b, c):
    out = []
    done = False
    while not done:
        b = (a % 8) ^ 3
        c = a // (2 ** b)
        b = (b ^ 5 ^ c)
        a = a // 8
        out.append(b % 8)
        if a == 0:
            done = True
    return out


def invert_program(program):
    b = 0
    c = 0
    options = []
    for a in range(2 ** 10):
        out = translated_program(a, b, c)
        if out[0] == program[0]:
            options.append(a)

    for i in range(1, len(program)):
        new_options = []
        for a_raw in options:
            for a_plus in range(2 ** 3):
                a = a_raw + a_plus * (2 ** (10 + 3 * (i - 1)))
                out = translated_program(a, b, c)
                if len(out) >= (i + 1) and out[i] == program[i]:
                    new_options.append(a)
        options = new_options

    return options



a = 33024962
b = 0
c = 0
program = [2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0]


out = run_program(program, a, b, c)
final_out = ""
for c in out:
    final_out += str(c) + ','
final_out = final_out[:-1]
print(final_out)

inverses = invert_program(program)

print(min(inverses))
