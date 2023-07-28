from library import *
from challenger import *


class AI:
    def __init__(self, challenger, player):
        self.challenger = challenger
        self.player = player

    # returns a list of punch options for the ai to use based on the player's free sectors
    def GetPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(
            self.player.sectorGroup)
        return punchOptions

    # returns a list of combo options for the ai to use based on the available punch options
    def GetComboOptions(self):
        comboOptions = []
        punchOptions = self.GetPunchOptions()
        for punch in punchOptions:
            for combo in comboLibrary.combos:

                # if punch is the first punch in the combo, add it to the comboOptions
                if (punch == combo.punches[0] and combo.stamina_cost < self.challenger.curr_stamina):
                    comboOptions.append(combo)

        return comboOptions
