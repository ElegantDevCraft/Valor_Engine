import json

class DataManager:
    def __init__(self, base_path='data/json_data/'):
        self.base_path = base_path

    def load_data(self, file_name):
        try:
            with open(self.base_path + file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"The file {file_name} was not found.")
        except json.JSONDecodeError:
            print(f"The file {file_name} is not valid JSON.")

    def load_world_data(self):
        return self.load_data('world.json')

    def load_player_data(self):
        return self.load_data('player.json')

    def load_items_data(self):
        return self.load_data('items.json')

    def load_npcs_data(self):
        return self.load_data('npcs.json')

    def load_quests_data(self):
        return self.load_data('quests.json')

    def load_enemies_data(self):
        return self.load_data('enemies.json')