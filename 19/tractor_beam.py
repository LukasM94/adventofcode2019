#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

height = 100

def readMap():
    global height
    map = []
    file = open("beam", "r")
    for i in range(height):
        map.append(list(file.readline()))
    return map

def printMap(map):
    for line in map:
        print(''.join(line)[:-1])

def getCount(map):
    count = 0
    for line in map:
        for c in line:
            count += int(c == '#')
    return count

def doPart2(map):
    x1 = 14
    y1 = 13
    delta1 = 12
    x2 = 8
    y2 = 5
    delta2 = 3

    # print(map[y1][x1] == '.')
    # print(map[y2][x2] == '.')
    # map[y1][x1] = 'x'
    # map[y2][x2] = 'y'
    # printMap(map)
    # map[y1][x1] = '.'
    # map[y2][x2] = '.'

    i = 0
    while y1 != y2:
        i  += 1
        if i % delta2 == 0:
            x2 += 1
        x2 += 1
        y2 += 1

    # print(map[y1][x1] == '.')
    # print(map[y2][x2] == '.')
    # map[y1][x1] = 'x'
    # map[y2][x2] = 'y'
    # printMap(map)
    # map[y1][x1] = '.'
    # map[y2][x2] = '.'

    j = 0
    while y1 - y2 <= 100:
        j  += 1
        if j % delta1 == 0:
            x1 += 1
        x1 += 1
        y1 += 1

    while True:
        i  += 1
        if i % delta2 == 0:
            x2 += 1
        x2 += 1
        y2 += 1

        if x2 - x1 > 100:
            break

        j  += 1
        if j % delta1 == 0:
            x1 += 1
        x1 += 1
        y1 += 1

    # print(map[y1][x1] == '.')
    # print(map[y2][x2] == '.')
    # map[y1][x1] = 'x'
    # map[y2][x2] = 'y'
    # printMap(map)
    # map[y1][x1] = '.'
    # map[y2][x2] = '.'

    # A = []
    # for y in range(10):
    #     row = []
    #     for x in range(10):
    #         p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    #         p.stdin.write(str(x - 5 + x1) + '\n')
    #         p.stdin.write(str(y - 5 + y1) + '\n')
    #         # print("write x <" + str(x) + ">, y <" + str(y) + ">")
    #         c = int(p.stdout.readline())
    #         # print("read " + str(c))
    #         if c == 1:
    #             row.append('#')
    #         else:
    #             row.append('.')
    #     A.append(row)
    #
    # B = []
    # for y in range(10):
    #     row = []
    #     for x in range(10):
    #         p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    #         p.stdin.write(str(x - 5 + x2) + '\n')
    #         p.stdin.write(str(y - 5 + y2) + '\n')
    #         # print("write x <" + str(x) + ">, y <" + str(y) + ">")
    #         c = int(p.stdout.readline())
    #         # print("read " + str(c))
    #         if c == 1:
    #             row.append('#')
    #         else:
    #             row.append('.')
    #     B.append(row)
    #
    # B[5][5] = 'x'
    # print("x <" + str(x2) + ">, y <" + str(y2) + ">")
    # for line in B:
    #     print(''.join(line))
    #
    # A[5][5] = 'x'
    # print("x <" + str(x1) + ">, y <" + str(y1) + ">")
    # for line in A:
    #     print(''.join(line))

    x1 -= 6
    y2 -= 5

    A = []
    for y in range(100):
        row = []
        for x in range(100):
            if x < 99 and x > 0 and y < 99 and y > 0:
                row.append(' ')
                continue
            p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
            p.stdin.write(str(x + x1) + '\n')
            p.stdin.write(str(y + y2) + '\n')
            # print("write x <" + str(x) + ">, y <" + str(y) + ">")
            c = int(p.stdout.readline())
            # print("read " + str(c))
            if c == 1:
                row.append('#')
            else:
                row.append('.')
        A.append(row)
    for line in A:
        print(''.join(line))

    print(str(10000*x1 + y2))

    # for y in range(10):
    #     for x in range(10):
    #         if map[y2 + y][x1 + x] != '#':
    #             print("fail x <" + str(x) + ">, y <" + str(y) + ">")

def main():
    map = readMap()
    printMap(map)
    count = getCount(map)
    print(count)
    doPart2(map)

if __name__ == "__main__":
    main()
