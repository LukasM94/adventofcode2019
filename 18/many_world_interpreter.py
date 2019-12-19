#!/usr/bin/env python3

map = []
robot = []
# robots = []
list_map = []
locks = {}
doors = {}
count_list = []
cache = {}
smallest = 100000

class Robot():
    def __init__(self, x, y, count, name):
        self.x_ = x
        self.y_ = y
        self.count_ = count
        self.name_ = name

    def isRobot(c):
        return ord(c) == ord('@')

    def __str__(self):
        return "Robot" + str(self.name_) + " x<" + str(self.x_) + ">, y<" + str(self.y_) + ">, count <" + str(self.count_) + ">"

    def copy(self):
        return Robot(self.x_, self.y_, self.count_, self.name_)

def isDoor(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def isLock(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def findAll():
    global map
    robots = []
    x = 0
    y = 0
    robot_count = 0
    for row in map:
        for c in row:
            if isLock(c):
                print("lock <" + str(c) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
                locks[c] = [x,y]
            if isDoor(c):
                print("door <" + str(c) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
                doors[c] = [x,y]
            if Robot.isRobot(c):
                # robot = Robot(x, y)
                print("robot" + str(len(robots)) + " <" + str(c) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
                robots.append(Robot(x, y, 0, robot_count))
                robot_count += 1
                map[y][x] = '.'
            x += 1
        y += 1
        x = 0
    return robots

def printMap(map, robots):
    print("=================================")
    y = 0
    old_value = []
    for robot in robots:
        old_value.append(map[robot.y_][robot.x_])
        map[robot.y_][robot.x_] = '@'
    for row in map:
        print(''.join(row))
        y += 1
    for robot in robots:
        map[robot.y_][robot.x_] = old_value[0]
        old_value = old_value[1:]
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

def recursive(map, mask, robot, count, list, used_keys, open_doors):
    global doors
    # global cache
    global smallest
    c = map[robot.y_][robot.x_]

    if count > smallest:
        return

    bit = mask[robot.y_][robot.x_]
    C = chr(ord(c) - 0x20)
    if bit == 1:
        return
    if c != '.':
        if c == '#':
            return
        print("  char <" + str(c) + ">, x <" + str(robot.x_) + ">, y <" + str(robot.y_) + ">")
        if c not in used_keys and c not in open_doors:
            print("    used_keys <" + str(used_keys) + ">")
            print("    open_doors <" + str(open_doors) + ">")
            print("    C <" + str(C) + "> or c <" + str(c) + "> not in list")
            if isLock(c) == True:
                list.append([count, c])
                return
            else:
                return
    mask[robot.y_][robot.x_] = 1
    robot.y_ -= 1
    recursive(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.y_ += 1
    robot.x_ += 1
    recursive(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.x_ -= 1
    robot.y_ += 1
    recursive(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.y_ -= 1
    robot.x_ -= 1
    recursive(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.x_ += 1

def getMask(map):
    mask = []
    for line in map:
        row = [0] * len(line)
        mask.append(row)
    return mask

def doubleRec(map, count, c, used_keys, open_doors, robot):
    global smallest
    global cache
    C = chr(ord(c) - 0x20)

    string = str(c) + ',' + ''.join(sorted(used_keys))
    if string in cache:
        if cache[string] > count:
            cache[string] = count
        else:
            count = cache[string]
            return
    else:
        cache[string] = count

    used_keys = used_keys.copy()
    open_doors = open_doors.copy()
    used_keys.append(c)
    open_doors.append(C)

    list = []
    mask = getMask(map)
    [robot.x_, robot.y_] = locks[c]
    if len(used_keys) == len(locks) and count < smallest:
        smallest = count
    # print("char <" + str(c) + ">, count <" + str(count) + ">")
    # print("used_keys <" + str(used_keys) + ">")
    # print("open_doors <" + str(open_doors) + ">")

    recursive(map, mask, robot, count, list, used_keys, open_doors)
    if count > smallest:
        return

    list = sorted(list, key=lambda x: x[0])
    for entry in list:
        doubleRec(map, entry[0], entry[1], used_keys, open_doors, robot)

def doPart1(map):
    global robot
    list = []
    mask = getMask(map)
    count = 0
    used_keys = []
    open_doors = []

    recursive(map, mask, robot, count, list, used_keys, open_doors)
    # print(list)
    for entry in list:
        doubleRec(map, entry[0], entry[1], used_keys, open_doors, robot)









def doubleRec2(map, c, used_keys, open_doors, robots, robot_number):
    global smallest
    global cache
    robot = robots[robot_number]
    C = chr(ord(c) - 0x20)

    string = str(c) + ',' + str(robot_number) + ',' + ''.join(sorted(used_keys))
    # print("cache[string] > robots[robot_number].count_")
    if string in cache:
        # print(str(cache[string]) + " >= " + str(robots[robot_number].count_))
        if cache[string] >= robot.count_:
            # print("adjusted")
            cache[string] = robot.count_
        else:
            # print("optimized")
            robot.count_ = cache[string]
            print(string)
            return
    else:
        # print("set")
        cache[string] = robot.count_

    used_keys = used_keys.copy()
    open_doors = open_doors.copy()
    used_keys.append(c)
    open_doors.append(C)

    robots0 = []
    robots1 = []
    robots2 = []
    robots3 = []
    for r in robots:
        robots0.append(r.copy())
        robots1.append(r.copy())
        robots2.append(r.copy())
        robots3.append(r.copy())

    count = robots[0].count_
    count += robots[1].count_
    count += robots[2].count_
    count += robots[3].count_

    if len(used_keys) == len(locks) and count < smallest:
        smallest = count
        print("total count is " + str(count))

    if count > smallest:
        # print("too large")
        return

    list = []
    next_list = []
    mask = getMask(map)
    [robot.x_, robot.y_] = locks[c]
    if __debug__: printMap(map, robots)
    if __debug__: print(''.join(used_keys))
    if __debug__: print(robot)

    if __debug__: print("char <" + str(c) + ">, count <" + str(count) + ">")
    if __debug__: print("used_keys <" + str(used_keys) + ">")
    if __debug__: print("open_doors <" + str(open_doors) + ">")

    if __debug__: print("=================start======================")
    if __debug__: print("============================================")
    if __debug__: print(robots0[0])
    list = []
    recursive2(map, mask, robots0, 0, list, used_keys, open_doors)
    next_list.extend(list)

    if __debug__: print(robots0[0])
    if __debug__: print("============================================")
    if __debug__: print(robots1[1])
    list = []
    recursive2(map, mask, robots1, 1, list, used_keys, open_doors)
    next_list.extend(list)

    if __debug__: print(robots1[1])
    if __debug__: print("============================================")
    if __debug__: print(robots2[2])
    list = []
    recursive2(map, mask, robots2, 2, list, used_keys, open_doors)
    next_list.extend(list)

    if __debug__: print(robots2[2])
    if __debug__: print("============================================")
    if __debug__: print(robots3[3])
    list = []
    recursive2(map, mask, robots3, 3, list, used_keys, open_doors)
    next_list.extend(list)

    if __debug__: print(robots3[3])
    if __debug__: print("============================================")

    if __debug__:
        for r in robots:
            print(r)
    # for r in robots0:
    #     print(r)
    # for r in robots1:
    #     print(r)
    # for r in robots2:
    #     print(r)
    # for r in robots3:
    #     print(r)
    next_list = sorted(next_list, key=lambda x: x[0])
    for entry in next_list:
        entry[2][entry[3]].count_ = entry[0]
        doubleRec2(map, entry[1], used_keys, open_doors, entry[2], entry[3])

    if __debug__: print("===================end======================")

def recursive2(map, mask, robots, robot_number, list, used_keys, open_doors):
    global smallest
    robot = robots[robot_number]
    c = map[robot.y_][robot.x_]

    count = robots[0].count_
    count += robots[1].count_
    count += robots[2].count_
    count += robots[3].count_
    # print("count > smallest")
    # print(str(count) + " > " + str(smallest))
    if count > smallest:
        # print("too large")
        return

    bit = mask[robot.y_][robot.x_]
    C = chr(ord(c) - 0x20)
    if bit == 1:
        return
    if c != '.':
        if c == '#':
            return
        if __debug__: print("  char <" + str(c) + ">, x <" + str(robot.x_) + ">, y <" + str(robot.y_) + ">")
        if c not in used_keys and c not in open_doors:
            if __debug__: print("    used_keys <" + str(used_keys) + ">")
            if __debug__: print("    open_doors <" + str(open_doors) + ">")
            if isLock(c) == True:
                if __debug__: print("      True")
                if __debug__: print("      " + str(robot))
                next_robots = []
                for r in robots:
                    next_robots.append(r.copy())
                list.append([robot.count_, c, next_robots, robot_number])
                return
            else:
                return
    mask[robot.y_][robot.x_] = 1
    robot.y_ -= 1
    robot.count_ += 1
    recursive2(map, mask, robots, robot_number, list, used_keys, open_doors)
    robot.count_ -= 1
    robot.y_ += 1
    robot.x_ += 1
    robot.count_ += 1
    recursive2(map, mask, robots, robot_number, list, used_keys, open_doors)
    robot.count_ -= 1
    robot.x_ -= 1
    robot.y_ += 1
    robot.count_ += 1
    recursive2(map, mask, robots, robot_number, list, used_keys, open_doors)
    robot.count_ -= 1
    robot.y_ -= 1
    robot.x_ -= 1
    robot.count_ += 1
    recursive2(map, mask, robots, robot_number, list, used_keys, open_doors)
    robot.count_ -= 1
    robot.x_ += 1
    return

def doPart2(map, robots):
    next_list = []
    used_keys = []
    open_doors = []
    mask = getMask(map)

    robots0 = []
    robots1 = []
    robots2 = []
    robots3 = []
    for r in robots:
        robots0.append(r.copy())
        robots1.append(r.copy())
        robots2.append(r.copy())
        robots3.append(r.copy())

    count = robots[0].count_
    count += robots[1].count_
    count += robots[2].count_
    count += robots[3].count_
    if count > smallest:
        # print("too large")
        return

    if __debug__: print("===================Init=====================")
    if __debug__: print(robots0[0])
    list = []
    recursive2(map, mask, robots0, 0, list, used_keys, open_doors)
    next_list.extend(list)
    if __debug__: print(robots0[0])
    if __debug__: print("============================================")
    if __debug__: print(robots1[1])
    list = []
    recursive2(map, mask, robots1, 1, list, used_keys, open_doors)
    next_list.extend(list)
    if __debug__: print(robots1[2])
    if __debug__: print("============================================")
    if __debug__: print(robots2[2])
    list = []
    recursive2(map, mask, robots2, 2, list, used_keys, open_doors)
    next_list.extend(list)
    if __debug__: print(robots2[2])
    if __debug__: print("============================================")
    if __debug__: print(robots3[3])
    list = []
    recursive2(map, mask, robots3, 3, list, used_keys, open_doors)
    next_list.extend(list)
    if __debug__: print(robots3[3])
    if __debug__: print("===================End======================")

    if __debug__:
        for r in robots:
            print(r)
    # for r in robots0:
    #     print(r)
    # for r in robots1:
    #     print(r)
    # for r in robots2:
    #     print(r)
    # for r in robots3:
    #     print(r)
    next_list = sorted(next_list, key=lambda x: x[0])
    for entry in next_list:
        entry[2][entry[3]].count_ = entry[0]
        doubleRec2(map, entry[1], used_keys, open_doors, entry[2], entry[3])

def main():
    global map
    global smallest
    readInput()
    robots = findAll()
    printMap(map, robots)
    # doPart1(map)
    doPart2(map, robots)
    print(smallest)

if __name__ == "__main__":
    main()
