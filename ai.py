from library import *
from challenger import *


class AI:
    def __init__(self, challenger, player):
        self.challenger = challenger
        self.player = player
        self.current_combo = None

    # returns a list of punch options for the ai to use based on the player's free sectors

    def GetPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(
            self.player.sectorGroup)
        return punchOptions

    # returns a list of combo options for the ai to use based on the available punch options
    def GetComboOptions(self):
        self.comboOptions = []
        punchOptions = self.GetPunchOptions()
        for punch in punchOptions:
            for combo in comboLibrary.combos:
                # if punch is the first punch in the combo, add it to the comboOptions
                if (punch == combo.punches[0] and combo.stamina_cost < self.challenger.curr_stamina):
                    self.comboOptions.append(combo)
        return self.comboOptions

    def PrintComboOptions(self):
        print("AI COMBO OPTIONS ============================== ")
        print(">> AI Curr Stamina : ", self.challenger.curr_stamina,
              "======================\n")
        for combo in self.comboOptions:
            print(combo, "\n")
        print("=============================================== ")

    def GetBestDamageCombo(self):
        comboOptions = self.GetComboOptions()

        # Iterate through all combos and find the combo with the highest total damage output
        best_combo = None
        best_damage = 0

        for combo in comboOptions:
            combo_damage = sum(punch.damage for punch in combo.punches)
            if combo_damage > best_damage:
                best_combo = combo
                best_damage = combo_damage

        return best_combo

    def GetBestStaminaCombo(self):
        comboOptions = self.GetComboOptions()

        # Initialize variables to track the best combo with the lowest stamina cost
        best_combo = None
        # Set to positive infinity as an initial value
        lowest_stamina_cost = float('inf')

        for combo in comboOptions:
            combo_stamina_cost = combo.stamina_cost
            if combo_stamina_cost < lowest_stamina_cost:
                best_combo = combo
                lowest_stamina_cost = combo_stamina_cost

        return best_combo
