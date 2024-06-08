from rich import print as rprint

# Define a base class for locations in the game
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_locations = {}

    def connect_location(self, location, direction):
        self.connected_locations[direction] = location

# Example of creating specific locations
class Forest(Location):
    def __init__(self):
        super().__init__("Forest", "You are standing in a forest with tall trees all around.")
        self.interactions = {}

class Castle(Location):
    def __init__(self):
        super().__init__("Castle", "You see a grand castle with a towering gate.")
