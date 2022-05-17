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
    def __init__(self):
        self.tail = None
        self.amt_players = 6

    def create_table(players):
        for i in range(self.amt_players):
            if self.list_is_empty():
                new_node = Node(players[i])
                self.tail = new_node
            else:
                new_node = Node(players[i])
                new_node.next = self.tail.next
                self.tail.next = new_node

    def show_table():
        if self.tail == None:
            print("The table is empty")
        temp = self.tail.next
        while temp is not self.tail:
            print(temp.player.name)
            temp = temp.next