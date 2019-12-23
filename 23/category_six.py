#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys

computers = 50
goal_address = 255
no_input = -1

def getProcessed():
    global computers
    list_of_p = []
    for i in range(computers):
        p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        list_of_p.append(p)
    return list_of_p

def getInputQueue():
    global computers
    input_queue = []
    for i in range(computers):
        input_queue.append(i)
    return input_queue

def getOutputQueue():
    global computers
    output_queue = []
    for i in range(computers):
        output_queue.append([])
    return output_queue

def startComputers(list_of_p, input_queue):
    global computers
    for i in range(computers):
        p = list_of_p[i]
        input_for_p = list_of_p[i]
        p.stdin.write(str(input_for_p) + '\n')

def handlePart1(list_of_p, input_queue, output_queue):
    global goal_address

def main():
    list_of_p = getProcessed()
    input_queue = getInputQueue()
    output_queue = getOutputQueue()
    startComputers(list_of_p, input_queue)
    handlePart1(list_of_p, input_queue, output_queue)

if __name__ == "__main__":
    main()
