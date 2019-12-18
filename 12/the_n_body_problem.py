#!/usr/bin/env python3

moons = []
init_moons = []
steps = 0
velocity = []
max_steps = 10
energy = []

def readInput():
    global moons
    global init_moons
    global velocity
    global energy
    file = open("input", "r")
    count = 0
    moons = []
    init_moons = []
    steps = 0
    velocity = []
    energy = []
    for line in file:
        temp = line.split(",")
        moons.append([count, int(temp[0][3:]), int(temp[1][3:]), int(temp[2][3:-2])])
        init_moons.append([count, int(temp[0][3:]), int(temp[1][3:]), int(temp[2][3:-2])])
        velocity.append([0, 0, 0])
        energy.append([-1, -1])
        count += 1
    file.close()

def printStep():
    global moons
    global velocity
    global steps
    print("After " + str(steps) + " steps")
    for i in range(len(moons)):
        print("pos=<" + str(moons[i][1]) + ", " + str(moons[i][2]) + ", " + str(moons[i][3]) + ", vel=<" + str(velocity[i][0]) + ", " + str(velocity[i][1]) + ", " + str(velocity[i][2]) + ">")
    print("")

def printEnergy():
    global steps
    global energy
    print("Energey after " + str(steps) + " steps")
    total = 0
    for i in range(len(energy)):
        total += energy[i][0] * energy[i][1]
        print("pot: " + str(energy[i][0]) + ", kin: " + str(energy[i][1]) + ", total: " + str(energy[i][0] * energy[i][1]))
    print("Sum of total energy: " + str(total) + "\n")

def applyVel():
    global moons
    global velocity
    global energy
    for i in range(len(moons)):
        moon = moons[i]
        for other_moon in moons:
            if moon[0] == other_moon[0]:
                continue

            if moon[1] > other_moon[1]:
                velocity[i][0] -= 1
            elif moon[1] < other_moon[1]:
                velocity[i][0] += 1

            if moon[2] > other_moon[2]:
                velocity[i][1] -= 1
            elif moon[2] < other_moon[2]:
                velocity[i][1] += 1

            if moon[3] > other_moon[3]:
                velocity[i][2] -= 1
            elif moon[3] < other_moon[3]:
                velocity[i][2] += 1
    for i in range(len(moons)):
        moons[i][1] += velocity[i][0]
        moons[i][2] += velocity[i][1]
        moons[i][3] += velocity[i][2]
        energy[i][0] = abs(moons[i][1]) + abs(moons[i][2]) +  abs(moons[i][3])
        energy[i][1] = abs(velocity[i][0]) + abs(velocity[i][1]) + abs(velocity[i][2])

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def doPhysics():
    global moons
    global init_moons
    global steps
    global velocity
    ## 1)
    # printStep()
    # steps += 1
    # while steps <= max_steps:
    #     applyVel()
    #     if __debug__: printStep()
    #     if __debug__: printEnergy()
    #     steps += 1
    ## 2)
    print("=================")
    steps = 1
    readInput()
    while True:
        applyVel()
        if init_moons[0][1] == moons[0][1] and init_moons[1][1] == moons[1][1] and init_moons[2][1] == moons[2][1] and init_moons[3][1] == moons[3][1] and velocity[0][0] == 0 and velocity[1][0] == 0 and velocity[2][0] == 0 and velocity[3][0] == 0:
            break
        steps += 1
    print(steps)
    x_prims = primes(steps)
    print("=================")
    steps = 1
    readInput()
    while True:
        applyVel()
        if init_moons[0][2] == moons[0][2] and init_moons[1][2] == moons[1][2] and init_moons[2][2] == moons[2][2] and init_moons[3][2] == moons[3][2] and velocity[0][1] == 0 and velocity[1][1] == 0 and velocity[2][1] == 0 and velocity[3][1] == 0:
            break
        steps += 1
    print(steps)
    y_prims = primes(steps)
    print("=================")
    steps = 1
    readInput()
    while True:
        applyVel()
        if init_moons[0][3] == moons[0][3]  and init_moons[3][3] == moons[3][3]  and init_moons[2][3] == moons[2][3]  and init_moons[3][3] == moons[3][3] and velocity[0][2] == 0 and velocity[1][2] == 0 and velocity[2][2] == 0 and velocity[3][2] == 0:
            break
        steps += 1
    print(steps)
    z_prims = primes(steps)
    print("=================")
    print("x_prims: " + str(x_prims))
    print("y_prims: " + str(y_prims))
    print("z_prims: " + str(z_prims))


def main():
    readInput()
    doPhysics()

if __name__ == "__main__":
    main()
