import random
import json
import os
import sys

import pytextgame
from rich import console

# Main game loop

def main():
    while True:
        show_current_scene()
        player_input = get_player_input()
        process_input(player_input)
        if check_end_conditions():
            break
