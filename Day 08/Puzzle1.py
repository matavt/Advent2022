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
    visCount = (width + height -2) * 2
    for i in range(1,width-1):
        for j in range(1,height-1):
            if checkVis(i,j):
                visCount += 1
    
    print(visCount)

def checkVis(y,x):

    global forest
    global width
    global height
    
    #check left
    vis = True
    for i in range(x-1,-1,-1):
        if forest[y][x] <= forest[y][i]:
            vis = False
            i = -1
    if vis:
        return True
    
    #check right
    vis = True
    for i in range(x+1,width):
        if forest[y][x] <= forest[y][i]:
            vis = False
            i = width
    if vis:
        return True
        
    #check up    
    vis = True
    for i in range(y-1,-1,-1):
        if forest[y][x] <= forest[i][x]:
            vis = False
            i = -2
    if vis:
        return True

    #check down
    vis = True
    for i in range(y+1,height):
        if forest[y][x] <= forest[i][x]:
            vis = False
            i = height + 1
    if vis:
        return True
    
    #can't be seen
    return False
    
    

if __name__ == ("__main__"):
    main()