#!/usr/bin/env python3

number_of_cards = 10

def getCards():
    global number_of_cards
    cards = []
    for i in range(number_of_cards):
        cards.append(i)

def readInput():
    file = open("input", "r")
    cmds = []
    for line in file:
        cmds.append(line.split())
    return cmds

def cutPositiv(number, cards):
    return []

def cutNegativ(number, cards):
    return []

def dealWithIncrement(number, cards):
    return []

def dealIntoNewStack(cards):
    return []

def handleCmds(cards, cmds):
    if len(cmds) == 0:
        return cards
    cmd = cmds.pop(0)
    print("command is " + str(cmd))
    if cmd[0] == "cut":
        number = int(cmds[1])
        if number > 0:
            cards = cutPositiv(number, cards)
        elif number < 0:
            cards = cutNegativ(number, cards)
        else:
            print("0 is not allowed")
    elif cmd[0] == "deal":
        if cmd[1] == "with" and cmd[2] == "increment":
            number = int(cmd[3])
            cards = dealWithIncrement(number, cards)
        elif cmd[1] == "into" and cmd[2] == "new" and cmd[3] == "stack":
            cards = dealIntoNewStack(cards)
        else:
            print("do not know the command")
    else:
        print("do not know the command")
    return handleCmds(cards, cmds)

def main():
    cards = getCards()
    cmds = readInput()
    cards = handleCmds(cards, cmds)
    print("Result is " + str(cards))

if __name__ == "__main__":
    main()
