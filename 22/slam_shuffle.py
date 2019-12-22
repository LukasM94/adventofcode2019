#!/usr/bin/env python3

import sys
from ecdsa import SigningKey, VerifyingKey, BadSignatureError, NIST256p, NIST192p
from ecdsa.numbertheory import inverse_mod

number_of_cards = 0

def getCards():
    global number_of_cards
    cards = []
    for i in range(number_of_cards):
        cards.append(i)
    return cards

def readInput():
    file = open("input", "r")
    cmds = []
    for line in file:
        cmds.append(line.split())
    return cmds

def cut(number, cards):
    first_cards = cards[:number]
    second_cards = cards[number:]
    cards = second_cards + first_cards
    return cards

def dealWithIncrement(number, cards):
    global number_of_cards
    temp_cards = []
    for i in range(number_of_cards):
        temp_cards.append([])
    for i in range(number_of_cards):
        temp_i = i * number
        temp_i = temp_i % number_of_cards
        temp_cards[temp_i].append(cards[i])
    cards = []
    for entry in temp_cards:
        cards += entry
    return cards

def dealIntoNewStack(cards):
    cards.reverse()
    return cards

def handleCmds(cards, cmds):
    if len(cmds) == 0:
        return cards
    cmd = cmds.pop(0)
    # print("cards are  " + str(cards))
    # print("command is " + str(cmd))
    if cmd[0] == "cut":
        number = int(cmd[1])
        cards = cut(number, cards)
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

def handleCmdsPart2(number, length, cmds):
    if len(cmds) == 0:
        return number
    cmd = cmds.pop(0)
    if cmd[0] == "cut":
        n = int(cmd[1])
        number = number + n
        number = number % length
    elif cmd[0] == "deal":
        if cmd[1] == "with" and cmd[2] == "increment":
            n = int(cmd[3])
            n = inverse_mod(n, length)
            number = number * n
            number = number % length
        elif cmd[1] == "into" and cmd[2] == "new" and cmd[3] == "stack":
            number = length - number - 1
        else:
            print("do not know the command")
    else:
        print("do not know the command")
    return handleCmdsPart2(number, length, cmds)

def main():
    global number_of_cards
    # global TESTING
    # if len(sys.argv) > 1 and sys.argv[1] == "TEST":
    #     number_of_cards = 10
    #     TESTING = True
    # else:
    #     number_of_cards = 10007
    #     TESTING = False
    # cards = getCards()
    # cmds = readInput()
    # cards = handleCmds(cards, cmds)
    # print(cards[2020])
    number_of_cards = 119315717514047
    # cards = getCards()
    cmds = readInput()
    cmds.reverse()
    # if TESTING == True:
    #     print("Result is " + str(cards))
    # else:
        # for i in range(len(cards)):
        #     if cards[i] == 2019:
        #         print("2019 card is at position " + str(i))
    number = 2020
    number = handleCmdsPart2(number, 119315717514047, cmds)
    print(number)


if __name__ == "__main__":
    main()
