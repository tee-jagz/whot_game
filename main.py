import random

class card:
    def __init__(self, num, shape):
        self.num = num
        self.shape = shape


    def isAction(self):
        if self.num in [0,2,5,14]:
            return True
        else:
            return False


    def cardAction(self):
        if self.isAction():
            if self.num == 0:
                return 0
            elif self.num == 2:
                return 2
            elif self.num == 5:
                return 3
            elif self.num == 14:
                return 1
    
    
    def cardDisplay(self):
        return f'{self.num} : {self.shape}'

    def value(self):
        if self.isAction():
            return self.num+5
        else:
            return self.num

    
class deck:
    def __init__ (self):
        self.deck = []
        for shape in ['Circle', 'Square', 'Triangle']:
            for num in range(15):
                self.deck.append(card(num, shape))
    
    def shuffle(self):
        return random.shuffle(self.deck)

    def give(self):
        return self.deck.pop()

    def show(self):
        for card in self.deck:
            print(card.cardDisplay())


class hand:
    def __init__(self):
        self.hand = []

    def getCard(self, num):
        for i in range(num):
            self.hand.append(deck.give())

    def checkStage(self, card, stage):
        if (card.num == stage.num) or (card.shape == stage.shape):
            return True

    def playCard(self, ind):
        if self.checkStage(ind, stage.getStage()):
            self.hand.pop(ind)
        else:
            print('Ko work!')
    
    def show(self):
        for card in self.hand:
            print(card.cardDisplay())


class stage:
    def __init__(self):
        self.stage = []

    def getStage(self):
        return self.stage(-1)

    


deck = deck()
hand = hand()

hand.getCard(2)
hand.show()