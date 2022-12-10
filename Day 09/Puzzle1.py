def main():
    loop = True 
    headPos = (0,0)
    tailPos = (0,0)
    visited = {}
    visited[str(headPos)] = True
    while loop:
        dataIn = input()
        if dataIn == "end":
            loop = False
        else:
            dataIn = dataIn.split(" ")

            if dataIn[0] == "U":
                for i in range(int(dataIn[1])): 
                    currentHeadPos = headPos
                    headPos = (headPos[0],headPos[1] - 1)
                    if not testAdj(headPos,tailPos):
                        tailPos = currentHeadPos
                        visited[str(tailPos)] = True
                        
            if dataIn[0] == "D":
                for i in range(int(dataIn[1])): 
                    currentHeadPos = headPos
                    headPos = (headPos[0],headPos[1] + 1)
                    if not testAdj(headPos,tailPos):
                        tailPos = currentHeadPos
                        visited[str(tailPos)] = True

            if dataIn[0] == "L":
                for i in range(int(dataIn[1])): 
                    currentHeadPos = headPos
                    headPos = (headPos[0] - 1,headPos[1])
                    if not testAdj(headPos,tailPos):
                        tailPos = currentHeadPos
                        visited[str(tailPos)] = True
                    
            if dataIn[0] == "R":
                for i in range(int(dataIn[1])): 
                    currentHeadPos = headPos
                    headPos = (headPos[0] + 1,headPos[1])
                    if not testAdj(headPos,tailPos):
                        tailPos = currentHeadPos
                        visited[str(tailPos)] = True
    print(len(visited))

def testAdj(headPos, tailPos):
    vertDif = headPos[1] - tailPos[1]
    horzDif = headPos[0] - tailPos[0]
    if (vertDif in range(-1,2)) and  (horzDif in range(-1,2)):
        return True
    return False

if __name__ == ("__main__"):
    main()