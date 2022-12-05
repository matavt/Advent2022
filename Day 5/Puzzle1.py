def main():
    loop = True
    stacks = []
    stacks = [[] for i in range(9)]

    while loop:
        inData = input()
        if inData[1] == "1":
            loop = False
        else:
            for i in range(1, 34 ,4):
                index = (int(i/4))
                if(inData[i] != " "):
                    stacks[index].append(inData[i])
    for i in range(len(stacks)):
        stacks[i].reverse()
    inData = input()
    loop = True
    while loop:
        inData = input()
        if inData == "end":
            loop = False
        else:
            data = inData.split(" ")
            numMove = int(data[1])
            startMove = int(data[3]) - 1
            endMove = int(data[5]) - 1

            for i in range(numMove):
                stacks[endMove].append(stacks[startMove].pop())
    output = ""
    for i in range(9):
        output += stacks[i].pop()
    print(output)

if __name__ == ("__main__"):
    main()