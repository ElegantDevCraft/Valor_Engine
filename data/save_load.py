import json

# This file handles saving and loading game states.

def save_game(game_state, filename='savegame.json'):
    with open(filename, 'w') as file:
        json.dump(game_state, file)

def load_game(filename='savegame.json'):
    with open(filename, 'r') as file:
        game_state = json.load(file)
    return game_state
