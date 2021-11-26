class Card:
    def __init__(self, suit, value):
        self.Suit = suit
        self.Value = value

    def __repr__(self):
        return str(self.Suit) + " " + self.Value