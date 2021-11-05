from Ranking import Ranking

# TODO 1: Evaluate cards
class Evaluator:
    @staticmethod
    def EvaluatePlayers(isPlayerRemaining, playerCards):
        return 0

    @staticmethod
    def EvaluateSevenCards(cards):
        return 0

    # Returns the value of 5 cards (or a value less than the best ranking so far)
    #
    # Straight Flush: 1-10
    # Four-of-a-Kind: 1-13
    # Full House: 1-156
    # Flush: 1-9
    # Straight: 1-10
    # 3-of-a-kind: 1-13
    # 2-pair: 1-156
    # 1-pair: 1-13
    # High card: 1-8
    @staticmethod
    def EvaluateFiveCards(cards, bestRankingSoFar):
        value = Evaluator.StraightFlush(cards)
        if value != 0 or Ranking.StraightFlush == bestRankingSoFar:
            return (Ranking.StraightFlush, value)

        value = Evaluator.FourOfAKind(cards)
        if value != 0 or Ranking.FourOfAKind == bestRankingSoFar:
            return (Ranking.FourOfAKind, value)

        value = Evaluator.Flush(cards)
        if value != 0 or Ranking.Flush == bestRankingSoFar:
            return (Ranking.Flush, value)

        value = Evaluator.Straight(cards)
        if value != 0 or Ranking.Straight == bestRankingSoFar:
            return (Ranking.Straight, value)

        value = Evaluator.ThreeOfAKind(cards)
        if value != 0 or Ranking.ThreeOfAKind == bestRankingSoFar:
            return (Ranking.ThreeOfAKind, value)

        value = Evaluator.TwoPair(cards)
        if value != 0 or Ranking.TwoPair == bestRankingSoFar:
            return (Ranking.TwoPair, value)

        value = Evaluator.Pair(cards)
        if value != 0 or Ranking.Pair == bestRankingSoFar:
            return (Ranking.Pair, value)

        return (Ranking.HighCard, Evaluator.HighCard(cards))
    
    @staticmethod
    def StraightFlush(cards):
        return 0

    @staticmethod
    def FourOfAKind(cards):
        return 0

    @staticmethod
    def Flush(cards):
        return 0

    @staticmethod
    def Straight(cards):
        return 0

    @staticmethod
    def ThreeOfAKind(cards):
        return 0

    @staticmethod
    def TwoPair(cards):
        return 0

    @staticmethod
    def Pair(cards):
        return 0

    @staticmethod
    def HighCard(cards):
        return 0