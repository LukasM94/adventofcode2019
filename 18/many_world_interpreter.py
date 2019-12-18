#!/usr/bin/env python3

map = []
robot = []
list_map = []
locks = {}
doors = {}
count_list = []
cache = {}
smallest = 100000

class Point:
    def __init__(self, x, y, c):
        self.x_ = x
        self.y_ = y
        self.name_ = c
        self.opened_doors_ = []

    def validPoint(c):
        return ord(c) != ord('#')

    def __eq__(self, other):
        return self.name_ == other.name_

class Crux(Point):
    def __init__(self, x, y, c):
        Point.__init__(self, x, y, c)

class Robot(Crux):
    def __init__(self, x, y):
        Crux.__init__(self, x, y, '@')

    def isRobot(c):
        return ord(c) == ord('@')

    def __str__(self):
        return "Robot x<" + str(self.x_) + ">, y<" + str(self.y_) + ">"

class Lock(Crux):
    def __init__(self, x, y, c):
        Crux.__init__(self, x, y, ord(c))

    def isLock(c):
        return ord(c) >= ord('a') and ord(c) <= ord('z')

    def __str__(self):
        return "Lock x<" + str(self.x_) + ">, y<" + str(self.y_) + ">, c<" + chr(self.name_) + ">"

class Door(Point):
    def __init__(self, x, y, c):
        Point.__init__(self, x, y, ord(c))

    def isDoor(c):
        return ord(c) >= ord('A') and ord(c) <= ord('Z')

    def __str__(self):
        return "Door x<" + str(self.x_) + ">, y<" + str(self.y_) + ">, c<" + chr(self.name_) + ">"

class Path:
    def __init__(self, point1):
        self.point1_ = point1
        self.doors_ = []

    def addPoint2(self, point2, count):
        self.point2_ = point2
        self.count_ = count

    def addDoor(self, door):
        self.doors_.append(door)

    def __str__(self):
        string = "point1 <" + str(self.point1_) + ">, point2 <" + str(self.point2_) + ">, count <" + str(self.count_) + ">\n"
        for door in self.doors_:
            string += "  door <" + str(door) + ">\n"
        return string[:-1]

def findRobot():
    global map
    global robot
    x = 0
    y = 0
    for row in map:
        for c in row:
            if Lock.isLock(c):
                print("lock <" + str(c) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
                locks[c] = [x,y]
            if Door.isDoor(c):
                print("door <" + str(c) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
                doors[c] = [x,y]
            if Robot.isRobot(c):
                robot = Robot(x, y)
                map[y][x] = '.'
            x += 1
        y += 1
        x = 0

def printMap(map):
    global robot
    print("=================================")
    y = 0
    for row in map:
        if y == robot.y_:
            temp = row.copy()
            temp[robot.x_] = "@"
            print(''.join(temp))
        else:
            print(''.join(row))
        y += 1
    print("=================================")

def readInput():
    global map
    file = open("input", "r")
    for line in file:
        row = []
        for c in line:
            row.append(c)
        map.append(row[:-1])
    file.close()

def recursive(map, mask, x, y, count, list, used_keys, open_doors):
    global doors
    # global cache
    global smallest
    c = map[y][x]

    if count > smallest:
        return

    # string = str(c) + ''.join(sorted(used_keys))
    # if string in cache:
    #     print("optimize")
    #     count = cache[string]
    #     return

    bit = mask[y][x]
    C = chr(ord(c) - 0x20)
    if bit == 1:
        return
    if c != '.':
        if c == '#':
            return
        # print("    char <" + str(c) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
        if c not in used_keys and c not in open_doors:
            # print("    used_keys <" + str(used_keys) + ">")
            # print("    open_doors <" + str(open_doors) + ">")
            # print("    C <" + str(C) + "> or c <" + str(c) + "> not in list")
            if Lock.isLock(c) == True:
                list.append([count, c])
                return
            else:
                return
    mask[y][x] = 1
    recursive(map, mask, x, y - 1, count + 1, list, used_keys, open_doors)
    recursive(map, mask, x + 1, y, count + 1, list, used_keys, open_doors)
    recursive(map, mask, x, y + 1, count + 1, list, used_keys, open_doors)
    recursive(map, mask, x - 1, y, count + 1, list, used_keys, open_doors)

def getMask(map):
    mask = []
    for line in map:
        row = [0] * len(line)
        mask.append(row)
    return mask

def doubleRec(map, count, c, used_keys, open_doors):
    global smallest
    global cache
    C = chr(ord(c) - 0x20)

    string = str(c) + ',' + ''.join(sorted(used_keys))
    # print(string + ", " + str(count))
    if string in cache:
        if cache[string] > count:
            # print("hit")
            cache[string] = count
        else:
            # print("get")
            count = cache[string]
            return
    else:
        # print("add")
        cache[string] = count


    used_keys = used_keys.copy()
    open_doors = open_doors.copy()
    used_keys.append(c)
    open_doors.append(C)

    list = []
    mask = getMask(map)
    [x, y] = locks[c]
    if len(used_keys) == len(locks) and count < smallest:
        smallest = count
    # else:
    #     print("fail:" + str(count))
    # print("char <" + str(c) + ">, count <" + str(count) + ">")
    # print("used_keys <" + str(used_keys) + ">")
    # print("open_doors <" + str(open_doors) + ">")

    recursive(map, mask, x, y, count, list, used_keys, open_doors)
    if count > smallest:
        return

    list = sorted(list, key=lambda x: x[0])
    list = sorted(list, key=lambda x: x[0])
    for entry in list:
        doubleRec(map, entry[0], entry[1], used_keys, open_doors)

def getMaps(map):
    global robot
    list = []
    mask = getMask(map)
    count = 0
    used_keys = []
    open_doors = []
    recursive(map, mask, robot.x_, robot.y_, count, list, used_keys, open_doors)
    # print(list)
    for entry in list:
        doubleRec(map, entry[0], entry[1], used_keys, open_doors)

def main():
    global map
    global smallest
    readInput()
    findRobot()
    printMap(map)
    getMaps(map)
    print(smallest)

if __name__ == "__main__":
    main()
