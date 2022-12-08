class Directory:    
    def __init__(self, name=""):
        self.name = name
        self.parent = ""
        self.children = []
        self.files = {}
    
    def contentSize(self):
        fileSize = 0
        for key in self.files:
            fileSize += self.files[key]
        for child in self.children:
            fileSize += child.contentSize()
        return fileSize

def main():
    directoryList = {"/":Directory("/")}
    current = "/"
    loop = True
    while loop:
        inData = input().split(" ")

        if inData[0] == "end":
            loop = False
        elif inData[0] == "$":
            if inData[1] == "cd":
                if inData[2] == "/":
                    current = "/"
                elif inData[2] == "..":
                    current = current[:-len(directoryList[current].name)]
                else:
                    current += inData[2]

        elif inData[0] == "dir":
            newDir = current + inData[1]
            directoryList[newDir] = Directory(inData[1])
            directoryList[current].children.append(directoryList[newDir])
            directoryList[newDir].parent = current
        else:
            directoryList[current].files[inData[1]] = int(inData[0])

    totalSize = 0
    for key in directoryList:
        fileSizes = directoryList[key].contentSize()
        if fileSizes <100000:
            totalSize += fileSizes
    
    print(totalSize)

if __name__ == ("__main__"):
    main()