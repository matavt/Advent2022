def main():
    cycle = 0
    signal = 1
    totalStrength = 0.
    checks = [20,60,100,140,180,220]
    checkpoints = []

    line = input()
    while line != "end":
        command = line.split(" ")
        if command[0] == "noop":
            cycle += 1
            if cycle in checks:
                checkpoints.append((cycle,signal))
                totalStrength += cycle*signal
        if command[0] == "addx":
            cycle += 1
            if cycle in checks:
                checkpoints.append((cycle,signal))
                totalStrength += cycle*signal
            cycle += 1
            if cycle in checks:
                checkpoints.append((cycle,signal))
                totalStrength += cycle*signal
            signal += int(command[1])        
        line = input()

    print(checkpoints)
    print(totalStrength)

if __name__ == ("__main__"):
    main()