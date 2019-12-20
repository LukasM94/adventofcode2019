#!/usr/bin/env python3

def readMap():
    file = open("input", "r")
    map = []
    max_width = 0
    for line in file:
        row = []
        temp = 0
        for c in line:
            if c != '\n':
                temp += 1
                row.append(c)
        map.append(row)
        if temp > max_width:
            max_width = temp
    for line in map:
        while len(line) < (max_width + 1):
            line.append(' ')
    empty_line = ' ' * (max_width + 1)
    map.append(empty_line)
    return map

def printMap(map):
    for line in map:
        print(''.join(line))

def isUpperLetter(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def isCrossOver(map, x, y):
    count = map[y - 1][x] == '.'
    count += map[y][x + 1] == '.'
    count += map[y + 1][x] == '.'
    count += map[y][x - 1] == '.'
    return count > 1

def getTurns(map, x, y):
    count = int(getValue(map, x, y - 1))
    count += int(getValue(map, x + 1, y))
    count += int(getValue(map, x, y + 1))
    count += int(getValue(map, x - 1, y))
    return count

def getValue(map, x, y):
    return map[y][x] == '.' or map[y][x] == '~'

def getOtherCoordinates(portals, x, y):
    for entry in portals:
        if [x, y] == entry[0]:
            print(entry[1])
            return entry[1]
        elif [x, y] == entry[1]:
            print(entry[0])
            return entry[0]

# class Node:
#     count = 0
#     def __init__(self, x, y):
#         self.x_ = x
#         self.y_ = y
#         self.number_ = Node.count
#         Node.count += 1
#         self.north_ = 0
#         self.east_ = 0
#         self.south_ = 0
#         self.west_ = 0
#
#     def __init__(self, x, y, n, e, s, w):
#         self.x_ = x
#         self.y_ = y
#         self.number_ = Node.count
#         Node.count += 1
#         self.north_ = n
#         self.east_ = e
#         self.south_ = s
#         self.west_ = w
#
#     def __str__(self):
#         return "node <" + str(self.number_) + ">, x <" + str(self.x_) + ">, y <" + str(self.y_) + ">, n <" + str(self.north_) + ">, e <" + str(self.east_) + ">, s <" + str(self.south_) + ">, w <" + str(self.west_) + ">"
#
# class Path:
#     def __init__(self, node1, node2, distance):
#         self.node1_ = node1
#         self.node2_ = node2
#         self.distance_ = distance

def getList(map, x, y, count, portals):
    stack = []
    stack.append([x, y, count])
    turns = 0
    while len(stack) != 0:
        [x, y, _] = stack.pop(0)
        if getValue(map, x, y - 1):
            y -= 1
        elif getValue(map, x + 1, y):
            x += 1
        elif getValue(map, x, y + 1):
            y += 1
        elif getValue(map, x - 1, y):
            x -= 1
        map[y][x] = '*'
        printMap(map)
        turns = getTurns(map, x, y)
        while turns > 0:
            print("append x <" + str(x) + ">, y <" + str(y) + ">, turns <" + str(turns) + ">")
            stack.append([x, y, count])
            turns -= 1

    return []

def getImportantPoints(map):
    y_aa = 0
    x_aa = 0
    found = False
    nodes = []
    for x in range(len(map[0])):
        if map[0][x] == 'A' and map[1][x] == 'A':
            x_aa = x
            y_aa = 2
            found = True
            map[0][x] = ' '
            map[1][x] = ' '
    if found == False:
        for y in range(len(map)):
            if map[y][0] == 'A' and map[y][1] == 'A':
                x_aa = 2
                y_aa = y
                map[y][0] = ' '
                map[y][1] = ' '

    # nodes.append(Node(x_aa, y_aa, 0, 0, 1, 0))

    portals = []
    temp_portals = {}

    for y in range(len(map) - 2):
        for x in range(len(map[0]) - 2):
            first = map[y][x]
            second = map[y][x + 1]
            if isUpperLetter(first) and isUpperLetter(second):
                x_portal = -1
                y_portal = y
                if x == 0 or map[y][x + 2] == '.':
                    x_portal = x + 2
                    # nodes.append(Node(x_portal, y_portal, 0, 0, 1, 0))
                else:
                    x_portal = x - 1
                    # nodes.append(Node(x_portal, y_portal, 1, 0, 0, 0))
                map[y_portal][x_portal] = '~'
                name = ''.join(sorted(first + second))
                if name not in temp_portals:
                    temp_portals[name] = [x_portal, y_portal]
                else:
                    coordinates = str(1000 * x + y)
                    list = []
                    list.append(temp_portals[name])
                    list.append([x_portal, y_portal])
                    list.append(name)
                    portals.append(list)
            second = map[y + 1][x]
            if isUpperLetter(first) and isUpperLetter(second):
                x_portal = x
                y_portal = -1
                if y == 0 or map[y + 2][x] == '.':
                    y_portal = y + 2
                    # nodes.append(Node(x_portal, y_portal, 0, 1, 0, 0))
                else:
                    y_portal = y - 1
                    # nodes.append(Node(x_portal, y_portal, 0, 0, 0, 1))
                map[y_portal][x_portal] = '~'
                name = ''.join(sorted(first + second))
                if name not in temp_portals:
                    temp_portals[name] = [x_portal, y_portal]
                else:
                    coordinates = str(1000 * x + y)
                    list = []
                    list.append(temp_portals[name])
                    list.append([x_portal, y_portal])
                    list.append(name)
                    portals.append(list)

    # for node in nodes:
    #     print(node)
    print(portals)
    return getList(map, x_aa, y_aa, 0, portals)

def main():
    map = readMap()
    printMap(map)
    list = getImportantPoints(map)
    printMap(map)
    print(list)

if __name__ == "__main__":
    main()
