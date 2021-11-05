from Card import Card
from Suit import Suit
import random

class Deck:
    def __init__(self):
        values = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "jack",
            "queen",
            "king",
            "ace",
        ]

        self.Cards = []

        for suit in Suit:
            for value in values:
                self.Cards.append(Card(suit, value))
    
    def DealCard(self):
        card = random.choice(self.Cards)
        self.Cards.remove(card)
        return card
