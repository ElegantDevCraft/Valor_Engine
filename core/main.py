import random
import json
import os
import sys

import pytextgame
from rich import console
from .game_engine import GameEngine
from ..data.save_load import save_game, load_game

def main():
    engine = GameEngine()
    engine.start_game()

if __name__ == "__main__":
    main()
