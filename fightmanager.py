from library import *
from challenger import *
from ai import *
import time
import random


class FightManager:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

        # set fight manager reference
        self.player1.fight_manager = self
        self.player2.fight_manager = self

        print("Fight Manager >> Player 1: ", self.player1.name)
        print("Fight Manager >> Player 2: ", self.player2.name)
        print("Fight Manager >> Initialized")
        print()
        print("WELCOME TO PUNCH ACADEMY")
        print("========================")
        print()

    def Start(self):
        self.FightSetup()

        for i in range(2):
            self.NewRound()

    def FightSetup(self):
        print("\nFight Manager >> Fight Setup")
        print("CHOOSE YOUR DEFENSE STANCE")
        print("========================")
        self.player1.RequestDefenseChoice()
        self.player2.RequestDefenseChoice()

    def NewRound(self):
        print("\nFight Manager >> New Round")
        print("========================")
        print("---- NEW ROUND ----")
        print("========================")
        self.player1.Visualize()
        self.player2.Visualize()
        print("========================")
        p1_action_id = self.player1.RequestActionChoice()
        p2_action_id = self.player2.RequestActionChoice()

        print()
        print("Fight Manager >> CHOOSE ACTION")
        print("Fight Manager >>", self.player1.name, "Action :", p1_action_id)
        print("Fight Manager >>", self.player2.name, "Action :", p2_action_id)

        # PLAYER1 - GET ACTION CHOICE
        p1_punch = None
        if (p1_action_id == 1):
            p1_punch = self.player1.RequestPunchChoice()
        elif (p1_action_id == 2):
            self.player1.RequestDefenseChoice()

        # PLAYER2 - GET ACTION CHOICE
        p2_punch = None
        if (p2_action_id == 1):
            p2_punch = self.player2.RequestPunchChoice()
        elif (p2_action_id == 2):
            self.player2.RequestDefenseChoice()

        print()
        print("Fight Manager >> EXECUTE ACTION")
        self.ExecutePunch(self.player1, p1_punch)
        self.ExecutePunch(self.player2, p2_punch)

    def ExecutePunch(self, player, punch):
        print(player.name, "Punch:", punch)
        player.opponent.TakePunch(punch)
        print("++", player.opponent.name, "Stamina",
              player.opponent.curr_stamina)
