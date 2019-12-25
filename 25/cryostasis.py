#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys
import time

from threading import Thread
from Queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names

map = []
x = 0
y = 0
list = [
    "space law space brochure",
    "fixed point",
    "candy cane",
    "sand",
    "ornament",
    "fuel cell",
    "wreath"
]

def enqueueOutput(stdout, queue):
    for line in iter(stdout.readline, ''):
        queue.put(line)
    stdout.close

def enqueueInput(stdin, queue):
    for c in iter(queue.get, ''):
        stdin.write(str(ord(c)) + '\n')
    stdin.close

def initProcess():
    global computers
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    q_out = Queue()
    q_in = Queue()
    t_out = Thread(target=enqueueOutput, args=(p.stdout, q_in))
    t_in = Thread(target=enqueueInput, args=(p.stdin, q_out))
    t_out.daemon = True
    t_out.start()
    t_in.daemon = True
    t_in.start()
    return [p, q_in, q_out]

def addToMap(map, x, y, c):
    if map[y - 10][x - 10] != '#' or c == 'x':
        map[y - 10][x - 10] = c

def handleInput(q):
    # global map
    # global x
    # global y
    time.sleep(0.1)
    string = ""
    try:
        while (True):
            c = chr(int(q.get_nowait()[:-1]))
            string += c
    except:
        # if string.find("north") != -1:
        #     addToMap(map, x, y - 1, '^')
        # if string.find("east") != -1:
        #     addToMap(map, x + 1, y, '>')
        # if string.find("south") != -1:
        #     addToMap(map, x, y + 1, 'v')
        # if string.find("west") != -1:
        #     addToMap(map, x - 1, y, '<')
        print(string)
    return

def handleOutput(q, string):
    for c in string:
        q.put(c)

def getCmd():
    global x
    global y
    string = raw_input()
    string += str('\n')
    # if string.find("north") != -1:
    #     y -= 1
    # if string.find("east") != -1:
    #     x += 1
    # if string.find("south") != -1:
    #     y += 1
    # if string.find("west") != -1:
    #     x -= 1
    return string

def doPart1(q_in, q_out):
    file = open("cmd", "r")
    for line in file:
        handleInput(q_in)
        handleOutput(q_out, line)

    # file = open("cmd", "w+")
    while True:
        try:
            handleInput(q_in)
            printMap()
            cmd = getCmd()
            # file.write(cmd)
            # file.flush()
            handleOutput(q_out, cmd)
        except:
            file.close
            exit()

def printMap():
    global map
    global x
    global y
    addToMap(map, x, y, 'x')
    for line in map:
        print(''.join(line))
    addToMap(map, x, y, '#')

def main():
    # global map
    # for y in range(20):
    #     row = []
    #     for x in range(20):
    #         row.append(' ')
    #     map.append(row)
    [p, q_in, q_out] = initProcess()
    doPart1(q_in, q_out)

if __name__ == "__main__":
    main()
