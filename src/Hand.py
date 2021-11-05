from ActionOption import ActionOption
from Deck import Deck
from Evaluator import Evaluator
from Round import Round

class Hand:
    def __init__(self, players, dealerPosition):
        self.Actions = {}
        
        deck = Deck()
        self.Flop = (deck.DealCard(), deck.DealCard(), deck.DealCard())
        self.Turn = deck.DealCard()
        self.River = deck.DealCard()

        self.PlayerChips = {}
        self.PlayerCards = {}
        isPlayerRemaining = {}
        potContributions = {}
        for player in players:
            self.PlayerCards[player] = (deck.DealCard(), deck.DealCard())
            self.PlayerChips[player] = player.Chips
            isPlayerRemaining[player] = True
            potContributions[player] = 0

        numPlayersRemaining = len(players)
        
        smallBlindPostion = (dealerPosition + 1) % len(players)
        bigBlindPosition = (dealerPosition + 2) % len(players)
        players[smallBlindPostion].Chips = players[smallBlindPostion].Chips - 50
        players[bigBlindPosition].Chips = players[bigBlindPosition].Chips - 100
        potContributions[players[smallBlindPostion]] = 50
        potContributions[players[bigBlindPosition]] = 100
        maxPotContribution = 100

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
            isPreFlopFirst = True and round == Round.PreFlop

            # Loop through players until one is left or it gets back to the last person to bet
            while numPlayersRemaining > 1 and (lastBetPosition != currentPosition or isPreFlopFirst):
                isPreFlopFirst = False
                currentPlayer = players[currentPosition]
                if isPlayerRemaining[currentPlayer]:
                    playerAction = currentPlayer.Action(players, potContributions[currentPlayer], maxPotContribution, self)
                    self.Actions[round].append(playerAction)

                    if playerAction.ActionOption == ActionOption.Bet:
                        lastBetPosition = currentPosition
                        potContributions[currentPlayer] = potContributions[currentPlayer] + playerAction.PotContribution
                        maxPotContribution = max(maxPotContribution, potContributions[currentPlayer])
                        
                    elif playerAction.ActionOption == ActionOption.Fold:
                        numPlayersRemaining = numPlayersRemaining - 1
                        isPlayerRemaining[currentPlayer] = False
                    
                    elif playerAction.ActionOption == ActionOption.CheckCall:
                        potContributions[currentPlayer] = potContributions[currentPlayer] + playerAction.PotContribution
            
                currentPosition = (currentPosition + 1) % len(players)

        # TODO 3: distribute money (and side-pots) - winner subtract money equally, next winner subtract money (until 0 left for all)
        self.WinnerPosition = Evaluator.EvaluatePlayers(isPlayerRemaining, self.PlayerCards)
        print("Pot contributions: " + str(potContributions))
        print("Winner Position: " + str(self.WinnerPosition))
