import random
import json
import os
import sys

import pytextgame
from rich import console
from core.game_engine import GameEngine
from data.save_load import SaveLoad
from interfaces.handling.parser import CommandParser
from core.game_engine import GameEngine
from interfaces.handling.parser import CommandParser

def main():
    engine = GameEngine()
    parser = CommandParser(engine)
    
    # Start the game
    engine.start_game()

    engine.save_game()
    engine.load_game()
    
    # Main game loop that prompts for player input
    while True:
        command = input("What would you like to do? ")
        if command.lower() == 'quit':
            print("Thank you for playing!")
            break
        parser.parse(command)

if __name__ == "__main__":
    main()
