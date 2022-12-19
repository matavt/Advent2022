def main():
    dataIn = input().split(" ")
    line = {}
    targetline = 2000000
    beaconsInTarget = {}
    while dataIn[0] != "end":
        sensor = (int(dataIn[2].split("=")[1].strip(",")),int(dataIn[3].split("=")[1].strip(":")))
        beacon = (int(dataIn[8].split("=")[1].strip(",")),int(dataIn[9].split("=")[1]))
        if beacon[1] == targetline:
            beaconsInTarget[beacon[0]] = True
        distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        distFromTarget = abs(sensor[1] - targetline)
        offset = distance - distFromTarget
        dataIn = input().split(" ")
        if offset >= 0:
            for i in range (-offset,offset+1):
                line[sensor[0] + i] = True
    
    print(len(line)-len(beaconsInTarget))

if __name__ == ("__main__"):
    main()