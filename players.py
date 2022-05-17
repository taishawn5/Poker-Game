from multiprocessing.sharedctypes import Value
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

class Node:
    def __init__(self,player):
        self.player = player
        self.next = None

class Table:
    def __init__(self, names):
        self.tail = None
        self.amt_players = len(names)

    def create_table(self, the_players):
        for i in range(self.amt_players):
            if self.tail == None:
                new_node = Node(the_players[i])
                self.tail = new_node
                self.tail.next = new_node
            else:
                new_node = Node(the_players[i])
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node

    def deal_cards(self,deck):
        if self.tail == None:
            return print("There are no players to deal cards too")
        temp = self.tail.next
        i = 0
        while temp is not self.tail:
            temp.player.draw(deck).draw(deck)
        temp.player.draw(deck).draw(deck)


    def show_table(self):
        if self.tail == None:
            print("The table is empty")
        temp = self.tail.next
        while temp is not self.tail:
            print(temp.player.name + " " + temp.player.showHand())
            temp = temp.next
        print(temp.player.name + " " + temp.player.showHand())