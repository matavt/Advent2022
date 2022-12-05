def main():
    loop = True
    count = 0

    while loop:
        inputs = input()
        if inputs == "end":
            loop = False
        else:
            pairs = inputs.split(",")
            pair1 = pairs[0].split("-")
            pair2 = pairs[1].split("-")            
            firstSet = []
            secondSet = []
            for i in range(int(pair1[0]),int(pair1[1])+1):
                firstSet.append(i)
            for i in range(int(pair2[0]),int(pair2[1])+1):
                secondSet.append(i)         
            insec = set(firstSet).intersection(set(secondSet))
            if (len(insec) == len(secondSet)) or (len(insec) == len(firstSet)):
                count += 1
    print(count)

if __name__ == ("__main__"):
    main()