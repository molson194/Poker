from Card import Card
from Suit import Suit
import random

class Deck:
    def __init__(self):
        self.Cards = []

        for suit in Suit:
            for i in range(1, 14):
                self.Cards.append(Card(suit, i))
    
    def DealCard(self):
        card = random.choice(self.Cards)
        self.Cards.remove(card)
        return card
