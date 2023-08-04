from library import *


class Challenger:
    def __init__(self, defense_stance="looseface"):
        self.name = "Challenger"
        self.sectorGroup = SectorGroup()

        self.full_stamina = 10
        self.curr_stamina = 0
        self.block_strength = 0

        self.curr_defense_stance = defense_stance.lower().strip()

    def __repr__(self) -> str:
        out_string = f"{self.name} >> "
        out_string += str(self.curr_defense_stance)
        out_string += " >> " + str(self.curr_stamina) + \
            "/" + str(self.full_stamina)
        return out_string

    def Visualize(self):
        self.sectorGroup.Visualize()

    def SetCurrStamina(self):
        updated_stamina = self.full_stamina
        for sector in self.sectorGroup.sectors:
            # each blocked sector influences the stamina
            if sector.blocked:
                updated_stamina -= sector.weight

        self.curr_stamina = updated_stamina

    def SetDefenseStance(self, stance):
        self.curr_defense_stance = stance.lower().strip()

        if stance in defense_stances.keys():
            self.sectorGroup.SetSectorGroup(defense_stances[stance])

        self.SetCurrStamina()

    def GetPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(
            self.sectorGroup)
        return punchOptions

    def PrintPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(
            self.sectorGroup)
        for option in punchOptions:
            print(option)
