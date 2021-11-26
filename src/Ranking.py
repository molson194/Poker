from enum import Enum

class Ranking(Enum):
    StraightFlush = 1
    FourOfAKind = 2
    FullHouse = 3
    Flush = 4
    Straight = 5
    ThreeOfAKind = 6
    TwoPair = 7
    Pair = 8
    HighCard = 9