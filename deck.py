import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ["Spades","Clubs", "Diamonds", "Hearts"]:
            for i in range(1, 14):
               self.cards.append(Card(s,i))
    def show(self):
        for i in self.cards:
            i.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()