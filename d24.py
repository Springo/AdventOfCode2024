import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project
from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def eval_func(func, vals):
    arg1, op, arg2 = func
    if op == "AND":
        return vals[arg1] * vals[arg2]
    elif op == "OR":
        return vals[arg1] | vals[arg2]
    elif op == "XOR":
        return vals[arg1] ^ vals[arg2]


def recurse_eval(out, funcs, vals):
    arg1, op, arg2 = funcs[out]
    if arg1 not in vals:
        recurse_eval(arg1, funcs, vals)
    if arg2 not in vals:
        recurse_eval(arg2, funcs, vals)
    vals[out] = eval_func(funcs[out], vals)


def get_trace(out, funcs):
    arg1, op, arg2 = funcs[out]
    if arg1[0] == 'x' or arg1[0] == 'y':
        return "({}: {} {} {})".format(out, arg1, op, arg2)
    return "({}: {} {} {})".format(out, get_trace(arg1, funcs), op, get_trace(arg2, funcs))


lines = readFile("d24input.txt")

base_vals = dict()
vals = dict()
adj_list = dict()
funcs = dict()
phase = 0
for line in lines:
    if len(line) == 0:
        phase += 1
        continue
    if phase == 0:
        ls = line.split(": ")
        vals[ls[0]] = int(ls[1])
        base_vals[ls[0]] = int(ls[1])
    else:
        ls = line.split()
        if ls[0] not in adj_list:
            adj_list[ls[0]] = set()
        if ls[2] not in adj_list:
            adj_list[ls[2]] = set()
        if ls[4] not in adj_list:
            adj_list[ls[4]] = set()
        adj_list[ls[0]].add(ls[4])
        adj_list[ls[2]].add(ls[4])
        funcs[ls[4]] = (ls[0], ls[1], ls[2])


sorted_list = gu.top_sort(adj_list)
for out in sorted_list:
    if out not in vals:
        vals[out] = eval_func(funcs[out], vals)


z_vals = [0] * len(sorted_list)
for key in vals:
    if key[0] == 'z':
        z_vals[int(key[1:])] = vals[key]

z_joined = ""
for c in z_vals:
    z_joined = str(c) + z_joined
print(int(z_joined, 2))


rems = dict()
carries = dict()
for key in funcs:
    arg1, op, arg2 = funcs[key]
    if arg1[0] == 'x' or arg1[0] == 'y':
        dig = int(arg1[1:])
        if op == 'XOR':
            rems[dig] = key
        elif op == 'AND':
            carries[dig] = key


x = [0] * 45
y = [0] * 45
z = [0] * 45
for i in range(45):
    x[i] = vals['x{}'.format(str(i).zfill(2))]
    y[i] = vals['y{}'.format(str(i).zfill(2))]

x_str = ''.join(map(str, x[::-1]))
y_str = ''.join(map(str, y[::-1]))
x_int = int(x_str, 2)
y_int = int(y_str, 2)
z_true_int = x_int + y_int
z_true_str = reversed(bin(z_true_int)[2:])
z_true = [int(a) for a in list(z_true_str)]


vals = deepcopy(base_vals)
for i in range(45):
    keyname = "z{}".format(str(i).zfill(2))
    recurse_eval(keyname, funcs, vals)
    z[i] = vals[keyname]
    if z[i] != z_true[i]:
        print(i)
        print(get_trace(keyname, funcs))
        break

# swap z06 and ksv
# swap nbd and kbs
# swap z20 and tqq
# swap z39 and ckb


answer = ["z06", "ksv", "nbd", "kbs", "z20", "tqq", "z39", "ckb"]
answer = sorted(answer)
text_answer = ""
for a in answer:
    text_answer = "{},{}".format(text_answer, a)
print(text_answer)


