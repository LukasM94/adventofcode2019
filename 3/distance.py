#!/usr/bin/env python3
import math

def getCross(corner11, corner12, corner21, corner22):

    cross_x = math.inf
    cross_y = math.inf
    step_x  = math.inf
    step_y  = math.inf

    dx1 = abs(corner11[0] - corner12[0])
    dy1 = abs(corner11[1] - corner12[1])
    dx2 = abs(corner21[0] - corner22[0])
    dy2 = abs(corner21[1] - corner22[1])

    steps = min(corner11[2], corner12[2]) + min(corner21[2], corner22[2])

    if dx1 == 0:
        max_x   = max(corner21[0], corner22[0])
        min_x   = min(corner21[0], corner22[0])
        max_y   = max(corner11[1], corner12[1])
        min_y   = min(corner11[1], corner12[1])
        const_x = corner11[0]
        const_y = corner21[1]
        # print("min_x " + str(min_x) + " max_x " + str(max_x) + " min_y " + str(min_y) + " max_y " + str(max_y) + " const_x " + str(const_x) + " const_y " + str(const_y))
        if const_x >= min_x and const_x <= max_x:
            cross_x = const_x
            step_x  = abs(const_x - corner21[0])
        if const_y >= min_y and const_y <= max_y:
            cross_y = const_y
            step_y  = abs(const_y - corner11[1])

    if dy1 == 0:
        max_x   = max(corner11[0], corner12[0])
        min_x   = min(corner11[0], corner12[0])
        max_y   = max(corner21[1], corner22[1])
        min_y   = min(corner21[1], corner22[1])
        const_x = corner21[0]
        const_y = corner11[1]
        # print("min_x " + str(min_x) + " max_x " + str(max_x) + " min_y " + str(min_y) + " max_y " + str(max_y) + " const_x " + str(const_x) + " const_y " + str(const_y))
        if const_x >= min_x and const_x <= max_x:
            cross_x = const_x
            step_x  = abs(const_x - corner11[0])
        if const_y >= min_y and const_y <= max_y:
            cross_y = const_y
            step_y  = abs(const_y - corner21[1])

    # print("cross_x " + str(cross_x) + " cross_y " + str(cross_y))
    steps += step_x + step_y
    return [cross_x, cross_y, steps]


def getCorners(path):
    points = [[0,0,0]]
    x = 0
    y = 0
    steps = 0
    for corner in path:
        s = int(corner[1:])
        i = 0
        if corner[0] == 'R':
            x += s
        elif corner[0] == 'L':
            x -= s
        elif corner[0] == 'U':
            y += s
        elif corner[0] == 'D':
            y -= s
        steps += s
        points.append([x, y, steps])
    return points

file = open("input1", "r")
path1 = file.readline()
path2 = file.readline()
file.close()
path1 = path1.split(",")
path2 = path2.split(",")

# print(path1)
# print(path2)

corners1 = getCorners(path1)
corners2 = getCorners(path2)
common   = []
result   = []

print(corners1)
print(corners2)

i = 0
while i < (len(corners1) - 1):
    j = 0
    while j < (len(corners2) - 1):
        temp = getCross(corners2[j], corners2[j + 1], corners1[i], corners1[i + 1])
        if temp != []:
            common.append(temp)
        j += 1
    i += 1

for i in common:
    # sum = abs(i[0]) + abs(i[1])
    # result.append(sum)
    result.append(i[2])

result.sort()
print(result[1])
