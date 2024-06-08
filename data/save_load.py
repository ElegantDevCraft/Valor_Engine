import json

class SaveLoad:
    @staticmethod
    def save_game_state(data, file_path='data/savegame.json'):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_game_state(file_path='data/savegame.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
