#!/usr/bin/env python3
# part 1
file = open("./input1", "r")
sum = 0
for line in file:
    sum += int(int(line) / 3) - 2
print(sum)
file.close()
# part 2

def calc(number):
    if number < 0:
        return 0
    fuel = int(number / 3) - 2
    add_fuel = calc(fuel)
    if add_fuel > 0:
        fuel += add_fuel
    return fuel

file = open("./input2", "r")
sum = 0
for line in file:
    sum += calc(int(line))
print(sum)
file.close()
