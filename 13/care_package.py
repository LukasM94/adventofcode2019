#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

grid   = []
width  = 44
height = 24
p      = 0
x_ball = 0
y_ball = 0
x_paddle = 0
y_paddle = 0
blocks = 0

def drawGrid():
    global grid
    for entry in grid:
        print(''.join(entry))

def getTiles():
    global width
    global height
    global grid
    global p
    global x_ball
    global y_ball
    global x_paddle
    global y_paddle
    global blocks
    tiles =[]
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    for i in range(width * height):
        x = int(p.stdout.readline())
        y = int(p.stdout.readline())
        tile = int(p.stdout.readline())
        tiles.append([x, y, tile])
    # print(tiles)
    # width  = int(tiles[-1][0])
    # height = int(tiles[-1][1])
    grid   = [[tiles[x + width * y][2] for x in range(width)] for y in range(height)]
    blocks = 0
    for x in range(width):
        for y in range(height):
            if grid[y][x] == 0:
                grid[y][x] = ' '
            elif grid[y][x] == 1:
                grid[y][x] = '#'
            elif grid[y][x] == 2:
                blocks += 1
                grid[y][x] = 'B'
            elif grid[y][x] == 3:
                grid[y][x] = '='
                x_paddle = x
            elif grid[y][x] == 4:
                grid[y][x] = 'O'
                x_ball = x
    drawGrid()
    print(blocks)

def refresh():
    global grid
    global p
    global blocks
    global x_paddle
    global x_ball
    while True:
        x = int(p.stdout.readline())
        y = int(p.stdout.readline())
        tile = int(p.stdout.readline())
        print("incomming: <" + str(x) + "> <" + str(y) + "> <" + str(tile) + ">")

        if x == -1:
            print("score is " + str(tile))

        if grid[y][x] == 'B':
            blocks -= 1

        if tile == 0:
            grid[y][x] = ' '
        elif tile == 1:
            grid[y][x] = '#'
        elif tile == 2:
            grid[y][x] = 'B'
        elif tile == 3:
            grid[y][x] = '='
            x_paddle = x
        elif tile == 4:
            grid[y][x] = 'O'
            x_ball = x
            return True

def play():
    global width
    global height
    global grid
    global p
    global blocks
    global x_paddle
    global x_ball
    x = int(p.stdout.readline())
    y = int(p.stdout.readline())
    score = int(p.stdout.readline())
    print("===================start====================")
    while blocks > 0:
        drawGrid()
        if x_ball == x_paddle:
            p.stdin.write(b'0\n')
            print("outgoing <0>")
        elif x_ball < x_paddle:
            p.stdin.write(b'-1\n')
            print("outgoing <-1>")
        elif x_ball > x_paddle:
            p.stdin.write(b'1\n')
            print("outgoing <1>")
        # print("tip input:")
        # joystick = int(input())
        # if joystick == 1:
        #     p.stdin.write(b'-1\n')
        #     print("outgoing <-1>")
        # elif joystick == 2:
        #     p.stdin.write(b'0\n')
        #     print("outgoing <0>")
        # elif joystick == 3:
        #     p.stdin.write(b'1\n')
        #     print("outgoing <1>")
        try:
            refresh()
        except:
            drawGrid()
            break
    print("===================finish===================")

def main():
    getTiles()
    play()

if __name__ == "__main__":
    main()
