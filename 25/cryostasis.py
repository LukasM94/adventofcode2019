#!/usr/bin/env python2
from subprocess import Popen, PIPE, STDOUT
import os
import sys
import time

from threading import Thread
from Queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names


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

def handleInput(q):
    time.sleep(0.1)
    string = ""
    try:
        while (True):
            c = chr(int(q.get_nowait()[:-1]))
            string += c
    except:
        print(string)
    return

def handleOutput(q, string):
    for c in string:
        q.put(c)

def getCmd():
    c = raw_input()
    c += str('\n')
    return c

def doPart1(q_in, q_out):
    while True:
        try:
            handleInput(q_in)
            cmd = getCmd()
            handleOutput(q_out, cmd)
        except:
            exit()

def main():
    [p, q_in, q_out] = initProcess()
    doPart1(q_in, q_out)

if __name__ == "__main__":
    main()
