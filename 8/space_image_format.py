#!/usr/bin/env python3

pixels = 25
column = 6
layers = 0
input  = []

def readInput():
    global input
    global pixels
    global column
    global layers
    file = open("input", "r")
    line = file.readline()
    file.close()
    temp = []
    for i in range(len(line) - 1):
        temp.append(int(line[i]))
    # print(line)
    layers = int(len(line) / (pixels * column))
    # print(line)
    for i in range(layers):
        start = i * pixels * column
        end   = (i+1) * pixels * column
        input.append(temp[start:end])
    print(input)

def fewestZeros():
    global input
    global pixels
    global column
    global layers
    fewest_i     = 0
    fewest_count = 150
    for i in range(len(input)):
        count = 0
        for j in range(len(input[i])):
            if (input[i][j] % 10) == 0:
                count += 1
        if count < fewest_count:
            fewest_i     = i
            fewest_count = count
            # print("fewest_i " + str(fewest_i))
            # print("fewest_count " + str(fewest_count))
    # print(input[fewest_i])
    count_one = 0
    count_two = 0
    for j in range(len(input[fewest_i])):
        if input[fewest_i][j] % 10 == 1:
            count_one += 1
    for j in range(len(input[fewest_i])):
        if input[fewest_i][j] % 10 == 2:
            count_two += 1
    # print(count_two * count_one)

def getImage():
    global input
    global pixels
    global column
    global layers
    image = []
    # print(layers)
    # print(pixels*column)
    file = open("out", "w")
    for i in range(pixels*column):
        for j in range(layers):
            print(input[j][i])
            if input[j][i] != 2:
                if (i % pixels) == 0:
                    file.write('\n')
                if input[j][i] == 0:
                    file.write(' ')
                else:
                    file.write(str(input[j][i]))
                image.append(input[j][i])
                print("break")
                break
    file.close()
    print(image)
    print(len(image))

def main():
    readInput()
    fewestZeros()
    getImage()

if __name__ == "__main__":
    main()
