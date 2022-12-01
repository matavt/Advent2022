def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
        
def lParser():
    while 1:
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)
                
line_parser = lParser()

def get_line():
    global line_parser
    return next(line_parser)

def main():
    return

if __name__ == ("__main__"):
    main()