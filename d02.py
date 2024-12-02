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


def is_safe(nums):
    dir_set = False
    decreasing = False
    for i in range(1, len(nums)):
        if dir_set is False:
            if nums[i] < nums[i - 1]:
                decreasing = True
            dir_set = True
        else:
            if nums[i] < nums[i - 1] and not decreasing:
                return False
            elif nums[i] > nums[i - 1] and decreasing:
                return False

        diff = abs(nums[i] - nums[i - 1])
        if not 1 <= diff <= 3:
            return False

    return True


lines = readFile("d02input.txt")

count = 0
count2 = 0
for line in lines:
    ls = line.split()
    nums_raw = [int(x) for x in ls]

    if is_safe(nums_raw):
        count += 1

    for j in range(len(nums_raw)):
        nums = nums_raw[:j] + nums_raw[j + 1:]
        if is_safe(nums):
            count2 += 1
            break

print(count)
print(count2)
