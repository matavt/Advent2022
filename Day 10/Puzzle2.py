def main():
    xReg = 1
    display = Display()

    line = input()
    while line != "end":

        command = line.split(" ")
        if command[0] == "noop":
            display.drawPixels(xReg)
        if command[0] == "addx":
            display.drawPixels(xReg)
            display.drawPixels(xReg)
            xReg += int(command[1])     
        line = input()
    display.createImage()


class Display:
    def __init__(self):
        self.pixels = [["."for i in range(40)]for j in range(6)]
        self.currentPixel = 0

    def drawPixels(self,position):
        rowCol = divmod(self.currentPixel,40)
        if abs(position - rowCol[1]) <=1:
            self.pixels[rowCol[0]][rowCol[1]] = "#"
        self.currentPixel += 1

    def createImage(self):
        for i in range(6):
            for j in range(40):
                print(self.pixels[i][j],end="")
            print("")


if __name__ == ("__main__"):
    main()