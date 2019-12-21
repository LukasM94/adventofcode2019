#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

def handleInput(p):
    while True:
        i = getInput(p)
        if i == '':
            break
        print(i)

def getInput(p):
    string = []
    while True:
        try:
            i = int(p.stdout.readline())
            string.append(chr(i))
            if i == 10:
                break
        except:
            print("solution is " + str(i))
            break
    if len(string) > 1:
        string = string[:-1]
    return ''.join(string)

def start(p, instructions):
    while len(instructions) > 0:
        instr = instructions.pop(0)
        print(instr[:-1])
        for c in instr:
            # print(ord(c))
            p.stdin.write(str(ord(c)) + '\n')

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
    handleInput(p)

if __name__ == "__main__":
    main()
