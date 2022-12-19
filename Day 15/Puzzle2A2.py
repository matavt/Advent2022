# technically attempt 3 brute forcing using technique from puzzle 1 solution.

def main():
    sensors = []
    dataIn = input().split(" ")
    sensor = (int(dataIn[2].split("=")[1].strip(",")),int(dataIn[3].split("=")[1].strip(":")))
    xEndPoint = [sensor[0],sensor[0]]
    yEndPoint = [sensor[1],sensor[1]]

    while dataIn[0] != "end":
        sensor = (int(dataIn[2].split("=")[1].strip(",")),int(dataIn[3].split("=")[1].strip(":")))
        beacon = (int(dataIn[8].split("=")[1].strip(",")),int(dataIn[9].split("=")[1]))
        distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        sensors.append((sensor[0],sensor[1],distance))
        if sensor[0]<xEndPoint[0]:
            xEndPoint[0] = sensor[0]
        if sensor[0]>xEndPoint[1]:
            xEndPoint[1] = sensor[0]
        if sensor[1]<yEndPoint[0]:
            yEndPoint[0] = sensor[1]
        if sensor[1]<yEndPoint[1]:
            yEndPoint[1] = sensor[1]        
        dataIn = input().split(" ")





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