#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

p = 0
droid = 0

class Droid:
    def __init__(self):
        self.x_ = 0
        self.y_ = 0
        self.positions_ = []
        self.possible_movements_ = []
        self.movements_ = []
        self.walls_ = []
        self.count_ = 0
        self.width_ = 100
        self.height_ = 100
        self.return_ = False
        self.found_ = False
        self.o2_ = []

    def discover(self):
        global p
        directions = 0
        for i in range(4):
            dir = i + 1
            p.stdin.write(str(dir) + '\n')
            result = int(p.stdout.readline())
            if result == 1:
                directions += self.saveStreet(dir)
                dir = returnDir(dir)
                p.stdin.write(str(dir) + '\n')
                result = int(p.stdout.readline())
            elif result == 2:
                # print("possible_movements_ " + str(self.possible_movements_))
                # print("movements_ " + str(self.movements_))
                # print("positions_ " + str(self.positions_))
                # print("size of movements " + str(len(self.movements_)))
                self.saveWall(dir, '*')
                # self.draw()
                dir = returnDir(dir)
                p.stdin.write(str(dir) + '\n')
                result = int(p.stdout.readline())
                self.found_ = True
            else:
                self.saveWall(dir, '#')
        if directions == 0:
            # print("deadlock")
            # self.draw()
            # print("possible_movements_ " + str(self.possible_movements_))
            # print("movements_ " + str(self.movements_))
            # print("positions_ " + str(self.positions_))
            self.return_ = True
            if self.found_ == True:
                found = False
                for entry in self.o2_:
                    if self.x_ == entry[0] and self.y_ == entry[1]:
                        self.count_ = entry[2]
                        found = True
                if found == False:
                    self.o2_.append([self.x_, self.y_, self.count_])
                print("count " + str(self.count_))
        elif directions > 2:
            if self.found_ == True:
                found = False
                for entry in self.o2_:
                    if self.x_ == entry[0] and self.y_ == entry[1]:
                        self.count_ = entry[2]
                        found = True
                if found == False:
                    self.o2_.append([self.x_, self.y_, self.count_])
                print("count " + str(self.count_))

    def goReturn(self):
        global p
        for element in self.possible_movements_:
            if [self.x_, self.y_] == [element[0], element[1]]:
                # print("return")
                # self.draw()
                # print("possible_movements_ " + str(self.possible_movements_))
                # print("movements_ " + str(self.movements_))
                # print("positions_ " + str(self.positions_))
                self.possible_movements_ = self.possible_movements_[:-1]
                self.return_ = False
                return
        entry = self.movements_[-1]
        self.movements_ = self.movements_[:-1]
        x = entry[0]
        y = entry[1]
        dir = returnDir(entry[2])
        p.stdin.write(str(dir) + '\n')
        self.count_ += 1
        result = p.stdout.readline()
        self.x_ = x
        self.y_ = y
        print("dir <" + str(dir) + ">, result <" + str(result[:-1]) + ">, x<" + str(x) + ">, y<" + str(y) + ">")
        found = False

    def move(self):
        global p
        if self.return_ == True:
            self.goReturn()
            return
        entry = 0
        entry = self.possible_movements_[-1]
        self.possible_movements_ = self.possible_movements_[:-1]
        self.movements_.append(entry)
        x = entry[0]
        y = entry[1]
        dir = entry[2]
        p.stdin.write(str(dir) + '\n')
        self.count_ += 1
        result = p.stdout.readline()
        print("dir <" + str(dir) + ">, result <" + str(result[:-1]) + ">, x<" + str(x) + ">, y<" + str(y) + ">")
        if [self.x_, self.y_] not in self.positions_:
            self.positions_.append([self.x_, self.y_])
        if dir == 1:
            y -= 1
        elif dir == 2:
            y += 1
        elif dir == 3:
            x -= 1
        elif dir == 4:
            x += 1
        self.x_ = x
        self.y_ = y

    def saveStreet(self, dir):
        x = self.x_
        y = self.y_
        if dir == 1:
            y -= 1
        elif dir == 2:
            y += 1
        elif dir == 3:
            x -= 1
        elif dir == 4:
            x += 1
        if self.return_ == True:
            return 1
        if [x, y] not in self.positions_:
            self.possible_movements_.append([self.x_, self.y_, dir])
            return 1
        return 0

    def saveWall(self, dir, char):
        x = self.x_
        y = self.y_
        if dir == 1:
            y -= 1
        elif dir == 2:
            y += 1
        elif dir == 3:
            x -= 1
        elif dir == 4:
            x += 1
        if [x, y] not in self.walls_:
            self.walls_.append([x, y, char])

    def draw(self):
        for y in range(self.height_):
            row = []
            y -= self.height_/2
            for x in range(self.width_):
                x -= self.width_/2
                if x == droid.x_ and y == droid.y_:
                    row.append("D")
                elif [x,y] in self.positions_:
                    row.append(".")
                elif [x,y,'#'] in self.walls_:
                    row.append("#")
                elif [x,y,'*'] in self.walls_:
                    row.append("*")
                else:
                    row.append(" ")
            print(''.join(row))

def nextDir(dir):
    if dir == 1:
        return 4
    if dir == 2:
        return 3
    if dir == 3:
        return 1
    if dir == 4:
        return 2

def returnDir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    elif dir == 4:
        return 3

def move():
    global p
    global droid
    droid = Droid()
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    # go up
    dir = 1
    droid.draw()
    try:
        while True:
            droid.discover()
            droid.move()
    except:
        droid.o2_.sort(key=lambda x:x[2])
        print(droid.o2_)
        droid.draw()

def main():
    move()

if __name__ == "__main__":
    main()
