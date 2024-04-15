from utilities.inventory import Inventory

# Player character definition and behavior

class Player:
    def __init__(self):
        self.stats = {'Strength': 10, 'Agility': 10, 'Intellect': 10}
        self.inventory = Inventory()
        self.location = 'start_location'
