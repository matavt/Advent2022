def main():
    global forest
    forest = []
    loop = True
    lineNum = 0
    while loop:
        dataIn = input()
        if dataIn == "end":
            loop = False
        else:
            forest.append([])
            for tree in dataIn:
                forest[lineNum].append(int(tree))
        lineNum += 1
    
    global width
    width = len(forest)
    global height
    height = len(forest[0])
    visCount = 0
    for i in range(width):
        for j in range(height):
            if checkVis(i,j):
                visCount += 1
    
    print(visCount)

def checkVis(x,y):
    #check left
    global forest
    global width
    global height

    if x == 0 or y == 0:
        return True
    
    if x == width-1 or y == height-1:
        return True
    
    vis = True
    for i in range(x-1,0,-1):
        print(i)
        if forest[x][y] <= forest[i][y]:
            vis == False
            break
    if vis:
        return True
    
    return False
    
    

if __name__ == ("__main__"):
    main()