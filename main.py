import random


# Create a card class
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
        return f'[{self.num}:{self.shape}]'

    def value(self):
        if self.isAction():
            return self.num+5
        else:
            return self.num


# Create a deck class
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


# Create a hand class for each player
class hand:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def getCard(self, num):
        for i in range(num):
            self.hand.append(deck.give())

    def checkStage(self, card, stage):
        if (card.num == stage.num) or (card.shape == stage.shape):
            return True
        else:
            return False

    def playCard(self, ind):
        stage.addCard(self.hand.pop(ind))
        

    def remainingCards(self):
        return len(self.hand)
    
    def show(self):
        print(f'{self.name}:')
        for ind,  card in enumerate(self.hand):
            print(f'({ind}):{card.cardDisplay()}', end=' | ')
        print('\n')

    def skip(self, isSkip = False):
        return isSkip

    def liability(self):
        temp = 0
        for card in self.hand:
            temp += card.value()
        return temp


class stage:
    def __init__(self):
        self.stage = []

    def getStage(self):
        return self.stage[-1]

    def addCard(self, card):
        self.stage.append(card)

    def show(self):
        temp = '+              +\n'*2
        print(f" {'+'*14}")
        print(f"{temp} {self.stage[-1].cardDisplay()}")
        print(f"{temp} {'+'*14}")


class engine:
    def __init__(self, players):
        self.players = []
        for player in range(players):
            self.players.append(hand(f'Player {player+1}'))

    def startGame(self):
        deck.shuffle()
        for player in self.players:
            player.getCard(8)
        stage.addCard(deck.give())

    def play(self):
        turn = 0
        while True:
            print('Turn :', turn)
            if turn == 0:
                self.players[turn].show()
            stage.show()
            if turn == 0:
                while True:
                    pick = input('Which card will you like to play: ')
                    if (pick.isdigit() == False) or (int(pick) > len(self.players[turn].hand) and int(pick) != 100):
                        print('Enter the index of card you want to play or "100" to pick a card.')
                        continue
                    else:
                        if self.players[turn].checkStage(self.players[turn].hand[int(pick)], stage.getStage()) == False:
                            print('Select a card that matches shape or number or "100" to pick a card.')
                            continue
                        break
                self.players[turn].playCard(int(pick))
            else:
                c = 0
                while True:
                    pick = random.randint(0, self.players[turn].remainingCards()-1)

                    if self.players[turn].checkStage(self.players[turn].hand[int(pick)], stage.getStage()) == False:
                        print(f'{pick} Computer dey select rubbish lowo.')
                        c += 1
                        if c == 14:
                            self.players[turn].show()
                            break
                        continue
                    else:
                        self.players[turn].playCard(pick)
                        break
                    
            if self.players[turn].remainingCards() < 1:
                print('Game finished!')
                break
            else:
                print('Turn: ', turn)
                if turn == (len(self.players)-1):
                    turn = 0
                else:
                    turn += 1

            
                




stage = stage()
deck = deck()
engine = engine(2)    

# pHand = hand('Player 1')
# cHand = hand('AI 1')
# stage.addCard(deck.give())
print(f'{"-"*100}\nWelcome to the game of WORT!\n{"-"*70}\n')
# while True:
#     pHand.getCard(4)
#     cHand.getCard(4)

engine.startGame()
engine.play()
