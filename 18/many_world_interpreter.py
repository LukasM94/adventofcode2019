#!/usr/bin/env python3

map = []
robot = []
robots = []
list_map = []
locks = {}
doors = {}
count_list = []
cache = {}
smallest = 100000

class Robot():
    def __init__(self, x, y, count):
        self.x_ = x
        self.y_ = y
        self.count_ = count

    def isRobot(c):
        return ord(c) == ord('@')

    def __str__(self):
        return "Robot" + str(self.count_) + " x<" + str(self.x_) + ">, y<" + str(self.y_) + ">"

def isDoor(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def isLock(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def findAll():
    global map
    global robots
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
                robots.append(Robot(x, y, robot_count))
                robot_count += 1
                map[y][x] = '.'
            x += 1
        y += 1
        x = 0

def printMap(map):
    global robots
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









def doubleRec2(map, count, c, used_keys, open_doors, robot):
    global smallest
    global cache
    global robots
    C = chr(ord(c) - 0x20)
    local_robot0 = Robot(robots[0].x_, robots[0].y_, robots[0].count_)
    local_robot1 = Robot(robots[1].x_, robots[1].y_, robots[1].count_)
    local_robot2 = Robot(robots[2].x_, robots[2].y_, robots[2].count_)
    local_robot3 = Robot(robots[3].x_, robots[3].y_, robots[3].count_)

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
    next_list = []
    mask = getMask(map)
    print(''.join(used_keys))
    # print(robot == robots[0])
    # print(robot == robots[1])
    # print(robot == robots[2])
    # print(robot == robots[3])
    printMap(map)
    [robot.x_, robot.y_] = locks[c]
    if len(used_keys) == len(locks) and count < smallest:
        smallest = count
    # print("char <" + str(c) + ">, count <" + str(count) + ">")
    # print("used_keys <" + str(used_keys) + ">")
    # print("open_doors <" + str(open_doors) + ">")

    # print("=================start======================")
    # print("============================================")
    # print(robots[0])
    list = []
    old_used_keys = used_keys.copy()
    old_open_doors = open_doors.copy()
    recursive2(map, mask, robots[0], count, list, old_used_keys, old_open_doors)
    next_list.extend(list)
    # print(robots[0])
    # print("============================================")
    # print(robots[1])
    list = []
    old_used_keys = used_keys.copy()
    old_open_doors = open_doors.copy()
    recursive2(map, mask, robots[1], count, list, old_used_keys, old_open_doors)
    next_list.extend(list)
    # print(robots[1])
    # print("============================================")
    # print(robots[2])
    list = []
    old_used_keys = used_keys.copy()
    old_open_doors = open_doors.copy()
    recursive2(map, mask, robots[2], count, list, old_used_keys, old_open_doors)
    next_list.extend(list)
    # print(robots[2])
    # print("============================================")
    # print(robots[3])
    list = []
    old_used_keys = used_keys.copy()
    old_open_doors = open_doors.copy()
    recursive2(map, mask, robots[3], count, list, old_used_keys, old_open_doors)
    next_list.extend(list)
    # print(robots[3])
    # print("============================================")

    if count > smallest:
        return

    next_list = sorted(next_list, key=lambda x: x[0])
    for entry in next_list:
        doubleRec2(map, entry[0], entry[1], entry[3], entry[4], entry[2])
    robots[0] = local_robot0
    robots[1] = local_robot1
    robots[2] = local_robot2
    robots[3] = local_robot3

    # print("===================end======================")

def recursive2(map, mask, robot, count, list, used_keys, open_doors):
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
        # print("  char <" + str(c) + ">, x <" + str(robot.x_) + ">, y <" + str(robot.y_) + ">")
        if c not in used_keys and c not in open_doors:
            # print("    used_keys <" + str(used_keys) + ">")
            # print("    open_doors <" + str(open_doors) + ">")
            # print("    Char <" + str(C) + "> or char <" + str(c) + "> not in list")
            if isLock(c) == True:
                # print("      True")
                list.append([count, c, robot, used_keys, open_doors])
                return
            else:
                return
    mask[robot.y_][robot.x_] = 1
    robot.y_ -= 1
    recursive2(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.y_ += 1
    robot.x_ += 1
    recursive2(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.x_ -= 1
    robot.y_ += 1
    recursive2(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.y_ -= 1
    robot.x_ -= 1
    recursive2(map, mask, robot, count + 1, list, used_keys, open_doors)
    robot.x_ += 1

def doPart2(map):
    global robots
    next_list = []
    mask = getMask(map)
    count = 0
    local_robot0 = Robot(robots[0].x_, robots[0].y_, robots[0].count_)
    local_robot1 = Robot(robots[1].x_, robots[1].y_, robots[1].count_)
    local_robot2 = Robot(robots[2].x_, robots[2].y_, robots[2].count_)
    local_robot3 = Robot(robots[3].x_, robots[3].y_, robots[3].count_)

    # print("=================start======================")
    # print("============================================")
    # print(robots[0])
    list = []
    used_keys = []
    open_doors = []
    recursive2(map, mask, robots[0], count, list, used_keys, open_doors)
    next_list.extend(list)
    # print(robots[0])
    # print("============================================")
    # print(robots[1])
    list = []
    used_keys = []
    open_doors = []
    recursive2(map, mask, robots[1], count, list, used_keys, open_doors)
    next_list.extend(list)
    # print(robots[1])
    # print("============================================")
    # print(robots[2])
    list = []
    used_keys = []
    open_doors = []
    recursive2(map, mask, robots[2], count, list, used_keys, open_doors)
    next_list.extend(list)
    # print(robots[2])
    # print("============================================")
    # print(robots[3])
    list = []
    used_keys = []
    open_doors = []
    recursive2(map, mask, robots[3], count, list, used_keys, open_doors)
    next_list.extend(list)
    # print(robots[3])
    # print("============================================")

    if count > smallest:
        return

    next_list = sorted(next_list, key=lambda x: x[0])
    for entry in next_list:
        doubleRec2(map, entry[0], entry[1], entry[3], entry[4], entry[2])
    robots[0] = local_robot0
    robots[1] = local_robot1
    robots[2] = local_robot2
    robots[3] = local_robot3

def main():
    global map
    global smallest
    readInput()
    findAll()
    printMap(map)
    # doPart1(map)
    doPart2(map)
    print(smallest)

if __name__ == "__main__":
    main()
