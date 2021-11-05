from enum import Enum

class Ranking(Enum):
    StraightFlush = 1
    FourOfAKind = 2
    Flush = 3
    Straight = 4
    ThreeOfAKind = 5
    TwoPair = 6
    Pair = 7
    HighCard = 8