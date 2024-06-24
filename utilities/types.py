import json

class TypeChart:
    def __init__(self):
        self.chart = self.load_type_chart()

    def load_type_chart(self):
        with open('data/json_data/types.json', 'r') as file:
            return json.load(file)

    def get_effectiveness(self, attacker_type, defender_type):
        # Logic to determine move effectiveness based on the type chart
        pass