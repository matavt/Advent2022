# I left my brute force method here as some advice said to try it but mine isn't very fast
# and was going to take a couple of weeks on my laptop.

# the distress beacon must disance to nearest beacon +1 from a sensor
# calculated all points on this boundry.
# assuming its somewhere near the middle it will be this distance from the 4 nearest sensors.
# generate a list of possible point and test to make sure it is out of range of all beacons.
# if that doesn't solve it we can check edge conditions. eg. If it's in a corner it will only be near 1 beacon

from collections import Counter
def main():
    sensors = []
    dataIn = input().split(" ")
    while dataIn[0] != "end":
        sensor = (int(dataIn[2].split("=")[1].strip(",")),int(dataIn[3].split("=")[1].strip(":")))
        beacon = (int(dataIn[8].split("=")[1].strip(",")),int(dataIn[9].split("=")[1]))
        distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        sensors.append((sensor[0],sensor[1],distance))
        dataIn = input().split(" ")
    
    distress = []
    for sensor in sensors:
        disRange = sensor[2] +1
        distress.append((sensor[0]-disRange,sensor[1]))
        distress.append((sensor[0]+disRange,sensor[1]))
        distress.append((sensor[0],sensor[1]-disRange))
        distress.append((sensor[0],sensor[1]+disRange))
        for i in range(1,disRange):
            xa = sensor[0] + i
            xb = sensor[0] - i
            ya = sensor[1] - disRange + i
            yb = sensor[1] + disRange - i
            distress.append((xa,ya))
            distress.append((xa,yb))
            distress.append((xb,ya))
            distress.append((xb,yb))

    counts = Counter(distress)
    print(counts)

    # for y in range(-40,40):
    #     for x in range(-40,40):
    #         if (x,y) in distress:
    #             print(counts[(x,y)],end="")
    #         else:
    #             print(" ",end="")
    #     print()
    






def BruteForce():
    sensors = []
    dataIn = input().split(" ")
    while dataIn[0] != "end":
        sensor = (int(dataIn[2].split("=")[1].strip(",")),int(dataIn[3].split("=")[1].strip(":")))
        beacon = (int(dataIn[8].split("=")[1].strip(",")),int(dataIn[9].split("=")[1]))
        distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        sensors.append((sensor[0],sensor[1],distance))
        dataIn = input().split(" ")
    
    point = [0,0]
    for i in range(4000001):
        print("row: "+ str(i))
        inRange = False
        for j in range(4000001):
            inRange = False
            for sensor in sensors:
                if abs(sensor[0]-i) + abs(sensor[1]-j)<=sensor[2]:
                    inRange = True
                    break
            if not inRange:
                point = [i,j]
                break
        if not inRange:
            break
    print(point[0]*4000000 + point[1])


if __name__ == ("__main__"):
    main()