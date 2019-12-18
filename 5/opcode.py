#!/usr/bin/env python3

def compute(opcode):
    ip = 0
    result = 0
    operant1 = 0
    operant2 = 0
    first_parameter = 0
    second_parameter = 0
    dest = 0
    while True:
        ## fetch
        ir = int(opcode[ip])
        if ir == 99:
            break;
        ip += 1
        ## read
        cmd                = int(ir % 100)
        first_param_mode   = int((ir / 100) % 10)
        second_param_mode = int((ir / 1000) % 10)
        third_param_mode   = int((ir / 10000) % 10)
        ## execute
        if cmd == 1:
            ## ADD
            print("ADD")
            print(opcode[ip-1:ip+3])
            if first_param_mode == 0:
                operant1 = int(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                operant1 = int(opcode[ip])
            ip += 1
            if second_param_mode == 0:
                operant2 = int(opcode[int(opcode[ip])])
            elif second_param_mode == 1:
                operant2 = int(opcode[ip])
            ip += 1
            dest = int(opcode[ip])
            ip += 1
            opcode[dest] = operant1 + operant2
            # print("opcode[" + str(dest) + "] = " + str(operant1) + " + " + str(operant2))
        elif cmd == 2:
            ## MULT
            print("MULT")
            print(opcode[ip-1:ip+3])
            if first_param_mode == 0:
                operant1 = int(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                operant1 = int(opcode[ip])
            ip += 1
            if second_param_mode == 0:
                operant2 = int(opcode[int(opcode[ip])])
            elif second_param_mode == 1:
                operant2 = int(opcode[ip])
            ip += 1
            dest = int(opcode[ip])
            ip += 1
            opcode[dest] = operant1 * operant2
            # print("opcode[" + str(dest) + "] = " + str(operant1) + " * " + str(operant2))
        elif cmd == 3:
            ## GETCHAR
            print("getchar")
            print(opcode[ip-1:ip+1])
            if first_param_mode == 0:
                dest = int(opcode[ip])
            elif first_param_mode == 1:
                dest = ip
            ip += 1
            opcode[dest] = int(input())
        elif cmd == 4:
            ## PUTCHAR
            print("putchar")
            print(opcode[ip-1:ip+1])
            if first_param_mode == 0:
                print(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                print(opcode[ip])
            ip += 1
        elif cmd == 5:
            ## JUMP IF TRUE
            print("jump if true")
            print(opcode[ip-1:ip+2])
            if first_param_mode == 0:
                first_parameter = int(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                first_parameter = int(opcode[ip])
            ip += 1
            if second_param_mode == 0:
                second_parameter = int(opcode[int(opcode[ip])])
            elif second_param_mode == 1:
                second_parameter = int(opcode[ip])
            ip += 1
            if first_parameter != 0:
                ip = second_parameter
        elif cmd == 6:
            ## JUMP IF FALSE
            print("jump if false")
            print(opcode[ip-1:ip+2])
            if first_param_mode == 0:
                first_parameter = int(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                first_parameter = int(opcode[ip])
            ip += 1
            if second_param_mode == 0:
                second_parameter = int(opcode[int(opcode[ip])])
            elif second_param_mode == 1:
                second_parameter = int(opcode[ip])
            ip += 1
            print(str(first_parameter) + " == 0")
            if first_parameter == 0:
                ip = second_parameter
        elif cmd == 7:
            ## LESS THAN
            print("less than")
            print(opcode[ip-1:ip+3])
            if first_param_mode == 0:
                first_parameter = int(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                first_parameter = int(opcode[ip])
            ip += 1
            if second_param_mode == 0:
                second_parameter = int(opcode[int(opcode[ip])])
            elif second_param_mode == 1:
                second_parameter = int(opcode[ip])
            ip += 1
            dest = int(opcode[ip])
            ip += 1
            print(str(first_parameter) + " < " + str(second_parameter))
            if first_parameter < second_parameter:
                opcode[dest] = 1
            else:
                opcode[dest] = 0
        elif cmd == 8:
            ## EQUAL
            print("equal")
            print(opcode[ip-1:ip+1])
            if first_param_mode == 0:
                first_parameter = int(opcode[int(opcode[ip])])
            elif first_param_mode == 1:
                first_parameter = int(opcode[ip])
            ip += 1
            if second_param_mode == 0:
                second_parameter = int(opcode[int(opcode[ip])])
            elif second_param_mode == 1:
                second_parameter = int(opcode[ip])
            ip += 1
            dest = int(opcode[ip])
            ip += 1
            print(str(first_parameter) + " == " + str(second_parameter))
            if first_parameter == second_parameter:
                opcode[dest] = 1
            else:
                opcode[dest] = 0
        ## write back
    return opcode[0]

file = open("./input_thomas", "r")
line = file.readline()
opcode = line.split(",")
file.close()
# print(opcode)
result = compute(opcode)
# print(opcode)
