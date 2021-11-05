import random
from Action import Action
from ActionOption import ActionOption

class Player:
    def __init__(self, position, chips):
        self.Position = position
        self.Chips = chips

    def Action(self, players, currentPotContribution, maxPotContribution, hand):
        # TODO 5: decide action option based off of characteristics
        # TODO 7: Pass available options and chips remaining to the AI agent
        actionOption = random.choice(list(ActionOption))

        potContribution = maxPotContribution - currentPotContribution

        # TODO 4: Could fold here
        if potContribution > self.Chips:
            potContribution = self.Chips
            self.Chips = 0
            actionOption = ActionOption.CheckCall
            return Action(actionOption, potContribution)

        if actionOption == ActionOption.Bet:
            # TODO 6: decide bet amount off of characteristics
            betAmount = random.randint(1, self.Chips - potContribution)
            potContribution = potContribution + betAmount
            self.Chips = self.Chips - potContribution
            print("Player " + str(self.Position) + ": " + str(actionOption) + "=" + str(betAmount) + ", RemainingChips=" + str(self.Chips))
        
        elif actionOption == ActionOption.CheckCall:
            self.Chips = self.Chips - potContribution
            print("Player " + str(self.Position) + ": " + str(actionOption) + "=" + str(potContribution) + ", RemainingChips=" + str(self.Chips))

        else:
            print("Player " + str(self.Position) + ": " + str(actionOption) + ", RemainingChips=" + str(self.Chips))
        
        return Action(actionOption, potContribution)