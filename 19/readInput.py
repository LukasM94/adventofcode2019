#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

width = 120
height = 100

map = []
for y in range(height):
    row = []
    for x in range(width):
        p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        p.stdin.write(str(x) + '\n')
        p.stdin.write(str(y) + '\n')
        # print("write x <" + str(x) + ">, y <" + str(y) + ">")
        c = int(p.stdout.readline())
        # print("read " + str(c))
        if c == 1:
            row.append('#')
        else:
            row.append('.')
    map.append(row)

file = open("beam", "w")
for line in map:
    file.write(''.join(line) + '\n')
file.close
