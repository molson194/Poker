from ActionOption import ActionOption
from Deck import Deck
from Round import Round

class Hand:
    def __init__(self, players, dealerPosition):
        self.Actions = {}
        
        deck = Deck()
        self.Flop = (deck.DealCard(), deck.DealCard(), deck.DealCard())
        self.Turn = deck.DealCard()
        self.River = deck.DealCard()
        self.PlayerChips = []

        self.PlayerCards = {}
        for player in players:
            self.PlayerCards[player] = (deck.DealCard(), deck.DealCard())
            self.PlayerChips.append(player.Chips)

        isPlayerRemaining = [True] * len(players)
        numPlayersRemaining = len(players)
        potContributions = [0] * len(players)
        maxPotContribution = 0

        # TODO 1: set the bb sb pot contributions, subtract from chips, and increase max pot contribution

        for round in Round:
            print(str(round))

            self.Round = round
            self.Actions[round] = []

            # Start to left of dealer except pre-flop
            currentPosition = (dealerPosition + 1) % len(players)
            if round == Round.PreFlop:
                currentPosition = (dealerPosition + 3) % len(players)

            # Get first players action
            lastBetPosition = currentPosition
            isFirst = True

            # Loop through players until one is left or it gets back to the last person to bet
            while numPlayersRemaining > 1 and (lastBetPosition != currentPosition or isFirst):
                isFirst = False
                if isPlayerRemaining[currentPosition]:
                    playerAction = players[currentPosition].Action(players, potContributions[currentPosition], maxPotContribution, self)
                    self.Actions[round].append(playerAction)

                    if playerAction.ActionOption == ActionOption.Bet:
                        lastBetPosition = currentPosition
                        potContributions[currentPosition] = potContributions[currentPosition] + playerAction.PotContribution
                        maxPotContribution = max(potContributions)
                        
                    elif playerAction.ActionOption == ActionOption.Fold:
                        numPlayersRemaining = numPlayersRemaining - 1
                        isPlayerRemaining[currentPosition] = False
                    
                    elif playerAction.ActionOption == ActionOption.CheckCall:
                        potContributions[currentPosition] = potContributions[currentPosition] + playerAction.PotContribution
            
                currentPosition = (currentPosition + 1) % len(players)
        
        remainingPlayers = [position for position, element in enumerate(isPlayerRemaining) if element]

        # TODO 2: compare cards of players
        # TODO 3: distribute money (and side-pots) - winner subtract money equally, next winner subtract money (until 0 left for all)
        self.WinnerPosition = remainingPlayers[0]
        print("Pot contributions: " + str(potContributions))
        print("Winner Position: " + str(self.WinnerPosition))
