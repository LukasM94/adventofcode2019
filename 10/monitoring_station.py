#!/usr/bin/env python3

import math
import numpy

asteroids = []
view_asteroids = []
sorted_angles = []
goal_asteroid = []
goal_i = 0

def readAsteroids():
    global asteroids
    file = open("input", "r")
    row    = 0
    column = 0
    for line in file:
        for column in range(len(line)):
            if line[column] == '#':
                asteroids.append([column, row])
        row += 1
    file.close()
    if __debug__: print(asteroids)

def getUnionPoint(current_asteroid, asteroid):
    diff = [current_asteroid[0] - asteroid[0], current_asteroid[1] - asteroid[1]]
    abs  = diff[0] * diff[0] + diff[1] * diff[1]
    abs = math.sqrt(abs)
    if abs == 0:
        return []
    diff[0] = diff[0] / abs
    diff[0] = math.floor(diff[0] * 10000) / 10000
    diff[1] = diff[1] / abs
    diff[1] = math.floor(diff[1] * 10000) / 10000
    return diff

def getViewAsteroids(current_asteroid):
    global asteroids
    count = 0
    black_list = []
    if __debug__: print("current_asteroid is " + str(current_asteroid))
    for asteroid in asteroids:
        angle = getUnionPoint(current_asteroid, asteroid)
        if __debug__: print(angle)
        if angle != [] and angle not in black_list:
            black_list.append(angle)
            count += 1
    if __debug__: print(count)
    return count

def goAll():
    global asteroids
    global view_asteroids
    for current_asteroid in asteroids:
        view = getViewAsteroids(current_asteroid)
        view_asteroids.append(view)

def searchHighest():
    global asteroids
    global view_asteroids
    global goal_i
    global goal_asteroid
    highest = 0
    highest_i = 0
    for i in range(len(view_asteroids)):
        if view_asteroids[i] > highest:
            highest_i = i
            highest = view_asteroids[i]
    print(asteroids[highest_i])
    print(highest)
    goal_i = highest_i
    goal_asteroid = asteroids[highest_i]

def getAngle(asteroid, ref_asteroid):
    if ref_asteroid == asteroid:
        return 0
    diff = [ref_asteroid[0] - asteroid[0], ref_asteroid[1] - asteroid[1]]
    angle = numpy.arctan2(-diff[0], diff[1])
    if angle < 0:
        angle += 2 * math.pi
    angle = math.floor(angle * 100000) / 100000
    return angle

def getDistance(asteroid, ref_asteroid):
    diff = [ref_asteroid[0] - asteroid[0], ref_asteroid[1] - asteroid[1]]
    abs  = diff[0] * diff[0] + diff[1] * diff[1]
    abs  = math.sqrt(abs)
    abs  = math.floor(abs * 10000) / 10000
    return abs

def searchAllAngles():
    global asteroids
    global sorted_angles
    angles = []
    for i in range(len(asteroids)):
        angle = getAngle(asteroids[i], goal_asteroid)
        if __debug__: print(str(asteroids[i]) + " with angle " + str(angle))
        distance = getDistance(asteroids[i], goal_asteroid)
        angles.append([angle, distance, i])
    angles.sort(key=lambda distance: distance[1])
    angles.sort(key=lambda angle: angle[0])
    angles.pop(0)
    # print(angles)
    print("-----------------------------")
    for i in range(len(angles)):
        asteroid = asteroids[angles[i][2]]
        print(asteroid)
    i = 0
    count = 0
    current_angle = []
    found = False
    print("-----------------------------")
    while len(angles) != 0 and count != 200:
        current_angle = angles[i]
        angles.pop(i)
        print(asteroids[current_angle[2]])
        count += 1
        i = i % len(angles)
        while angles[i][0] == current_angle[0]:
            i += 1
            i = i % len(angles)
    asteroid = asteroids[current_angle[2]]
    print("-----------------------------")
    print(asteroid)
    print(asteroid[0] * 100 + asteroid[1])

def main():
    readAsteroids()
    goAll()
    searchHighest()
    searchAllAngles()


if __name__ == "__main__":
    main()
