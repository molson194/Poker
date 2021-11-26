from Card import Card
from Suit import Suit
import random

class Deck:
    Values = {
        "2": 13,
        "3": 12,
        "4": 11,
        "5": 10,
        "6": 9,
        "7": 9,
        "8": 7,
        "9": 6,
        "10": 5,
        "jack": 4,
        "queen": 3,
        "king": 2,
        "ace": 1,
    }

    def __init__(self):
        self.Cards = []

        for suit in Suit:
            for value in Deck.Values.keys():
                self.Cards.append(Card(suit, value))
    
    def DealCard(self):
        card = random.choice(self.Cards)
        self.Cards.remove(card)
        return card


    @staticmethod
    def RankValue(val1, val2):
        if val2 == None:
            return Deck.Values[val1] # Unique value for hands that involve single high-cards
        
        return Deck.Values[val1] * 14 + Deck.Values[val2] # Unique value for hands that involve two high-cards (i.e. full houses and two pair)