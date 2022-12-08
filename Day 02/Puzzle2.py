def main(): 
    result = {"A X":3,
        "A Y":4,
        "A Z":8,
        "B X":1,
        "B Y":5,
        "B Z":9,
        "C X":2,
        "C Y":6,
        "C Z":7}
    loop = True
    score = 0
    
    while loop:
        game = input()
        if game == "end":
            loop = False
        else:
            score += result[game]
    print(score)   

if __name__ == ("__main__"):
    main()