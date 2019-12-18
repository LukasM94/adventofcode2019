#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import sys
class Direction:
    #dir:
    # 0...up
    # 1...right
    # 2...down
    # 3...left

    #turn:
    # 0...left
    # 1...rigth
    def __init__(self):
        self.dir = 0
        self.x = 0
        self.y = 0

    def move(self, turn):
        if turn == 0:
            self.dir -= 1
        elif turn == 1:
            self.dir += 1
        self.dir %= 4

        if self.dir == 0:
            self.y -= 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y += 1
        elif self.dir == 3:
            self.x -= 1

painted_panels = []
dir = Direction()
size = 200

def paint():
    global painted_panels
    global dir
    global size
    display = []
    for y in range(size):
        for x in range(size):
            color = '.'
            for entry in painted_panels:
                 if (x - size/2) == entry[0][0] and (y - size/2) == entry[0][1] and entry[1] == 1:
                     color = '#'
                     break
            display.append(color)
    address = (dir.y + size/2) * size + (dir.x + size/2)
    if dir.dir == 0:
        display[address] = "^"
    elif dir.dir == 1:
        display[address] = ">"
    elif dir.dir == 2:
        display[address] = "v"
    elif dir.dir == 3:
        display[address] = "<"

    print("--------------------------")
    for y in range(size):
        for x in range(size):
            address = y * size + x
            sys.stdout.write(display[address])
        sys.stdout.write('\n')
    print("--------------------------\n")


def executeOpcode():
    global painted_panels
    global dir
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    # for the second part
    painted_panels.append([[0, 0], 1])
    # print("pos = (" + str(dir.x) + ", " + str(dir.y) + ")")
    # paint()
    while True:
        color = 0
        found = False
        for entry in painted_panels:
             if entry[0][0] == dir.x and entry[0][1] == dir.y:
                 color = entry[1]
                 found = True
                 break
        p.stdin.write(str(color))
        p.stdin.write(b'\n')
        try:
            next_color = int(p.stdout.readline())
            turn = int(p.stdout.readline())
        except:
            break
        if found == False:
            painted_panels.append([[dir.x, dir.y], next_color])
        else:
            for entry in painted_panels:
                if entry[0][0] == dir.x and entry[0][1] == dir.y:
                    entry[1] = next_color
                    break
        dir.move(turn)
        # print("pos = (" + str(dir.x) + ", " + str(dir.y) + ")")
        # print("(" + str(next_color) + ", " + str(turn) + ")")
        # paint()
    paint()
    print("painted panels " + str(len(painted_panels)))


def main():
    executeOpcode()

if __name__ == "__main__":
    main()
