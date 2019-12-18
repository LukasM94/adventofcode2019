#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

p = 0
map = []
width = 80
height = 80
x_D = 0
y_D = 0
started = False
count = 0
deadend = []
count_o2 = 0
o2 = 0

def addToMap(x, y, char):
    global map
    if [[x, y], char] not in map:
        # print("add x <" + str(x) + ">, y <" + str(y) + ">, char <" + char + ">")
        map.append([[x, y], char])

def drawMap():
    global map
    global height
    global width
    global x_D
    global y_D
    for y in range(height):
        row = []
        y -= height/2
        for x in range(width):
            x -= width/2
            if x == x_D and y == y_D:
                row.append("D")
            elif [[x, y], '#'] in map:
                row.append("#")
            elif [[x, y], '*'] in map:
                row.append("*")
            elif [[x, y], '.'] in map:
                row.append(".")
            else:
                row.append(" ")
        print(''.join(row))

def rightDir(dir):
    if dir == 1:
        return 4
    if dir == 2:
        return 3
    if dir == 3:
        return 1
    if dir == 4:
        return 2

def leftDir(dir):
    if dir == 1:
        return 3
    if dir == 2:
        return 4
    if dir == 3:
        return 2
    if dir == 4:
        return 1

def returnDir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    elif dir == 4:
        return 3

def determineCoordinate(x, y, dir):
    if dir == 1:
        return [x, y-1]
    if dir == 2:
        return [x, y+1]
    if dir == 3:
        return [x-1, y]
    if dir == 4:
        return [x+1, y]

def inverseDetermineCoordinate(x, y, dir):
    if dir == 1:
        return [x, y+1]
    if dir == 2:
        return [x, y-1]
    if dir == 3:
        return [x+1, y]
    if dir == 4:
        return [x-1, y]

def addToDeadend(x, y):
    global deadend
    global count_o2
    global o2
    found = False
    for i in range(len(deadend)):
        if deadend[i][0] == [x, y]:
            # print("deadend " + str(deadend[i]))
            if deadend[i][1] < count_o2:
                count_o2 = deadend[i][1]
            else:
                deadend[i][1] = count_o2
            found = True
    if found == False and o2 == 1:
        deadend.append([[x, y], count_o2])
    # print("x <" + str(x) + ">, y <" + str(y) + ">, count_o2 <" + str(count_o2) + ">")

def doMove(x, y, dir):
    global p
    global x_D
    global y_D
    global started
    global count
    global deadend
    global count_o2
    global o2
    started = True
    for i in range(3):
        p.stdin.write(str(dir) + '\n')
        result = int(p.stdout.readline()[:-1])
        # print("dir <" + str(dir) + ">, result <" + str(result) + ">, x<" + str(x) + ">, y<" + str(y) + ">")
        addToMap(x, y, '.')
        if result == 1:
            count_o2 += o2
            addToDeadend(x, y)
            x_D = x
            y_D = y
            drawMap()
            [x_next, y_next] = determineCoordinate(x, y, dir)
            dir_next = rightDir(dir)
            count += 1
            doMove(x_next, y_next, dir_next)
            count -= 1
        elif result == 0:
            [x_wall, y_wall] = determineCoordinate(x, y, dir)
            addToMap(x_wall, y_wall, '#')
        elif result == 2:
            p.stdin.write(str(returnDir(dir)) + '\n')
            p.stdout.readline()
            [x_star, y_star] = determineCoordinate(x, y, dir)
            dir_star = leftDir(dir)
            addToMap(x_star, y_star, '*')
            count += 1
            print("count " + str(count))
            o2 = 1
            count_o2 = 0
        dir = leftDir(dir)
    p.stdin.write(str(dir) + '\n')
    result = int(p.stdout.readline()[:-1])
    count_o2 += o2
    addToDeadend(x, y)
    # print("dir <" + str(dir) + ">, result <" + str(result) + ">, x<" + str(x) + ">, y<" + str(y) + ">")

def move():
    global p
    global deadend
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    doMove(0, 0, 1)
    drawMap()
    deadend.sort(key=lambda x:x[1])
    print(deadend)

def main():
    move()

if __name__ == "__main__":
    main()
