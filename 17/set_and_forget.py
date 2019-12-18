#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

map = []
x_robot = 0
y_robot = 0
ways = []
patterns = []

def printMap():
    global map
    for i in map:
        print(''.join(i))

def readMap():
    global map
    global x_robot
    global y_robot
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    try:
        row = []
        x = 0
        y = 0
        while True:
            temp = int(p.stdout.readline()[:-1])
            if temp == 35:
                row.append("#")
                x += 1
            elif temp == 46:
                row.append(".")
                x += 1
            elif temp == 10:
                map.append(row)
                y += 1
                x = 0
                row = []
            else:
                row.append("^")
                x_robot = x
                y_robot = y
    except:
        return

def scanMap():
    global map
    parameter = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            try:
                center = (map[y][x] == '#')
                up = (map[y - 1][x] == '#')
                down = (map[y + 1][x] == '#')
                right = (map[y][x + 1] == '#')
                left = (map[y][x - 1] == '#')
                count = center + up + down + right + left
                if count == 5:
                    parameter += (x*y)
                    # map[y][x] = 'O'
            except:
                continue
    print(parameter)

def prepareForPart1():
    file = open("input", "w")
    file1 = open("input1", "r")
    input1 = file1.read()
    file.seek(0)
    file.write(input1)
    file1.close()
    file.close()

def prepareForPart2():
    file = open("input", "w")
    file2 = open("input2", "r")
    input2 = file2.read()
    file.seek(0)
    file.write(input2)
    file2.close()
    file.close()

def getDir(x, y):
    global map
    try:
        return int((map[y][x] == '#' or map[y][x] == 'O' or map[y][x] == 'x'))
    except:
        return 0

def getUp(x, y):
    return getDir(x, y) * 1

def getRight(x, y):
    return getDir(x, y) * 2

def getDown(x, y):
    return getDir(x, y) * 4

def getLeft(x, y):
    return getDir(x, y) * 8

def getInv(dir):
    if dir == 0:
        return 0
    elif dir == 1:
        return 4
    elif dir == 2:
        return 8
    elif dir == 4:
        return 1
    elif dir == 8:
        return 2

def getTurn(next_dir, dir):
    if next_dir == 1 and dir == 8:
        return 'R'
    if next_dir == 8 and dir == 1:
        return 'L'
    if next_dir > dir:
        return 'R'
    else:
        return 'L'

def getScaffoldData():
    global map
    global x_robot
    global y_robot
    global ways
    x = x_robot
    y = y_robot
    x_old = x
    y_old = y
    dir = 0
    local_map = map
    while True:
        printMap()
        up = getUp(x,y-1)
        down = getDown(x,y+1)
        right = getRight(x+1,y)
        left = getLeft(x-1,y)
        # print("up <" + str(up) + ">, right <" + str(right) + ">, down <" + str(down) + ">, left <" + str(left) + ">")
        next_dir = up | down | right | left
        inv_dir = getInv(dir)
        # print("inv_dir " + bin(inv_dir))
        # print("next_dir " + bin(next_dir))
        prev_dir = dir
        dir = next_dir & ~inv_dir
        if __debug__: print("dir <" + str(dir) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
        while (next_dir & dir) != 0:
            if dir == 1:
                y -= 1
            elif dir == 2:
                x += 1
            elif dir == 4:
                y += 1
            elif dir == 8:
                x -= 1
            up = getUp(x,y-1)
            down = getDown(x,y+1)
            right = getRight(x+1,y)
            left = getLeft(x-1,y)
            next_dir = up | down | right | left
        map[y][x] = 'x'
        if dir == 0:
            break
        x_delta = abs(x - x_old)
        y_delta = abs(y - y_old)
        ways.append([getTurn(dir, prev_dir), abs(x_delta + y_delta)])
        x_old = x
        y_old = y
    print(ways)
    if __debug__: print(len(ways))
    temp = []
    for entry in ways:
        if entry not in temp:
            temp.append(entry)
    if __debug__: print(temp)

def patternSearch():
    global ways
    global patterns
    for start in range(len(ways)):
        size = 1
        if __debug__: print("start " + str(start))
        while size < 6:
            if __debug__: print("ways[start:size] is " + str(ways[start:(start+size)]))
            if ways[start:(start+size)] not in patterns:
                if __debug__: print("appended")
                patterns.append(ways[start:(start+size)])
            size += 1

def printPattern():
    global patterns
    for entry in patterns:
        print(entry)

def getPattern(i, used_patterns, count):
    if __debug__: print("i <" + str(i) + ">")
    global patterns
    global ways
    if len(used_patterns) > 3 or count > 10:
        return []
    if i == len(ways):
        print("gotit")
        return used_patterns
    for pattern in patterns:
        size_of_pattern = len(pattern)
        # print(str(pattern) + " ?= " + str(ways[i:(i+size_of_pattern)]))
        # print(str(pattern == ways[i:(i+size_of_pattern)]))
        if ways[i:(i+size_of_pattern)] == pattern:
            ret = []
            # print(used_patterns)
            count += 1
            if pattern in used_patterns:
                ret = getPattern((i+size_of_pattern), used_patterns, count)
                if ret != []:
                    return ret
            else:
                used_patterns.append(pattern)
                ret = getPattern((i+size_of_pattern), used_patterns, count)
                if ret != []:
                    return ret
                else:
                    used_patterns.remove(pattern)
            count -= 1
    return []

def parsePattern(pattern):
    global ways
    A = ""
    B = ""
    C = ""
    FUNC = "A,A,B,C,B,C,B,C,B,A"
    for a in pattern[0]:
        A += str(a[0]) + "," + str(a[1]) + ","
    for b in pattern[1]:
        B += str(b[0]) + "," + str(b[1]) + ","
    for c in pattern[2]:
        C += str(c[0]) + "," + str(c[1]) + ","
    A = A[:-1]
    B = B[:-1]
    C = C[:-1]
    print("A is    " + A)
    print("B is    " + B)
    print("C is    " + C)
    print("FUNC is " + FUNC)
    return [FUNC + '\n', A + '\n', B + '\n', C + '\n']

def doPart2(FUNC, A, B, C):
    # p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    # p.stdin.write(FUNC + '\n')
    # p.stdin.write(A + '\n')
    # p.stdin.write(B + '\n')
    # p.stdin.write(C + '\n')
    # p.stdin.write('n\n')
    # result = int(p.stdout.readline())
    # print(result)
    for c in FUNC:
        a = ord(c)
        print(a)
    for c in A:
        a = ord(c)
        print(a)
    for c in B:
        a = ord(c)
        print(a)
    for c in C:
        a = ord(c)
        print(a)
    print(ord('n'))
    print(ord('\n'))

def main():
    prepareForPart1()
    readMap()
    scanMap()
    printMap()
    prepareForPart2()
    getScaffoldData()
    patternSearch()
    # printPattern()
    pattern = getPattern(0, [], 0)
    # for entry in pattern:
    #     print(entry)
    [FUNC, A, B, C] = parsePattern(pattern)
    doPart2(FUNC, A, B, C)

if __name__ == "__main__":
    main()
