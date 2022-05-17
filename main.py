from deck import *
from players import *

# deck = Deck()
# deck.shuffle()

# bob = Player("Bob")
# bob.draw(deck).draw(deck)
# bob.showHand()
bob = Player("Bob")
tai = Player("Tai")
han = Player("Han")
soph = Player("Soph")
luke = Player("Luke")
kon = Player("Kon")

names = [bob,tai,han,soph,luke,kon]
table = Table(names)
table.create_table(names)
table.show_table()




