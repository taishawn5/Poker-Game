from deck import *
from players import *

# deck = Deck()
# deck.shuffle()

# bob = Player("Bob")
# bob.draw(deck).draw(deck)
# bob.showHand()

deck = Deck()
deck.shuffle()

bob = Player("Bob")
tai = Player("Tai")
han = Player("Han")
soph = Player("Soph")
luke = Player("Luke")
kon = Player("Kon")

names = [bob,tai,han,soph,luke,kon]
table = Table(names)
table.create_table(names)
table.deal_cards(deck)
table.show_table()




