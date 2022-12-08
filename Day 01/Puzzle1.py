def main():
    large = 0
    current = 0
    loop = True
    while loop:
        inVal = input()
        if inVal == "end":
            loop = False
        elif inVal == "":
            current = 0
        else:
            current += int(inVal)
            if current>large:
                large = current
    print(large)

if __name__ == ("__main__"):
    main()