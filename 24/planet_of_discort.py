#!/usr/bin/env python3

def readInput():
    map = []
    file = open("input", "r")
    for line in file:
        map.append(list(line[:-1]))
    map[2][2] = '?'
    return map

counter = 0

def printMap(map):
    print
    for line in map:
        print(''.join(line))

def countNeighbour(map, x, y):
    count = 0
    count += int((y - 1) >= 0 and map[y - 1][x] == '#')
    count += int((x + 1) < 5 and map[y][x + 1] == '#')
    count += int((y + 1) < 5 and map[y + 1][x] == '#')
    count += int((x - 1) >= 0 and map[y][x - 1] == '#')
    return count

def copyMap(map):
    copy_map = []
    for line in map:
        copy_line = line.copy()
        copy_map.append(copy_line)
    return copy_map

def doStep(map):
    global counter
    counter += 1
    next_map = copyMap(map)
    for y in range(len(map)):
        for x in range(len(map[0])):
            count = countNeighbour(map, x, y)
            # print("x <" + str(x) + ">, y <" + str(y) + ">, count <" + str(count) + ">")
            if map[y][x] == '#' and count != 1:
                next_map[y][x] = '.'
            elif map[y][x] == '.' and (count == 1 or count == 2):
                next_map[y][x] = '#'
    return next_map

def getValue(map):
    value = 1
    result = 0
    for line in map:
        for c in line:
            if c == '#':
                result += value
            value *= 2
    return result

def doPart1(map):
    global counter
    list = []
    print("===================")
    print("init")
    printMap(map)
    while True:
        map = doStep(map)
        print("===================")
        print("after " + str(counter) + " minutes")
        printMap(map)
        value = getValue(map)
        if value not in list:
            list.append(value)
        else:
            print("===================")
            print("after " + str(counter) + " minutes")
            printMap(map)
            print("value is " + str(value))
            break

def getZeroMap(map):
    zero_map = []
    for y in range(len(map)):
        zero_map.append(list(len(map) * '.'))
    zero_map[2][2] = '?'
    return zero_map

def changeBugs(maps, i):
    map = maps[i][1]
    next_map = copyMap(map)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if x == 2 and y == 2:
                continue
            count = 0
            if i != 0:
                neighbour_map = maps[i - 1][1]
                if y == 0:
                    count += int(neighbour_map[1][2] == "#")
                elif y == len(map) - 1:
                    count += int(neighbour_map[3][2] == "#")
                if x == 0:
                    count += int(neighbour_map[2][1] == "#")
                elif x == len(map[0]) - 1:
                    count += int(neighbour_map[2][3] == "#")
            if i != len(maps) - 1:
                neighbour_map = maps[i + 1][1]
                if x == 2 and y == 1:
                    count += int(neighbour_map[0][0] == "#")
                    count += int(neighbour_map[0][1] == "#")
                    count += int(neighbour_map[0][2] == "#")
                    count += int(neighbour_map[0][3] == "#")
                    count += int(neighbour_map[0][4] == "#")
                elif x == 2 and y == 3:
                    count += int(neighbour_map[4][0] == "#")
                    count += int(neighbour_map[4][1] == "#")
                    count += int(neighbour_map[4][2] == "#")
                    count += int(neighbour_map[4][3] == "#")
                    count += int(neighbour_map[4][4] == "#")
                if y == 2 and x == 1:
                    count += int(neighbour_map[0][0] == "#")
                    count += int(neighbour_map[1][0] == "#")
                    count += int(neighbour_map[2][0] == "#")
                    count += int(neighbour_map[3][0] == "#")
                    count += int(neighbour_map[4][0] == "#")
                elif y == 2 and x == 3:
                    count += int(neighbour_map[0][4] == "#")
                    count += int(neighbour_map[1][4] == "#")
                    count += int(neighbour_map[2][4] == "#")
                    count += int(neighbour_map[3][4] == "#")
                    count += int(neighbour_map[4][4] == "#")
            count += countNeighbour(map, x, y)
            # print("i <" + str(i) + ">, depth <" + str(maps[i][0]) + ">, x <" + str(x) + ">, y <" + str(y) + ">, count <" + str(count) + ">")
            if map[y][x] == '#' and count != 1:
                next_map[y][x] = '.'
            elif map[y][x] == '.' and (count == 1 or count == 2):
                next_map[y][x] = '#'
    # printMap(map)
    # print("===========")
    # printMap(next_map)
    return next_map

def doStep2(maps):
    global counter
    if counter % 2 == 1:
        depth = (len(maps) + 1) / 2
        maps.append([int(depth), getZeroMap(maps[0][1])])
        depth *= -1
        maps.append([int(depth), getZeroMap(maps[0][1])])
        maps = sorted(maps, key=lambda x: x[0], reverse=False)
    next_maps = []
    for i in range(len(maps)):
        next_maps.append([maps[i][0], changeBugs(maps, i)])
    return next_maps
    # for i in range(len(maps)):
    #     maps[i][1] = changeBugs(maps, i)
    # return maps

def printMaps(maps):
    maps = sorted(maps, key=lambda x: x[0], reverse=False)
    for entry in maps:
        print("Depth " + str(entry[0]))
        printMap(entry[1])

def doPart2(map):
    global counter
    maps = []
    copy_map = copyMap(map)
    maps.append([0, copy_map])
    print("===================")
    print("init")
    printMap(map)
    counter += 1
    for i in range(200):
        maps = doStep2(maps)
        # print("===================")
        # print("after " + str(counter) + " minutes")
        # printMaps(maps)
        counter += 1
    # printMaps(maps)
    print("count of bugs is " + str(countBugs(maps)))

def countBugs(maps):
    count = 0
    for map in maps:
        for line in map[1]:
            for c in line:
                if c == '#':
                    count += 1
    return count

def main():
    map = readInput()
    # doPart1(map)
    doPart2(map)

if __name__ == "__main__":
    main()
