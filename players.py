from deck import *

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.draw())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()
    def discard(self):
        return self.hand.pop()

class Table():
    def __init__(self, amt_players):
        self.amt_players = amt_players
    
    def create_table():
        pass