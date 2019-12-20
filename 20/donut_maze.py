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

def goOn(map, x, y):
    count = map[y - 1][x] == '.'
    count += map[y][x + 1] == '.'
    count += map[y + 1][x] == '.'
    count += map[y][x - 1] == '.'
    return count != 1

def getOtherCoordinates(portals, x, y):
    for entry in portals:
        if [x, y] == entry[0]:
            print(entry[1])
            return entry[1]
        elif [x, y] == entry[1]:
            print(entry[0])
            return entry[0]

point_number = 0
def getList(map, x, y, count, portals):
    global point_number

    while goOn(map, x, y) == False:
        map[y][x] = ','
        # printMap(map)
        y -= int(map[y - 1][x] == '.')
        x += int(map[y][x + 1] == '.')
        y += int(map[y + 1][x] == '.')
        x -= int(map[y][x - 1] == '.')

    list = []
    # print("x <" + str(x) + ">, y <" + str(y) + ">")
    # printMap(map)
    if map[y][x] == '~':
        map[y][x] = ','
        # print("portal for x <" + str(x) + ">, y <" + str(y) + ">")
        try:
            [x, y] = getOtherCoordinates(portals, x, y)
        except:
            return []
        count += 1
    elif map[y][x] != '.':
        return []
    map[y][x] = ','
    if isCrossOver(map, x, y):
        list.append([[x, y],[point_number, count]])
        point_number += 1
    temp = getList(map, x, y - 1, count + 1, portals)
    if temp != []:
        list += temp
    temp = getList(map, x + 1, y, count + 1, portals)
    if temp != []:
        list += temp
    temp = getList(map, x, y + 1, count + 1, portals)
    if temp != []:
        list += temp
    temp = getList(map, x - 1, y, count + 1, portals)
    if temp != []:
        list += temp
    return list

def getImportantPoints(map):
    y_aa = 0
    x_aa = 0
    found = False
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
                else:
                    y_portal = y - 1
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
