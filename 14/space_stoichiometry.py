#!/usr/bin/env python3

import math

reactions = []
reserved_elements = []
already_used = []

class Reaction:
    def __init__(self, lhs, rhs):
        self.lhs_ = lhs
        self.rhs_ = rhs

    def print(self):
        print("lhs " + str(self.lhs_) + ", rhs " + str(self.rhs_))

    def containInLhs(self, element):
        for entry in self.lhs_:
            if entry[1] == element:
                return True
        return False

def readInput():
    global reactions
    file = open("input", "r")
    for line in file:
        splitted_line = line.split(" => ")
        temp = splitted_line[0].split(", ")
        lhs = []
        for entry in temp:
            lhs.append(entry.split(" "))
        rhs = splitted_line[1].split(" ")
        rhs[1] = rhs[1][:-1]
        reactions.append(Reaction(lhs, rhs))
    file.close()

def printAll():
    global reactions
    global reserved_elements
    print("==============print=reactions====")
    for reaction in reactions:
        reaction.print()
    print("==============print=reserved=====")
    for element in reserved_elements:
        print(element)
    print("==============print=end============")

def addToReservedElements(element):
    global reserved_elements
    for entry in reserved_elements:
        if entry[1] == element[1]:
            entry[0] += int(element[0])
            return
    reserved_elements.append([int(element[0]), element[1]])

def getReserevElement(element):
    global reserved_elements
    for entry in reserved_elements:
        if entry[1] == element[1]:
            entry[0] += int(element[0])
            return entry
    return []

def recursive(element_name, count):
    global reactions
    global reserved_elements
    global already_used
    print("recursive(" + str(element_name) + ", " + str(count) + ")")
    i = 0
    found = False
    for i in range(len(reactions)):
        if reactions[i].rhs_[1] == element_name:
            found = True
            break
    entry = reactions[i]
    mult = math.ceil(count / int(entry.rhs_[0]))
    if entry.lhs_[0][1] == "ORE":
        print("count = " + str(count))
        return mult * int(entry.lhs_[0][0])
    print("start")
    entry.print()
    sub_element = []
    print("==============start=loop=========")
    result = 0
    for sub_element in entry.lhs_:
        contains = False
        sub_element[0] = mult * int(sub_element[0])
        for sub_entry in reactions:
            if sub_entry != entry and sub_entry.containInLhs(sub_element[1]) == True:
                contains = True
                break
        if contains == True:
            print("contains " + str(sub_element))
            addToReservedElements(sub_element)
            already_used.append(sub_element)
        else:
            print("not contains " + str(sub_element))
            element = getReserevElement(sub_element)
            if element != []:
                sub_element[0] = element[0]

    reactions.pop(i)
    for sub_element in entry.lhs_:
        contains = False
        for sub_entry in reactions:
            if sub_entry.containInLhs(sub_element[1]) == True or sub_element in already_used:
                contains = True
                break
        if contains == False:
            result += recursive(sub_element[1], int(sub_element[0]))
    print("==============end=loop===========")
    entry.print()
    print("done")
    printAll()
    return result

def main():
    readInput()
    printAll()
    # print(recursive("FUEL", 1))
    print(recursive("FUEL", 3061522))


if __name__ == "__main__":
    main()
