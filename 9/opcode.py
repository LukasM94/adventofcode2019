#!/usr/bin/env python3

opcode   = []
rel_base = 0
ip       = 0

cmd                   = 0
first_parameter_mode  = 0
second_parameter_mode = 0
third_parameter_mode  = 0

def readInstruction(ir):
    global cmd
    global first_parameter_mode
    global second_parameter_mode
    global third_parameter_mode
    cmd                   = int(ir % 100)
    first_parameter_mode  = int((ir / 100) % 10)
    second_parameter_mode = int((ir / 1000) % 10)
    third_parameter_mode  = int((ir / 10000) % 10)

def getFirstAddress():
    global opcode
    global rel_base
    global ip
    global first_parameter_mode
    if first_parameter_mode == 0:
        address = int(opcode[ip])
    elif first_parameter_mode == 1:
        address = ip
    elif first_parameter_mode == 2:
        rel_address = int(opcode[ip])
        address = rel_address + rel_base
    ip += 1
    return address

def getSecondAddress():
    global opcode
    global rel_base
    global ip
    global second_parameter_mode
    if second_parameter_mode == 0:
        address = int(opcode[ip])
    elif second_parameter_mode == 1:
        address = ip
    elif second_parameter_mode == 2:
        rel_address = int(opcode[ip])
        address = rel_address + rel_base
    ip += 1
    return address

def getDestAddress():
    global opcode
    global rel_base
    global ip
    global third_parameter_mode
    if third_parameter_mode == 0:
        address = int(opcode[ip])
    elif third_parameter_mode == 2:
        rel_address = int(opcode[ip])
        address = rel_address + rel_base
    ip += 1
    return address

def getFirstParam():
    global opcode
    return int(opcode[getFirstAddress()])

def getSecondParam():
    global opcodegetDestAddressAddress
    return int(opcode[getSecondAddress()])

def add():
    ## ADD
    global opcode
    if __debug__: print("ADD")
    if __debug__: print(opcode[ip-1:ip+3])
    operant1 = getFirstParam()
    operant2 = getSecondParam()
    dest = getDestAddress()
    opcode[dest] = operant1 + operant2
    if __debug__: print("opcode[" + str(dest) + "] = " + str(operant1) + " + " + str(operant2))

def mult():
    ## MULT
    global opcode
    if __debug__: print("MULT")
    if __debug__: print(opcode[ip-1:ip+3])
    operant1 = getFirstParam()
    operant2 = getSecondParam()
    dest = getDestAddress()
    opcode[dest] = operant1 * operant2
    if __debug__: print("opcode[" + str(dest) + "] = " + str(operant1) + " * " + str(operant2))

def getchar():
    ## GETCHAR
    global opcode
    if __debug__: print("getchar")
    if __debug__: print(opcode[ip-1:ip+1])
    dest = getFirstAddress()
    opcode[dest] = int(input())

def putchar():
    ## PUTCHAR
    global opcode
    if __debug__: print("putchar")
    if __debug__: print(opcode[ip-1:ip+1])
    src = getFirstParam()
    print(src)

def jumpIfTrue():
    ## JUMP IF TRUE
    global opcode
    global ip
    if __debug__: print("jump if true")
    if __debug__: print(opcode[ip-1:ip+2])
    operant1 = getFirstParam()
    operant2 = getSecondParam()
    if operant1 != 0:
        ip = operant2

def jumpIfFalse():
    ## JUMP IF FALSE
    global opcode
    global ip
    if __debug__: print("jump if false")
    if __debug__: print(opcode[ip-1:ip+2])
    operant1 = getFirstParam()
    operant2 = getSecondParam()
    if __debug__: print(str(operant1) + " == 0")
    if operant1 == 0:
        ip = operant2

def lessThan():
    ## LESS THAN
    global opcode
    global ip
    if __debug__: print("less than")
    if __debug__: print(opcode[ip-1:ip+3])
    operant1 = getFirstParam()
    operant2 = getSecondParam()
    dest = getDestAddress()
    if __debug__: print(str(operant1) + " < " + str(operant2))
    if operant1 < operant2:
        opcode[dest] = 1
    else:
        opcode[dest] = 0

def equal():
    ## EQUAL
    global opcode
    if __debug__: print("equal")
    if __debug__: print(opcode[ip-1:ip+1])
    operant1 = getFirstParam()
    operant2 = getSecondParam()
    dest = getDestAddress()
    if __debug__: print(str(operant1) + " == " + str(operant2))
    if operant1 == operant2:
        opcode[dest] = 1
    else:
        opcode[dest] = 0

def changeRelBase():
    ## CHANGE RELATIVE BASE
    global opcode
    global rel_base
    if __debug__: print("change rel base")
    if __debug__: print(opcode[ip-1:ip+1])
    operant1 = getFirstParam()
    rel_base += operant1
    if __debug__: print("rel base now " + str(rel_base))

def fetch():
    ## FETCH
    global opcode
    global ip
    ir = int(opcode[ip])
    ip += 1
    return ir

def compute():
    global opcode
    global rel_base
    global ip
    global cmd
    global first_parameter_mode
    global second_parameter_mode
    while True:
        ## fetch
        ir = fetch()
        ## read
        readInstruction(ir)
        ## execute
        if cmd == 1:
            add()
        elif cmd == 2:
            mult()
        elif cmd == 3:
            getchar()
        elif cmd == 4:
            putchar()
        elif cmd == 5:
            jumpIfTrue()
        elif cmd == 6:
            jumpIfFalse()
        elif cmd == 7:
            lessThan()
        elif cmd == 8:
            equal()
        elif cmd == 9:
            changeRelBase()
        elif cmd == 99:
            exit()

def main():
    global opcode
    file = open("./input", "r")
    line = file.readline()
    opcode = line.split(",")
    file.close()
    for i in range(4096):
        opcode.append(0)
    if __debug__: print(opcode)
    result = compute()

if __name__ == "__main__":
    main()
