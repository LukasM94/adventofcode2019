#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys
import time
from threading import Thread
from Queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names

computers = 50
goal_address = 255
no_input = -1
nat = []

def initProcesses():
    global computers
    list_of_p = []
    for i in range(computers):
        p = Popen(['./int_computer.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE, bufsize=1, close_fds=ON_POSIX)
        list_of_p.append(p)
    return list_of_p

def initInputQueue():
    global computers
    input_queue = []
    for i in range(computers):
        input_queue.append([i])
    return input_queue

def enqueueOutput(out, queue):
    for line in iter(out.readline, ''):
        queue.put(line)
    out.close

def initOutputQueue(list_of_p):
    global computers
    output_queue = []
    for i in range(computers):
        p = list_of_p[i]
        q = Queue()
        t = Thread(target=enqueueOutput, args=(p.stdout, q))
        t.daemon = True
        t.start()
        output_queue.append(q)
    return output_queue

def writeToComputers(list_of_p, input_queue):
    print("writeToComputers")
    global computers
    global no_input
    for i in range(computers):
        p = list_of_p[i]
        if input_queue[i] == []:
            print("write " + str(-1) + " to process " + str(i))
            p.stdin.write(str(-1) + '\n')
        else:
            for entry in input_queue[i]:
                print("write " + str(entry) + " to process " + str(i))
                p.stdin.write(str(entry) + '\n')
        input_queue[i] = []

def redirectPackets(input_queue, output_queue):
    print("redirectPackets")
    global computers
    global nat
    for i in range(computers):
        q = output_queue[i]
        try:
            while True:
                pid = int(q.get_nowait())
                # print("pid <" + str(pid) + ">")
                x = int(q.get_nowait())
                # print("x <" + str(x) + ">")
                y = int(q.get_nowait())
                # print("y <" + str(y) + ">")
                if pid == 255:
                    if nat != [] and nat[1] == y:
                        print("naty is " + str(y))
                    nat = [x, y]
                    break
                print("pid <" + str(pid) + ">, x <" + str(x) + ">, y <" + str(y) + ">")
                input_queue[pid].append(x)
                input_queue[pid].append(y)
        except:
            continue

def natSentPackage(input_queue):
    global nat
    print("natSentPackage: x <" + str(nat[0]) + ">, y <" + str(nat[1]) + ">")
    input_queue[0].append(nat[0])
    input_queue[0].append(nat[1])

count = 0

def isIdle(input_queue):
    global count
    for entry in input_queue:
        if entry != []:
            return False
    for entry in input_queue:
        print(entry)
    if count == 10:
        print("is idle")
        count = 0
        return True
    count += 1

def handlePart1(list_of_p, input_queue, output_queue):
    while True:
        redirectPackets(input_queue, output_queue)
        if isIdle(input_queue) == True:
            natSentPackage(input_queue)
        else:
            writeToComputers(list_of_p, input_queue)
        time.sleep(0.01)

def main():
    list_of_p = initProcesses()
    input_queue = initInputQueue()
    output_queue = initOutputQueue(list_of_p)
    writeToComputers(list_of_p, input_queue)
    writeToComputers(list_of_p, input_queue)
    handlePart1(list_of_p, input_queue, output_queue)

if __name__ == "__main__":
    main()
