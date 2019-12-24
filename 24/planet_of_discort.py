#!/usr/bin/env python3

def readInput():
    map = []
    file = open("input", "r")
    for line in file:
        map.append(list(line[:-1]))
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

def doStep(map):
    global counter
    counter += 1
    next_map = []
    for line in map:
        next_line = line.copy()
        next_map.append(next_line)
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
        # print("===================")
        # print("after " + str(counter) + " minutes")
        # printMap(map)
        value = getValue(map)
        if value not in list:
            list.append(value)
        else:
            print("===================")
            print("after " + str(counter) + " minutes")
            printMap(map)
            print("value is " + str(value))
            break

def main():
    map = readInput()
    doPart1(map)

if __name__ == "__main__":
    main()
