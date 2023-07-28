from library import *


class Challenger:
    def __init__(self, defense_stance="looseface"):
        self.name = "Challenger"
        self.sectorGroup = SectorGroup()

        self.full_stamina = 10
        self.curr_stamina = 0
        self.block_strength = 0

        self.curr_defense_stance = defense_stance.lower().strip()

    def Visualize(self):
        print(
            f"\n>> {self.name.upper()} DEFENSE STANCE : {self.curr_defense_stance.upper()}")
        self.sectorGroup.Visualize()
        print("\t>> Stamina:", self.curr_stamina, "\n")

    def SetCurrStamina(self):
        updated_stamina = self.full_stamina
        for sector in self.sectorGroup.sectors:
            # each blocked sector influences the stamina
            if sector.blocked:
                updated_stamina -= sector.weight

        self.curr_stamina = updated_stamina

    def SetDefenseStance(self, defense_stance):
        self.curr_defense_stance = defense_stance.lower().strip()

        if defense_stance in defense_stances.keys():
            self.sectorGroup.SetSectorGroup(defense_stances[defense_stance])

        self.SetCurrStamina()
