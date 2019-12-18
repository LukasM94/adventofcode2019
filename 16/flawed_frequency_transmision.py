#!/usr/bin/env python3

import math
import numpy

input = []
phases = 0
result = 0
offset = 0
matrix = []

def readInput():
    global input
    global phases
    global result
    global offset
    file = open("input", "r")
    phases = int(file.readline())
    temp = file.readline()
    try:
        result = int(file.readline())
    except:
        print("no result")
    file.close()
    for i in range(10000):
        for c in temp:
            if c != '\n':
                input.append(int(c))
    offset = int(temp[0:7])
    print(str(len(input)))
    print(str(offset))

def part1():
    global input
    global phases
    global result
    global offset
    frequencies = []
    next_coefitient = []
    for i in range(math.ceil(len(input) / 4)):
        next_coefitient.append(1)
        next_coefitient.append(0)
        next_coefitient.append(-1)
        next_coefitient.append(0)
    next_coefitient = next_coefitient[0:len(input)]
    frequencies.append(next_coefitient)
    j = 2
    while j <= len(input):
        next_coefitient = []
        for i in range(math.ceil(len(input))):
            next_coefitient.append(frequencies[0][int(i/j)])
        for i in range(j - 1):
            next_coefitient.insert(0, 0)
        next_coefitient = next_coefitient[0:len(input)]
        frequencies.append(next_coefitient)
        j += 1
    next = input
    temp = []
    for p in range(phases):
        temp = []
        for i in range(len(frequencies)):
            sum = 0
            for j in range(len(input)):
                sum += (int(next[j]) * frequencies[i][j])
            sum = abs(sum) % 10
            temp.append(str(sum))
        next = temp
    print(''.join(temp[0:7]))
    print(result)

def part2():
    global input
    global offset
    global result
    global phases
    output = input[offset:]
    print(output[:8])
    output.reverse()
    print(output[:8])
    for i in range(phases):
        output = numpy.cumsum(output) % 10
        # print(output[:8])
    output = list(map(lambda x: str(x), output))
    output.reverse()
    print(''.join(output[:8]))
    print(result)

def main():
    readInput()
    # part1()
    part2()

if __name__ == '__main__':
    main()
