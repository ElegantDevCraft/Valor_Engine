
from rich.table import Table
from rich.console import Console
import random
import json

# Load the creatures data from the JSON file
with open('data/json_data/creatures.json', 'r') as file:
    creatures_data = json.load(file)

with open('data/json_data/npcs.json', 'r') as file:
    npc_data = json.load(file)

class CommandParser:
    def __init__(self, game_engine):
        # Initialize command mappings and other necessary variables
        self.game_engine = game_engine
        self.commands = {
            "explore": self.explore,
            "talk": self.talk,
            "battle": self.battle_menu,
            "trade": self.trade,
            "quest": self.quest,
            "help": self.help,
            # Add more commands as needed
        }

    def parse(self, input_command):
        # Logic to parse the input command and execute the corresponding action
        parts = input_command.split()
        command = parts[0].lower()
        args = parts[1:]

        # Execute the corresponding method for the command
        if command in self.commands:
            self.commands[command](*args)
        else:
            print("I don't understand that command.")

    # Command methods inspired by the games
    def explore(self, *args):
        # Example locations
        locations = {
            "forest": "You are standing in a forest with tall trees all around.",
            "cave": "You enter a dark cave; it's cold and damp.",
            "village": "You arrive at a small village bustling with activity."
        }

        # Example movement commands
        movements = {
            "north": "forest",
            "south": "village",
            "enter": "cave"
        }

        # Check if the player's command is a movement command
        if args and args[0] in movements:  # Added check for args existence
            new_location = movements[args[0]]
            print(locations[new_location])
            self.game_engine.player['location'] = new_location
            # Update the player's current location in the game state here
        else:
            print("You can't go that way.")

        # Random encounter
        if random.choice([True, False]):
            self.random_encounter(new_location)

    def random_encounter(self, current_location):
         # Filter creatures that can be found in the current location
        possible_creatures = [creature for creature in creatures_data['creatures'] if current_location in creature['locations']]
        
        if possible_creatures:
            # Randomly select one of the possible creatures
            encountered_creature = random.choice(possible_creatures)
            print(f"A wild {encountered_creature['name']} appears!")
            
            # Here you can add logic to initiate a battle or capture sequence
            # For example:
            # self.initiate_battle(encountered_creature)
            # or
            # self.attempt_capture(encountered_creature)
        else:
            print("You wander around but encounter nothing.")

    # Dialogue system
    def talk(self, *args):
        # Check if the player has specified which NPC to talk to
        if args:
            npc_name = ' '.join(args).lower()
            # Retrieve the dialogue for the specified NPC
            if npc_name in npc_data:
                dialogue = random.choice(npc_data[npc_name]['dialogues'])
                print(f"{npc_name.capitalize()}: {dialogue}")
            else:
                print("There is no one by that name here.")
        else:
            print("Who do you want to talk to?")

    def battle_menu(self, *args):
         # Transition to a menu system for battles
        print("A wild enemy appears!")
        print("Entering battle mode...")
        self.show_battle_menu()

    def trade(self, *args):
        # Resource management, selling and buying items
        print("You barter with a local merchant.")
        # Add more detailed logic here

    def quest(self, *args):
        # Embarking on quests, accepting and completing them
        print("You accept a quest.")
        # Add more detailed logic here

    def help(self, *args):
        # Use Rich to display a help menu with available commands in a table
        table = Table(title="Available Commands")

        table.add_column("Command", justify="left", style="cyan", no_wrap=True)
        table.add_column("Description", style="magenta")

        # Populate the table with commands and their descriptions
        table.add_row("explore", "Open-world exploration")
        table.add_row("talk", "Strike up a conversation with an NPC")
        # Removed 'recruit' row as it's not implemented
        # Add more rows as needed

        console = Console()
        console.print(table)
        # Add more detailed help information here

    def show_battle_menu(self):
        # Display the battle menu with options
        while True:
            print("\nChoose your action:")
            print("1. Attack")
            print("2. Defend")
            print("3. Use Item")
            print("4. Run Away")
            choice = input("> ")

            if choice == "1":
                self.attack()
                break
            elif choice == "2":
                self.defend()
                break
            elif choice == "3":
                self.use_item()
                break
            elif choice == "4":
                self.run_away()
                break
            else:
                print("Invalid choice. Please select a number from 1 to 4.")

    # Methods for battle menu actions
    def attack(self):
        print("You launch an attack!")
        # Add attack logic here

    def defend(self):
        print("You brace for the enemy's attack!")
        # Add defend logic here

    def use_item(self):
        print("You use an item from your inventory.")
        # Add item usage logic here

    def run_away(self):
        print("You attempt to flee from battle!")
        # Add escape logic here

    # Add more command methods as needed
