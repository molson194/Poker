from Deck import Deck
from Ranking import Ranking

class Evaluator:
    @staticmethod
    def EvaluatePlayers(playerCards, flop, turn, river):
        playerResults = []
        for player in playerCards.keys():
            playerResults.append( (player, Evaluator.EvaluateCards(list(playerCards[player]) + list(flop) + [turn] + [river]) ) )
        
        playerResults.sort(key=lambda x: x[1][0].value * 1000 + x[1][1])

        print(playerCards)
        print(flop)
        print(turn)
        print(river)
        print(playerResults)


        return playerResults

    @staticmethod
    # TODO: Consider kickers (two people that have the same main hand but different remaining cards)
    def EvaluateCards(cards):
        valueCounts = {}
        suitCounts = {}
        highCardValue = 0

        # TODO: Straight flush

        for card in cards:
            valueCounts[card.Value] = valueCounts.get(card.Value, 0) + 1
            suitCounts[card.Suit] = suitCounts.get(card.Suit, 0) + 1
            highCardValue = max(highCardValue, Deck.RankValue(card.Value, None))

        # 4 of a kind    
        firstMaxValueKey = max(valueCounts, key = valueCounts.get)
        firstMaxValueCount = valueCounts[firstMaxValueKey]

        if firstMaxValueCount == 4:
            return (Ranking.FourOfAKind, Deck.RankValue(firstMaxValueKey, None))

        # Full House
        if firstMaxValueCount == 3:
            del valueCounts[firstMaxValueKey]
            secondMaxValueKey = max(valueCounts, key = valueCounts.get)
            secondMaxValueCount = valueCounts[secondMaxValueKey]

            if secondMaxValueCount == 3 and Deck.RankValue(firstMaxValueKey, None) > Deck.RankValue(secondMaxValueKey, None):
                return (Ranking.FullHouse, Deck.RankValue(secondMaxValueKey, firstMaxValueKey))
            elif secondMaxValueCount >= 2:
                return (Ranking.FullHouse, Deck.RankValue(firstMaxValueKey, secondMaxValueKey))
        
        # TODO: Flush
        # TODO: Straight

        # 3 of a kind
        if firstMaxValueCount == 3:
            return (Ranking.ThreeOfAKind, Deck.RankValue(firstMaxValueKey, None))

        # Two Pair
        if firstMaxValueCount == 2:
            del valueCounts[firstMaxValueKey]
            secondMaxValueKey = max(valueCounts, key = valueCounts.get)
            secondMaxValueCount = valueCounts[secondMaxValueKey]

            if secondMaxValueCount == 2 and Deck.RankValue(firstMaxValueKey, None) > Deck.RankValue(secondMaxValueKey, None):
                return (Ranking.TwoPair, Deck.RankValue(secondMaxValueKey, firstMaxValueKey))
            elif secondMaxValueCount == 2:
                return (Ranking.TwoPair, Deck.RankValue(firstMaxValueKey, secondMaxValueKey))

        # Pair
        if firstMaxValueCount == 2:
            return (Ranking.Pair, Deck.RankValue(firstMaxValueKey, None))

        return (Ranking.HighCard, highCardValue)