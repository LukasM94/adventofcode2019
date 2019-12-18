#!/usr/bin/env python2

from subprocess import Popen, PIPE, STDOUT
import time
phase_list = []

def setPhaseList():
    global phase_list
    start = 1234
    end   = 43210
    i = start
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    number = bytearray(5)
    while i <= end:
        number[0] = i % 10
        number[1] = int(i / 10) % 10
        number[2] = int(i / 100) % 10
        number[3] = int(i / 1000) % 10
        number[4] = int(i / 10000) % 10
        zero = int(number[0] == 0) + int(number[1] == 0) + int(number[2] == 0) + int(number[3] == 0) + int(number[4] == 0)
        one = int(number[0] == 1) + int(number[1] == 1) + int(number[2] == 1) + int(number[3] == 1) + int(number[4] == 1)
        two = int(number[0] == 2) + int(number[1] == 2) + int(number[2] == 2) + int(number[3] == 2) + int(number[4] == 2)
        three = int(number[0] == 3) + int(number[1] == 3) + int(number[2] == 3) + int(number[3] == 3) + int(number[4] == 3)
        four = int(number[0] == 4) + int(number[1] == 4) + int(number[2] == 4) + int(number[3] == 4) + int(number[4] == 4)
        if zero == 1 and one == 1 and two == 1 and three == 1 and four == 1:
            phase_list.append(i)
        i += 1
    print(phase_list)

def setPhaseLis2():
    global phase_list
    start = 56789
    end   = 98765
    i = start
    five = 0
    six = 0
    seven = 0
    eigth = 0
    nine = 0
    number = bytearray(5)
    while i <= end:
        number[0] = i % 10
        number[1] = int(i / 10) % 10
        number[2] = int(i / 100) % 10
        number[3] = int(i / 1000) % 10
        number[4] = int(i / 10000) % 10
        five = int(number[0] == 5) + int(number[1] == 5) + int(number[2] == 5) + int(number[3] == 5) + int(number[4] == 5)
        six = int(number[0] == 6) + int(number[1] == 6) + int(number[2] == 6) + int(number[3] == 6) + int(number[4] == 6)
        seven = int(number[0] == 7) + int(number[1] == 7) + int(number[2] == 7) + int(number[3] == 7) + int(number[4] == 7)
        eigth = int(number[0] == 8) + int(number[1] == 8) + int(number[2] == 8) + int(number[3] == 8) + int(number[4] == 8)
        nine = int(number[0] == 9) + int(number[1] == 9) + int(number[2] == 9) + int(number[3] == 9) + int(number[4] == 9)
        if five == 1 and six == 1 and seven == 1 and eigth == 1 and nine == 1:
            phase_list.append(i)
        i += 1
    print(phase_list)
    # file = open("phase_list", "w")
    # file.write(str(len(phase_list)) + "\n")
    # for i in phase_list:
    #     file.write(str(i) + "\n")
    # file.close()

def doJob(j):
    global phase_list
    number = bytearray(5)
    number[0] = phase_list[j] % 10
    number[1] = int(phase_list[j] / 10) % 10
    number[2] = int(phase_list[j] / 100) % 10
    number[3] = int(phase_list[j] / 1000) % 10
    number[4] = int(phase_list[j] / 10000) % 10

    next = 0
    for i in range(5):
        p = Popen(['./opcode.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        print >> p.stdin, number[i]
        p.stdin.flush()
        print >> p.stdin, next
        p.stdin.flush()
        list = p.communicate("n\n")[0]
        next = list.split("\n")[-2]
    print next
    return next

def doJob2(j):
    global phase_list
    number = bytearray(5)
    number[0] = phase_list[j] % 10
    number[1] = int(phase_list[j] / 10) % 10
    number[2] = int(phase_list[j] / 100) % 10
    number[3] = int(phase_list[j] / 1000) % 10
    number[4] = int(phase_list[j] / 10000) % 10

    next = 0

    p0 = Popen(['./opcode.py'], stdout=PIPE, stdin=PIPE)
    p1 = Popen(['./opcode.py'], stdout=PIPE, stdin=PIPE)
    p2 = Popen(['./opcode.py'], stdout=PIPE, stdin=PIPE)
    p3 = Popen(['./opcode.py'], stdout=PIPE, stdin=PIPE)
    p4 = Popen(['./opcode.py'], stdout=PIPE, stdin=PIPE)

    p0.stdin.write(str(number[0]) + "\n")
    p1.stdin.write(str(number[1]) + "\n")
    p2.stdin.write(str(number[2]) + "\n")
    p3.stdin.write(str(number[3]) + "\n")
    p4.stdin.write(str(number[4]) + "\n")

    i = 0
    while True:
        try:
            p0.stdin.write(str(next) + "\n")
            next = int(p0.stdout.readline())
            # print(next)
        except:
            return next
        p1.stdin.write(str(next) + "\n")
        next = int(p1.stdout.readline())
        # print(next)
        p2.stdin.write(str(next) + "\n")
        next = int(p2.stdout.readline())
        # print(next)
        p3.stdin.write(str(next) + "\n")
        next = int(p3.stdout.readline())
        # print(next)
        p4.stdin.write(str(next) + "\n")
        next = int(p4.stdout.readline())
        # print(next)
        i += 1

def main():
    global phase_list
    # setPhaseList()
    # highest = 0
    # highest_i = 0
    # for i in range(len(phase_list)):
    #     cur = doJob(i)
    #     if cur > highest:
    #         highest = cur
    #         highest_i = i
    # print highest
    setPhaseLis2()
    # print doJob2(0)
    highest = 0
    highest_i = 0
    for i in range(len(phase_list)):
        cur = doJob2(i)
        if cur > highest:
            highest = cur
            highest_i = i
    print highest

if __name__ == "__main__":
    main()
