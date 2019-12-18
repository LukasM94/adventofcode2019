#!/usr/bin/env python3

start = 367479
end   = 893698
count = 0
i     = start
number = bytearray(6)
while i < end:
    number[0] = i % 10
    number[1] = int(i / 10) % 10
    number[2] = int(i / 100) % 10
    number[3] = int(i / 1000) % 10
    number[4] = int(i / 10000) % 10
    number[5] = int(i / 100000) % 10

    if number[0] < number[1] or number[1] < number[2] or number[2] < number[3] or number[3] < number[4] or number[4] < number[5]:
        i += 1
        continue
    j = 0
    while j < (len(number) - 5):
        if number[j] == number[j + 1] and number[j + 1] == number[j + 2] and number[j + 2] == number[j + 3] and number[j + 3] == number[j + 4] and number[j + 4] == number[j + 5]:
            number[j]     = 10
            number[j + 1] = 10
            number[j + 2] = 10
            number[j + 3] = 10
            number[j + 4] = 10
            number[j + 5] = 10
            # print("found 6")
        j += 1
    j = 0
    while j < (len(number) - 4):
        if number[j] == number[j + 1] and number[j + 1] == number[j + 2] and number[j + 2] == number[j + 3] and number[j + 3] == number[j + 4]:
            number[j]     = 10
            number[j + 1] = 10
            number[j + 2] = 10
            number[j + 3] = 10
            number[j + 4] = 10
            # print("found 5")
        j += 1
    j = 0
    while j < (len(number) - 3):
        if number[j] == number[j + 1] and number[j + 1] == number[j + 2] and number[j + 2] == number[j + 3]:
            number[j]     = 10
            number[j + 1] = 10
            number[j + 2] = 10
            number[j + 3] = 10
            # print("found 4")
        j += 1
    j = 0
    while j < (len(number) - 2):
        if number[j] == number[j + 1] and number[j + 1] == number[j + 2]:
            number[j]     = 10
            number[j + 1] = 10
            number[j + 2] = 10
            # print("found 3")
        j += 1
    j = 0
    found = False
    while j < (len(number) - 1):
        if number[j] == number[j + 1] and number[j] != 10:
            found = True
        j += 1
    if found == True:
        # print(number)
        # print("got it")
        print(i)
        count += 1
    i += 1
print(count)
