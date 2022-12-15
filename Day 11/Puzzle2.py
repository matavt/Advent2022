def main():
    monkeys = []
    dataIn = input()

    while dataIn != "end":
        monkeys.append(Monkey())
        dataIn = input().split(" ")
        for i in range(4,len(dataIn)):
            item = dataIn[i].strip(",")
            monkeys[-1].setItems(int(item))
        dataIn = input().split(" ")
        if dataIn[6] == "+":
            monkeys[-1].setOpType(dataIn[6],dataIn[7])
        if dataIn[6] == "*":
            if dataIn[7] == "old":
                monkeys[-1].setOpType("^",0)
            else:
                monkeys[-1].setOpType(dataIn[6],dataIn[7])
        dataIn = input().split(" ")
        monkeys[-1].setTest(dataIn[5])
        dataIn = input().split(" ")
        monkeys[-1].setMonkeyTrue(dataIn[9])
        dataIn = input().split(" ")
        monkeys[-1].setMonkeyFalse(dataIn[9])
        dataIn = input()
        dataIn = input()

    mod = 1
    for monkey in monkeys:
        if mod%monkey.testValue != 0:
            mod = mod * monkey.testValue
    for monkey in monkeys:
        monkey.setMod(mod)


    for i in range(10000):
        for monkey in monkeys:
            passList = monkey.throw()
            for item in passList:
                monkeys[item[0]].setItems(item[1])

    highestValue = 0
    secondHighestValue = 0
    for monkey in monkeys:
        value = monkey.inspected
        if value > highestValue:
            secondHighestValue = highestValue
            highestValue = value
        elif value > secondHighestValue:
            secondHighestValue = value
    
    print(highestValue * secondHighestValue)
    
class Monkey:
    def __init__(self):
        self.items = []
        self.inspected = 0
        self.testValue = 1
        self.monkeyFalse = 0
        self.monkeyTrue = 0
        self.opType = "+"
        self.opValue = "0"
        self.mod = 1
    
    def setItems(self,item):
        self.items.append(item)
    
    def setTest(self, value):
        self.testValue = int(value)

    def setMonkeyTrue(self, id):
        self.monkeyTrue = int(id)
    
    def setMonkeyFalse(self, id):
        self.monkeyFalse = int(id)

    def setOpType(self,type,value):
        self.opType = type
        self.opValue = int(value)

    def setMod(self, mod):
        self.mod = mod

    def operation(self,item):
        if self.opType == "*":
            item = item * self.opValue
        if self.opType == "+":
            item = item + self.opValue
        if self.opType == "^":
            item = item * item
        item = item%self.mod
        return item

    def test(self, item):
        if item%self.testValue == 0:
            return self.monkeyTrue
        return self.monkeyFalse

    def throw(self):
        passList = []
        for item in self.items:
            self.inspected += 1
            item = self.operation(item)
            monkey = self.test(item)
            passList.append((monkey,item))
        self.items = []
        return passList  

if __name__ == ("__main__"):
    main()