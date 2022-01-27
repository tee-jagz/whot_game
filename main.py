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

    def remainingCards(self):
        return len(self.deck)

    def show(self):
        for card in self.deck:
            print(card.cardDisplay())


# Create a hand class for each player
class hand:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.isSkip = False

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

    def skip(self, isSkip = True):
        self.isSkip = isSkip

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
            player.getCard(4)
        stage.addCard(deck.give())

    def punish(self, player):
        player.getCard(stage.getStage().cardAction())

    def checkDeck(self, players):
        if deck.remainingCards() < 1:
            temp = {}
            for player in players:
                temp[player.name] = player.liability()
                print(f"{player.name} : {player.liability()}", end = ' | ')
                
            k = list(temp.values())
            winValInd = k.index(min(k))
            winner = list(temp.keys())[winValInd]
            print(f"\n{winner} won!\n\n")
            return True

    def play(self):
        count = 0
        while True:
            turn = count % len(self.players)
            next = (turn+1) % len(self.players)

            if turn == 0:
                self.players[turn].show()
            
            if self.players[turn].isSkip:
                count += 1
                continue

            #self.players[turn].show()
            stage.show()
            print(f"\n{self.players[next].name} : {self.players[next].remainingCards()} card(s) left")
            print(f"Deck : {deck.remainingCards()}\n{'_'*20}")
            if turn == 0:
                while True:
                    pick = input('Which card will you like to play: ')
                    
                    if (pick.isdigit() == False) or (int(pick) > len(self.players[turn].hand) and int(pick) != 100):
                        print('Enter the index of card you want to play or "100" to pick a card.')
                        continue
                    elif int(pick) == 100:
                        self.players[(turn+1) % len(self.players)].skip(False)
                        break
                    else:
                        if self.players[turn].checkStage(self.players[turn].hand[int(pick)], stage.getStage()) == False:
                            print('Select a card that matches shape or number or "100" to pick a card.')
                            continue
                        break
                
                if int(pick) == 100:
                    self.players[turn].getCard(1)
                else:
                    self.players[turn].playCard(int(pick))
                    if stage.getStage().isAction() == True:
                        self.players[(turn+1) % len(self.players)].skip()
                        self.punish(self.players[next])
                    else:
                        self.players[next].skip(False)
            
            else:
                c = 0
                while True:
                    pick = random.randint(0, self.players[turn].remainingCards()-1)

                    if self.players[turn].checkStage(self.players[turn].hand[int(pick)], stage.getStage()) == False:
                        # print(f'{pick} Computer dey select rubbish lowo.')
                        c += 1
                        if c == 14:
                            self.players[turn].getCard(1)
                            self.players[next].skip(False)

                            break
                        continue
                    else:
                        self.players[turn].playCard(pick)
                        if stage.getStage().isAction():
                            self.players[next].skip()
                            self.punish(self.players[next])
                        else:
                            self.players[next].skip(False)
                        break
            if self.checkDeck(self.players):
                break
            if self.players[turn].remainingCards() < 1:
                print(f'{self.players[turn].name} won!')
                break
            else:
                count +=1


stage = stage()
deck = deck()
engine = engine(2)    

print(f'{"-"*100}\nWelcome to the game of WORT!\n{"-"*70}\n')

engine.startGame()
engine.play()
