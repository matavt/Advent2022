def main():
    dataSet = input()
    check = 4
    i = check
    while i < len(dataSet):
        dataList = []
        for j in range(i-check,i):
            dataList.append(dataSet[j])
        if len(dataList) == len(set(dataList)):
            print(i)
            i = len(dataSet)
        i += 1
if __name__ == ("__main__"):
    main()