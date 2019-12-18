#!/usr/bin/env python3
import math

orbits = []
num_of_orbits = []
path_san = []
path_you = []

def rec(i):
    global orbits
    global num_of_orbits
    if num_of_orbits[i] != -1:
        return num_of_orbits[i]
    sum = 1
    entry = orbits[i]
    first = entry[0]
    second = entry[1]
    for j in range(len(orbits)):
        subentry = orbits[j]
        if second == subentry[0]:
            sum += rec(j)
    num_of_orbits[i] = sum
    return sum

def getNextOrbits():
    global orbits;
    sum = 0
    sum += rec(j)
    # for j in range(len(orbits)):
    return sum

def getFindYou(i):
    global orbits
    global path_you
    entry = orbits[i]
    first = entry[0]
    second = entry[1]
    path_you.append(entry)
    # print(entry)
    if second == "YOU":
        return True
    for j in range(len(orbits)):
        subentry = orbits[j]
        if second == subentry[0]:
            if getFindYou(j) == True:
                return True
    path_you.pop()
    return False

def getFindSanta(i):
    global orbits
    global path_san
    entry = orbits[i]
    first = entry[0]
    second = entry[1]
    path_san.append(entry)
    # print(entry)
    if second == "SAN":
        return True
    for j in range(len(orbits)):
        subentry = orbits[j]
        if second == subentry[0]:
            if getFindSanta(j) == True:
                return True
    path_san.pop()
    return False

def main():
    global orbits;
    global num_of_orbits;
    path = 0
    file = open("input1", "r")
    for line in file:
        list = line.split(")")
        list[1] = list[1][:-1]
        orbits.append(list)
        num_of_orbits.append(-1)
    file.close()
    # print(orbits)
    # print(getNextOrbits())
    start = -1
    for i in range(len(orbits)):
        if orbits[i][0] == "COM":
            start = i
            break

    getFindYou(start)
    print(path_you)
    getFindSanta(start)
    print(path_san)
    i = len(path_you) - 1
    while path_you[i] not in path_san:
        i -= 1
    i += 1
    print(path_you[i:])
    j = len(path_san) - 1
    while path_san[j] not in path_you:
        j -= 1
    j += 1
    print(path_san[j:])

    count = len(path_san) - j + len(path_you) - i - 2
    print(count)

if __name__ == "__main__":
    main()
