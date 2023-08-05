from library import *


class Challenger:
    def __init__(self, name, ai=None):
        self.name = name
        self.fight_manager = None
        self.opponent = None
        self.sectorGroup = SectorGroup()

        self.ai = ai
        if (ai != None):
            ai.challenger = self

        self.full_stamina = 10
        self.curr_stamina = 0
        self.block_strength = 0
        self.punch_history = []

        self.curr_defense_stance = None

    def __repr__(self) -> str:
        out_string = f"\n>> {self.name}\n"
        out_string += "Defense : " + str(self.curr_defense_stance) + "\n"
        out_string += "Stamina : " + \
            str(self.curr_stamina) + "/" + str(self.full_stamina)
        return out_string

    def Visualize(self):
        print(self.__repr__())
        self.sectorGroup.Visualize()

    def TakePunch(self, punch):
        self.curr_stamina -= punch.damage
        if self.curr_stamina < 0:
            self.curr_stamina = 0

    def ResetStamina(self):
        updated_stamina = self.full_stamina
        for sector in self.sectorGroup.sectors:
            # each blocked sector influences the stamina
            if sector.blocked:
                updated_stamina -= sector.weight

        self.curr_stamina = updated_stamina

    def SetDefenseStance(self, stance):
        self.curr_defense_stance = stance.lower().strip()

        # choose the defense stance from global defense_stances
        if stance in defense_stances.keys():
            self.sectorGroup.SetSectorGroup(defense_stances[stance])
        else:
            print("Invalid Stance")
            return

        # update the current stamina amount
        self.ResetStamina()
        self.Visualize()

    def GetPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(
            self.sectorGroup)
        return punchOptions

    def PrintPunchOptions(self):
        punchOptions = punchLibrary.GetPunchOptions(self.sectorGroup)
        for i, option in enumerate(punchOptions):
            print(f"Option {i}: {option}")

    def RequestActionChoice(self):
        if (self.ai == None):
            input_action = int(
                input("\nPlayer >> Choose an action: (1) Attack, (2) Defend: "))

            if input_action == 1:
                return 1
            elif input_action == 2:
                return 2
            else:
                print("Invalid Input")
        else:
            return self.ai.ChooseAction()

    def RequestPunchChoice(self):
        if (self.ai == None):
            print("\n---- # PLAYER ATTACKS # ----")
            print("Here are your punch options:")

            # get punch options
            punch_options = self.GetPunchOptions()
            self.PrintPunchOptions()

            # get punch numbers
            punch_numbers = []
            for i in range(len(punch_options)):
                punch_numbers.append(punch_options[i].number)

            # ask for player input
            input_action = int(input("Player >> Choose a punch: "))
            chosen_punch = punch_options[int(input_action)]
        else:
            chosen_punch = self.ai.ChoosePunch()
        return chosen_punch

    def RequestDefenseChoice(self):
        print("\n" + self.name, "Choose Your Defense Stance")

        if (self.ai == None):
            # (( PLAYER CHOOSE DEFENSE POSITION ))
            # print out the defense stances
            for stance in defense_stances:
                print("  ", stance, ":", defense_stances[stance])

            # ask for player input
            input_action = str(
                input("\nType out a stance name for PLAYER start: "))

            self.SetDefenseStance(input_action)
        else:
            # (( AI CHOOSE DEFENSE POSITION ))
            self.ai.ChooseDefenseStance()
