#!/usr/bin/env python3

list = [
    "space law space brochure",
    "fixed point",
    "candy cane",
    "sand",
    "ornament",
    "fuel cell",
    "wreath"
]

res = []

for a in range(len(list)):
    for b in range(len(list)):
        if b == a:
            continue
        for c in range(len(list)):
            if c == b or c == a:
                continue
            temp = sorted([list[a], list[b], list[c]])
            if temp not in res:
                res.append(temp)

        temp = sorted([list[a], list[b]])
        if temp not in res:
            res.append(temp)
    temp = sorted([list[a]])
    if temp not in res:
        res.append(temp)


for entry in res:
    cpy_entry = entry.copy()
    for i in range(len(entry)):
        entry[i] = 'take ' + entry[i]
    for i in range(len(cpy_entry)):
        cpy_entry[i] = 'drop ' + cpy_entry[i]
    entry.append("west")
    entry += cpy_entry

# print(res)

file = open("cmd2", "w+")
for entry in res:
    for string in entry:
        file.write(string + '\n')
