from library import *
from challenger import *
from ai import *


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
    input_stance = str(
        input("\nType out a stance name for PLAYER start: "))
    player.SetDefenseStance(input_stance)
    player.Visualize()

    # (( AI CHOOSE DEFENSE POSITION ))
    input_stance = str(
        input("\nType out a stance name for AI start: "))
    challenger.SetDefenseStance(input_stance)
    challenger.Visualize()
    print("=============================================== ")

    comboOptions = challenger_ai.GetComboOptions()
    print("AI COMBO OPTIONS ============================== ")
    print(">> AI Curr Stamina : ", challenger.curr_stamina,
          "======================\n")
    for combo in comboOptions:
        print(combo, "\n")
    print("=============================================== ")


if __name__ == "__main__":
    main()
