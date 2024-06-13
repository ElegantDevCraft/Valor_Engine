from rich import print as rprint

# Define a base class for locations in the game
class Location:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions
        self.connected_locations = {}

    def describe(self):
        # Return a description of the location
        return f"{self.name}: {self.description}"

    def connect_location(self, direction, location_obj):
        self.connected_locations[direction] = location_obj

    def get_connected_location(self, direction):
        return self.connected_locations.get(direction, None)