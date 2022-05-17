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

table = Table()
table.create_table([bob,tai,han,soph,luke,kon])
table.show_table()




