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

def isPortal(map, x, y):
    return map[y][x] == '~'

def goThroughPortal(map, portals, x, y):
    for entry in portals:
        if [x, y] == entry[0][0:2]:
            print(entry[1])
            return entry[1]
        elif [x, y] == entry[1][0:2]:
            print(entry[0])
            return entry[0]
    return []

def copyMap(map):
    m = []
    for line in map:
        s = []
        for c in line:
            s.append(c)
        m.append(s)
    return m

def getList(map, x, y, count, portals):
    stack = []
    stack.append([x, y, count, 0])
    map[y][x] = '*'
    turns = 0
    level = 0
    # default_map = copyMap(map)
    maps = []
    for i in range(500):
        maps.append(copyMap(map))
    while len(stack) != 0:
        [x, y, count, level] = stack.pop(0)
        map = maps[level]
        # print("x <" + str(x) + ">, y <" + str(y) + ">")

        if map[y][x] == '~':
            count += 1
            map[y][x] = 'u'
        elif getValue(map, x, y - 1):
            count += 1
            y -= 1
        elif getValue(map, x + 1, y):
            count += 1
            x += 1
        elif getValue(map, x, y + 1):
            count += 1
            y += 1
        elif getValue(map, x - 1, y):
            count += 1
            x -= 1
        # print("count <" + str(count) + ">, level <" + str(level) + ">")
        # old = map[y][x]
        # map[y][x] = 'x'
        # printMap(map)
        # map[y][x] = old

        if isPortal(map, x, y):
            map[y][x] = 'i'
            next = goThroughPortal(map, portals, x, y)
            if next == []:
                if level != 0:
                    continue
                for portal in portals:
                    print(portal)
                printMap(map)
                print(count)
                exit()
            else:
                [x, y, lvl] = next
                level += lvl
            if level >= 0:
                stack.append([x, y, count, level])
        else:
            map[y][x] = '*'
            turns = getTurns(map, x, y)
            while turns > 0:
                stack.append([x, y, count, level])
                turns -= 1

    return []

def getImportantPoints(map):
    y_aa = 0
    x_aa = 0
    found = False
    nodes = []

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
                else:
                    x_portal = x - 1
                # print("portal at x <" + str(x_portal) + ">, y <" + str(y_portal) + ">")
                name = ''.join(sorted(first + second))
                map[y_portal][x_portal] = '~'
                # print(name)
                # printMap(map)
                t = []
                if x_portal == 2 or x_portal == len(map[0]) - 4 or y_portal == 2 or y_portal == len(map) - 4:
                    t = [x_portal, y_portal, 1]
                else:
                    t = [x_portal, y_portal, -1]
                if name not in temp_portals:
                    temp_portals[name] = t
                else:
                    list = []
                    list.append(temp_portals[name])
                    list.append(t)
                    list.append(name)
                    portals.append(list)
            second = map[y + 1][x]
            if isUpperLetter(first) and isUpperLetter(second):
                x_portal = x
                y_portal = -1
                if y == 0 or map[y + 2][x] == '.':
                    y_portal = y + 2
                else:
                    y_portal = y - 1
                # print("portal at x <" + str(x_portal) + ">, y <" + str(y_portal) + ">")
                name = ''.join(sorted(first + second))
                map[y_portal][x_portal] = '~'
                # print(name)
                # printMap(map)
                t = []
                if x_portal == 2 or x_portal == len(map) - 4 or y_portal == 2 or y_portal == len(map) - 4:
                    t = [x_portal, y_portal, 1]
                else:
                    t = [x_portal, y_portal, -1]
                if name not in temp_portals:
                    temp_portals[name] = t
                else:
                    list = []
                    list.append(temp_portals[name])
                    list.append(t)
                    list.append(name)
                    portals.append(list)
    [x_aa, y_aa, _ ] = temp_portals['AA']
    map[y_aa][x_aa] = '.'
    [x_zz, y_zz, _ ] = temp_portals['ZZ']

    printMap(map)
    print("start at x <" + str(x_aa) + ">, y <" + str(y_aa) + ">")
    for entry in portals:
        print(entry)
    return getList(map, x_aa, y_aa, 0, portals)

def main():
    map = readMap()
    printMap(map)
    list = getImportantPoints(map)
    printMap(map)
    print(list)

if __name__ == "__main__":
    main()
