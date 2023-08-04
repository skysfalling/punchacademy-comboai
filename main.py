from library import *
from challenger import *
from ai import *
import time


def main():
    punch_library = PunchLibrary()
    print()

    # (( CREATE THE CHALLENGERS ))
    player = Challenger()
    player.name = "Player"

    challenger = Challenger()
    challenger.name = "AI"
    challenger_ai = AI(challenger, player)

    print("WELCOME TO PUNCH ACADEMY")
    print("\n DEFENSE STANCES ============================== \n")
    for stance in defense_stances:
        print("  ", stance, ":", defense_stances[stance])

    # (( PLAYER CHOOSE DEFENSE POSITION ))
    input_action = str(
        input("\nType out a stance name for PLAYER start: "))
    player.SetDefenseStance(input_action)
    player.Visualize()

    # (( AI CHOOSE DEFENSE POSITION ))
    input_action = str(
        input("\nType out a stance name for AI start: "))
    challenger.SetDefenseStance(input_action)
    challenger.Visualize()

    print("=============================================== ")

    print("FIGHT!")

    player.Visualize()
    print("---------------")
    challenger.Visualize()
    print()

    # (( PLAYER PUNCH ))
    input_action = int(
        input("\nPlayer >> Choose an action: (1) Attack, (2) Defend: "))

    if input_action == 1:
        print("---- # PLAYER ATTACKS # ----")
        print("Here are your punch options:")
        print(player.PrintPunchOptions())

        punch_options = player.GetPunchOptions()
        punch_numbers = []
        for i in range(len(punch_options)):
            punch_numbers.append(punch_options[i].number)

        prompt = "\nPlayer >> Choose an action: "
        input_action = int(input(prompt))
        chosen_punch = punch_options[int(input_action) - 1]
        print("You chose: ", chosen_punch)

        # (( PLAYER PUNCH ))
        challenger.Visualize()
        input_action = str(
            input("\nPlayer >> Choose an available sector:"))

    challenger_ai.GetComboOptions()
    print(challenger_ai.GetBestDamageCombo())


if __name__ == "__main__":
    main()
