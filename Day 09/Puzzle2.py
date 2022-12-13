def main():
    positions = [[0,0] for i in range(10)]
    visited = {}


    readIn = input()
    while readIn != "end":
        dataIn = readIn.split(" ")
        if dataIn[0] == "U":
            for i in range(int(dataIn[1])):
                positions[0] = [positions[0][0],positions[0][1] -1]
                for i in range(1,10):
                    positions[i] = moveTail(positions[i-1],positions[i])
                    
        if dataIn[0] == "D":
            for i in range(int(dataIn[1])): 
                positions[0] = [positions[0][0],positions[0][1] + 1]
                for i in range(1,10):
                    positions[i] = moveTail(positions[i-1],positions[i])

        if dataIn[0] == "L":
            for i in range(int(dataIn[1])): 
                positions[0] = [positions[0][0] - 1,positions[0][1]]      
                for i in range(1,10):
                    positions[i] = moveTail(positions[i-1],positions[i])
                
        if dataIn[0] == "R":

            for i in range(int(dataIn[1])):
                positions[0] = [positions[0][0] + 1,positions[0][1]]
                for i in range(1,10):
                    positions[i] = moveTail(positions[i-1],positions[i])
                visited[str(positions[9])] = True
        print(positions)
        readIn = input()
    print(positions)
    print(visited)    
    print(len(visited))

def moveTail(headPos, tailPos):
    newPos = tailPos.copy()
    diff = (headPos[0] - tailPos[0],headPos[1] - tailPos[1])
    if diff == (2,2):
        newPos = [newPos[0]+1,newPos[1]+1]
    elif diff == (2,1):
        newPos = [newPos[0]+1,newPos[1]+1]
    elif diff == (2,0):
        newPos = [newPos[0]+1,newPos[1]]
    elif diff == (2,-1):
        newPos = [newPos[0]+1,newPos[1]-1]
    elif diff == (2,-2):
        newPos = [newPos[0]+1,newPos[1]-1]
    elif diff == (1,2):
        newPos = [newPos[0]+1,newPos[1]+1]
    elif diff == (1,-2):
        newPos = [newPos[0]+1,newPos[1]-1]
    elif diff == (0,2):
        newPos = [newPos[0],newPos[1]+1]
    elif diff == (0,-2):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-1,2):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-1,-2):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-2,2):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-2,1):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-2,0):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-2,-1):
        newPos = [newPos[0],newPos[1]]
    elif diff == (-2,-2):
        newPos = [newPos[0],newPos[1]]


    return newPos

if __name__ == ("__main__"):
    main()