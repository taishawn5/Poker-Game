from deck import *
from players import *

deck = Deck()
deck.shuffle()

bob = Player("Bob")
bob.draw(deck).draw(deck)
bob.showHand()

