from rich import print as rprint
from .locations import Forest, Castle

#Functions to initialize and populate the game world
def build_world():
    # Create the starting location
    starting_location = Forest()
    # Define interactions for the starting location
    starting_location.interactions = {
        'path': 'path leading to the castle',
        # ... other possible interactions ...
    }
    return starting_location
