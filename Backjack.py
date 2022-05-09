import random
class Card():
    def __init__(self,suit,value,calculatedvalue):
        self.suit = suit
        self.value = value
        self.calculatedvalue = calculatedvalue
    def show(self):
        print(f'{self.suit} of {self.value} with value {self.calculatedvalue}')

class Deck():
    def __init__(self):
        self.cards =[]
        self.build()

    def __len__(self):
        x= len(self.cards)
        print(f'the size of deck is {x}')
        return x

    def build(self):
        calculatedvalue=0
        for s in ['spade','heart','diamond','club']:
            for v in range (1,14):
                if v<10:
                    calculatedvalue = v
                else:
                    calculatedvalue=10
                self.cards.append(Card(s, v, calculatedvalue))

    def show(self):
        for c in self.cards:
            c.show()

    def Shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r]= self.cards[r], self.cards[i]

    def drawcard(self):
        return self.cards.pop()

class Player():
    def __init__(self):
        self.hand = []
        self.name=""

    def Playername(self):
        self.name=input('Player-Please enter your name: \n')
        print(f'Player created {self.name}')
        return self.name

    def placeBet(self):
        bet = input("How much bet would you like to  place: \n")
        return bet

    def draw(self, deck):
        y=len(deck)
        for i in range(y-2, y):
            self.hand.append(deck.drawcard())
        return self.hand

    def drawone(self,deck):
        y=len(deck)
        for i in range(y-1,y):
            self.hand.append(deck.drawcard())
        return self.hand

    def showhand(self):
        for c in self.hand:
            c.show()

    def totalhandvalue(self):
        total = 0
        flag = False
        for c in self.hand:
            if c.value == 1:
                flag = True
            total = total+c.calculatedvalue
        if total <= 10 and flag == True:
            total += 10
        return total

    def __len__(self):
        x= len(self.hand)
        print(f'the size of {self.name}\'s deck is {x}')
        return x

class dealer():
    def __init__(self, dealer):
        self.dealer = dealer
        print('Dealer is playing right now')
        self.dealerHand = []

    def dealerdraw(self, deck):
        y=len(deck)
        for i in range(y-2, y):
            self.dealerHand.append(deck.drawcard())

    def dealerdrawone(self,deck):
        y=len(deck)
        for i in range(y-1,y):
            self.dealerHand.append(deck.drawcard())
        return self.dealerHand

    def showdealer(self):
        oneShowCard = self.dealerHand[0]
        oneShowCard.show()
        hiddenCard = self.dealerHand[1]

    def totalhandvalue(self):
        total = 0
        flag = False
        for c in self.dealerHand:
            if c.value == 1:
                flag = True
            total = total+c.calculatedvalue
        if total <= 10 and flag == True:
            total += 10
        return total

    def __len__(self):
        x = len(self.dealerHand)
        print(f'the size of {self.dealer}\'s deck is {x}')
        return x

class Bet():
    def __init__(self, bet):
        self.bet = bet
        self.chips=[1]*10

    def totalChips(self):
        sum=0
        for totalchips in self.chips:
            sum += totalchips
        print("after running for loop")
        #print(f"value of total chips is {totalchips.__int__()}")
        total = sum-int(self.bet)
        if total<0:
            print("you placed a bet larger than available chips")
        else:
            print(f"remaining chips are {total} ")

























