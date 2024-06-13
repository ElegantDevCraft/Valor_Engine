import random
import json
import os
import sys

import pytextgame
from rich import console
from core.game_engine import GameEngine
from data.save_load import SaveLoad
from interfaces.handling.parser import CommandParser

# Load the world data from the JSON file
with open('data\\json_data\\world.json', 'r') as file:
    world_data = json.load(file)

def main():
    game_engine = GameEngine()
    parser = CommandParser(game_engine)
    
    # Start the game
    game_engine.start_game()
    
    # Main game loop that prompts for player input
    while game_engine.is_running:
        command = input("What would you like to do? ")
        if command.lower() == 'quit':
            # Save the game before quitting
            game_engine.save_game()
            print("Thank you for playing!")
            break
        parser.parse(command)

if __name__ == "__main__":
    main()
