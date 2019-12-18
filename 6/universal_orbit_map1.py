#!/usr/bin/env python3
import math

orbits = []
num_of_orbits = []

def rec(i):
    global orbits
    global num_of_orbits;
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


def getNextOrbits(i):
    global orbits;
    sum = 0
    for j in range(len(orbits)):
        sum += rec(j)
    return sum

def main():
    global orbits;
    global num_of_orbits;
    file = open("input1", "r")
    for line in file:
        list = line.split(")")
        list[1] = list[1][:-1]
        orbits.append(list)
        num_of_orbits.append(-1)
    file.close()
    print(orbits)
    print(getNextOrbits(0))

if __name__ == "__main__":
    main()
