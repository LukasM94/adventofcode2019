#!/usr/bin/env python3

map = []
robot = []
pathList = []
list = []

class Point:
    def __init__(self, x, y, c):
        self.x_ = x
        self.y_ = y
        self.name_ = c
        self.opened_doors_ = []

    def validPoint(c):
        return ord(c) != ord('#') and ord(c) != ord('x')

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

def findAll():
    global map
    global lockList
    global doorList
    global robot
    x = 0
    y = 0
    for row in map:
        for c in row:
            if Robot.isRobot(c):
                robot = Robot(x, y)
            x += 1
        y += 1
        x = 0

def printMap():
    global map
    print("=================================")
    for row in map:
        print(''.join(row))
    print("=================================")

def readInput():
    global map
    file = open("input", "r")
    for line in file:
        row = []
        for c in line:
            row.append(c)
        map.append(row[:-1])

def search(x, y, count, point, doors):
    global map
    global pathList
    c = map[y][x]
    if Point.validPoint(c) == False:
        return None
    map[y][x] = 'x'
    # printMap()
    if Lock.isLock(c) == True:
        path = Path(point)
        path.addPoint2(Lock(x, y, c), count)
        path.doors_ = doors
        doors = []
        pathList.append(path)
        count = 0
        point = Lock(x, y, c)
    elif Door.isDoor(c) == True:
        doors.append(Door(x, y, c))
    search(x, y - 1, count + 1, point, doors)
    search(x + 1, y, count + 1, point, doors)
    search(x, y + 1, count + 1, point, doors)
    search(x - 1, y, count + 1, point, doors)

def getPathList():
    global map
    global robot
    search(robot.x_, robot.y_, 0, robot, [])
#
# def printPathList():
#     global pathList
#     for path in pathList:
#         print(path)
#
# def doPart1(point):
#     print(point)
#     for path in pathList:
#         if path.point1_ == point:
#             doors_left = []
#             # for door in path.point2_.opened_doors_:
#             #     print(door)
#             # for door in path.doors_:
#             #     print(door)
#             doors_left = list(filter(lambda x: x not in path.point2_.opened_doors_, path.doors_))
#             for door in doors_left:
#                 print(door)
#             if doors_left == []:
#                 door = Door(-1, -1, chr(path.point2_.name_ - 0x20))
#                 path.point2_.opened_doors_.append(door)
#                 # print(path)
#                 doPart1(path.point2_)

def doPart1(point):
    print(point)


def main():
    readInput()
    printMap()
    findAll()
    getPathList()
    # printPathList()
    # print("=================================")
    # doPart1(robot)
    # print("=================================")

if __name__ == "__main__":
    main()
