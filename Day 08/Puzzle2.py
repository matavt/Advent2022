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
    maxView = 0
    for i in range(1,width-1):
        for j in range(1,height-1):
            viewDist = checkVis(i,j)
            if viewDist > maxView:
                maxView = viewDist
    
    print(maxView)

def checkVis(y,x):

    global forest
    global width
    global height
    
    #check left
    left = 0
    i =  x-1
    while i > -1:
        left += 1
        if forest[y][x] <= forest[y][i]:
            i = -1
        i -= 1

    #check right
    right = 0
    i = x+1
    while i < width:
        right += 1
        if forest[y][x] <= forest[y][i]:
            i = width
        i += 1
    
    #check up    
    up = 0
    i = y - 1
    while i > -1:
        up += 1
        if forest[y][x] <= forest[i][x]:
            i = -1
        i -= 1
    
    #check down
    down = 0
    i = y + 1
    while i < height:
        down += 1
        if forest[y][x] <= forest[i][x]:
            i = height
        i += 1

    return left * right * up * down
    
    

if __name__ == ("__main__"):
    main()