#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

def pipe(p):
    i = p.stdout.readline()
    print(i)
    # while True:
    #     try:
    #     except:
    #         return

def start(p, instructions):
    while len(instructions) > 0:
        instr = instructions.pop(0)
        # print(instr)
        for c in instr:
            print(ord(c))
            p.stdin.write(c)

def handleInstructions(p):
    instructions = []
    while True:
        instr = raw_input('')
        try:
            instructions.append(instr + '\n')
            if instr == 'WALK':
                break
        except:
            print("error")
            exit()
    return instructions

def readPromp(p):
    string = []
    c = ''
    while True:
        c = int(p.stdout.readline())
        if c == 10:
            break
        string.append(chr(c))
    return ''.join(string)

def handlePromp(p):
    string = readPromp(p)
    print(string)

def main():
    p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    handlePromp(p)
    instructions = handleInstructions(p)
    start(p, instructions)
    pipe(p)

if __name__ == "__main__":
    main()
