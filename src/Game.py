from Hand import Hand
from Player import Player

class Game:
    def __init__(self):
        players = []
        for i in range(3):
            players.append(Player(i, 1000))
        self.Players = players
        self.Hands = []

    def PlayGame(self):
        for i in range(2):
            print("Hand Start " + str(i))

            hand = Hand(self.Players, i % len(self.Players))
            self.Hands.append(hand)

            print("Hand End " + str(i))