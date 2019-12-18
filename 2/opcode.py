#!/usr/bin/env python3

def compute(opcode):
    ic = 0
    result = 0
    operant1 = 0
    operant2 = 0
    dest = 0
    while True:
        ## fetch
        ir = int(opcode[ic])
        # print("ir = " + str(ir))
        if ir == 99:
            break;
        ## read
        ic += 1
        operant1 = int(opcode[ic])
        # print("operant1 = " + str(operant1))
        ic += 1
        operant2 = int(opcode[ic])
        # print("operant2 = " + str(operant2))
        ic += 1
        dest = int(opcode[ic])
        # print("dest = " + str(dest))
        ic += 1
        ## execute
        if ir == 1:
            result = int(opcode[operant1]) + int(opcode[operant2])
            # print("mem(" + str(dest) + ") = mem(" + str(operant1) + ") + mem(" + str(operant2) + ")")
            # print("mem(" + str(dest) + ") = " + str(opcode[operant1]) + " + " + str(opcode[operant2]))
        elif ir == 2:
            result = int(opcode[operant1]) * int(opcode[operant2])
            # print("mem(" + str(dest) + ") = mem(" + str(operant1) + ") * mem(" + str(operant2) + ")")
            # print("mem(" + str(dest) + ") = " + str(opcode[operant1]) + " * " + str(opcode[operant2]))
        ## write back
        # print("mem(" + str(dest) + ") = " + str(result))
        opcode[dest] = result
        # print(opcode)
    # print(opcode)
    return opcode[0]

for noun in range(100):
    for verb in range(100):
        file = open("./input2", "r")
        line = file.readline()
        opcode = line.split(",")
        file.close()
        opcode[1] = str(noun)
        opcode[2] = str(verb)
        if compute(opcode) == 19690720:
            result = 100 * noun + verb

print(result)
