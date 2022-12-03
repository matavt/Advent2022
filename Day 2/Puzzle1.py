def main(): 
    result = {"A X":4,
        "A Y":8,
        "A Z":3,
        "B X":1,
        "B Y":5,
        "B Z":9,
        "C X":7,
        "C Y":2,
        "C Z":6}
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