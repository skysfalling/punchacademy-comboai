from library import *
from challenger import *
from ai import *
from fightmanager import *
import time


def main():
    ai_player = Challenger("AI", AI())
    player = Challenger("Player")
    fight_manager = FightManager(ai_player, player)
    fight_manager.Start()


if __name__ == "__main__":
    main()
