from library import *
from challenger import *
import random


class AI:
    def __init__(self):
        self.challenger = None
        self.current_combo = None

    # returns a list of punch options for the ai to use based on the player's free sectors

    def GetPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(
            self.challenger.opponent.sectorGroup)
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

    def ChooseAction(self):
        print("AI Choosing Attack or Defend")
        punch_options = self.challenger.GetPunchOptions()

        # Set up base utility scores
        attack_utility = 50
        defend_utility = 40

        # Choose action with the highest utility
        if attack_utility > defend_utility:
            print("AI Choosing Attack")
            return 1
        else:
            print("AI Choosing Defend")
            return 2

    def ChoosePunch(self):
        # Get best combos in terms of damage and stamina
        best_damage_combo = self.GetBestDamageCombo()
        best_stamina_combo = self.GetBestStaminaCombo()

        # If AI has enough stamina, choose punch from combo with highest damage,
        # otherwise, choose punch from combo with lowest stamina cost
        if self.challenger.curr_stamina >= best_damage_combo.stamina_cost:
            chosen_combo = best_damage_combo
        else:
            chosen_combo = best_stamina_combo

        # Choose the first punch from the chosen combo
        chosen_punch = chosen_combo.punches[0]
        return chosen_punch

    def ChooseDefenseStance(self):
        random_stance = random.choice(list(defense_stances.keys()))
        self.challenger.SetDefenseStance(random_stance)
