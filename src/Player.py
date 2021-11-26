import random
from Action import Action
from ActionOption import ActionOption

class Player:
    def __init__(self, position, chips):
        self.Position = position
        self.Chips = chips

    def Action(self, players, currentPotContribution, maxPotContribution, hand):

        availableActions = list(ActionOption)

        minBetAmount = maxPotContribution - currentPotContribution
        if minBetAmount >= self.Chips:
            availableActions.remove(ActionOption.Bet)

        maxBetAmount = self.Chips - minBetAmount

        # TODO: Implement different actions based on previous hand data, player characteristics, etc.
        return self.RandomAction(availableActions, minBetAmount, maxBetAmount)

    def __repr__(self):
        return "Player " + str(self.Position) + " Chip " + str(self.Chips)

    def RandomAction(self, availableActions, minBetAmount, maxBetAmount):
        actionOption = random.choice(availableActions)
        potContribution = 0

        if actionOption == ActionOption.Bet:
            betAmount = random.randint(1, maxBetAmount)
            potContribution = minBetAmount + betAmount
            self.Chips = self.Chips - potContribution      
        elif actionOption == ActionOption.CheckCall:
            checkCallAmount = min(minBetAmount, self.Chips)
            self.Chips = self.Chips - checkCallAmount
            potContribution = checkCallAmount
        
        print("Player " + str(self.Position) + ": " + str(actionOption) + ", RemainingChips: " + str(self.Chips))
        return Action(actionOption, potContribution)