import random


class CreateRandomList:
    def __init__(self, length):
        self.randomList = []
        self.length = length
        for _ in range(length):
            self.addNumber(length)

    def addNumber(self, length):
        i = random.randint(1, length)
        if i in self.randomList:
            self.addNumber(length)
        else:
            self.randomList.append(i)
