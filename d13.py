import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project

from fractions import Fraction


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_inv(a, b, c, d):
    inv_det = Fraction(1, a * d - b * c)
    return [inv_det * d, -inv_det * b, -inv_det * c, inv_det * a]


def get_button_presses(a_button, b_button, prize_loc):
    a_x, a_y = a_button
    b_x, b_y = b_button
    p_x, p_y = prize_loc

    inv_1, inv_2, inv_3, inv_4 = get_inv(a_x, b_x, a_y, b_y)
    ans_a = inv_1 * p_x + inv_2 * p_y
    ans_b = inv_3 * p_x + inv_4 * p_y

    if ans_a.denominator == 1 and ans_b.denominator == 1 and ans_a > 0 and ans_b > 0:
        return 3 * ans_a + ans_b
    return 0


lines = readFile("d13input.txt")

a_buttons = []
b_buttons = []
prize_locs = []
for line in lines:
    if len(line) > 0:
        ls = line.split(": ")
        if ls[0] == "Button A":
            ls2 = ls[1].split(", ")
            a_buttons.append((int(ls2[0][2:]), int(ls2[1][2:])))
        elif ls[0] == "Button B":
            ls2 = ls[1].split(", ")
            b_buttons.append((int(ls2[0][2:]), int(ls2[1][2:])))
        else:
            ls2 = ls[1].split(", ")
            prize_locs.append((int(ls2[0][2:]), int(ls2[1][2:])))


part1 = 0
part2 = 0
for i in range(len(a_buttons)):
    part1 += get_button_presses(a_buttons[i], b_buttons[i], prize_locs[i])
    part2 += get_button_presses(a_buttons[i], b_buttons[i],
                                (prize_locs[i][0] + 10000000000000, prize_locs[i][1] + 10000000000000))

print(part1)
print(part2)




