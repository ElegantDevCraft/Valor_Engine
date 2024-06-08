from keyboard import is_pressed
from markdown_it import MarkdownIt
from mdurl import encode
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from rich.console import Console
import pytextgame
from world.scene import Scene
from world.world_builder import build_world

import json
from data.data_manager import DataManager
from data.save_load import SaveLoad

# Initialize the Rich console
console = Console()

# Initialize the Markdown parser
md = MarkdownIt()

class GameEngine:
    def __init__(self):
        # Initialize the game world and player
        self.data_manager = DataManager()
        self.world = self.data_manager.load_world_data()
        self.is_running = True
        starting_location = build_world()
        self.current_scene = Scene(starting_location.description, starting_location.interactions)
        self.player = self.data_manager.load_player_data()

    def create_world(self):
        # Create the game world with a starting location
        return {
            'starting_location': {
                'description': 'You are standing in a forest with tall trees all around.',
                'actions': ['look', 'walk', 'use', 'talk'],
            }
        }

    def create_player(self):
        # Create the player character with initial attributes
        return {
            'name': 'Adventurer',
            'inventory': [],
            'location': 'starting_location'
        }

    def start_game(self):
        # Display a welcome message using Markdown and Pygments for syntax highlighting
        print("Welcome to the Adventure Game!")
        self.render_scene()  # Render the initial scene

        # Start the game loop
        while self.is_running:
            command = input("What do you want to do? ").strip().lower()
            if command:
                action_result = self.perform_action(command, self.player)
        
                # Check the result and print the appropriate response
                if action_result['result'] == 'success':
                    print(action_result['description'])
                    # If the action changes the scene, render the new scene
                    if self.is_scene_changed(action_result, command):
                        self.render_scene()
                else:
                    print("An error occurred:", action_result['description'])

            else:
                print("Please enter a command.")

    def is_scene_changed(self, action_result, command):
        # Determine if the scene should change based on the action result and command
        # This method can be expanded to handle more complex game logic
        return 'new_scene' in action_result or (command.startswith('walk') and 'error' not in action_result)

    def process_input(self):
        # Get player input and process it
        command = input("What do you want to do? ")
        if command.lower() == 'quit' or is_pressed('esc'):
            print("Goodbye!")
            self.is_running = False
        elif command:
            # Process the command using the perform_action method
            action_result = self.perform_action(command, self.player)
            # Check the result and print the appropriate response
            if action_result['result'] == 'success':
                print(action_result['description'])
            else:
                print("An error occurred:", action_result['description'])

    def perform_action(self, action, player):
        action_parts = action.split()
        command = action_parts[0]
        # Handle the player's action and return the result
        if action == 'look':
            # Return the description of the current location
            return {'result': 'success', 'description': self.current_scene.describe()}
        elif command == 'walk':
        # Check if a direction is provided
            if len(action_parts) > 1:
                direction = action_parts[1]
                # Check if the direction is valid in the current scene
                if direction in self.current_scene.interactions:
                    # Get the new scene based on the direction
                    new_scene = self.current_scene.interactions[direction]
                    # Ensure new_scene is a Scene instance
                    if isinstance(new_scene, Scene):
                        self.current_scene = new_scene
                        return {'result': 'success', 'description': self.current_scene.describe()}
                    else:
                        return {'result': 'error', 'description': 'You cannot go that way.'}
                else:
                    return {'result': 'error', 'description': f'There is no path leading {direction}.'}
            else:
                return {'result': 'error', 'description': 'You need to specify a direction to walk.'}
        else:
            return {'result': 'error', 'description': f'Unknown action: {command}'}

    def render_scene(self):
        #Check if current_scene is an instance of Scene and print its description
        if isinstance(self.current_scene, Scene):
            print(self.current_scene.describe())
        else:
            print("Error: 'current_scene' is not an instance of Scene.")

    def process_command(self, command):
        # Process the player's command
        try:
            # Get the result of the action
            action_result = self.current_scene.perform_action(command, self.player)
            # Check if the action was successful and update the current scene accordingly
            if action_result['result'] == 'success':
                # Update the current scene with the new scene dictionary
                self.current_scene = self.get_new_scene_based_on_action(action_result)
            else:
                # Handle the error message without changing the current scene
                console.print(action_result['description'], style="bold red")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")

    def save_game(self):
        # Create a dictionary that represents the current game state
        game_state = {
            'player': self.player,
            'current_scene': self.current_scene,
            # Include other relevant game state data
        }
        # Use the SaveLoad class to save the game state
        SaveLoad.save_game_state(game_state)

    def load_game(self):
        # Use the SaveLoad class to load the game state
        game_state = SaveLoad.load_game_state()
        # Restore the game state
        self.player = game_state['player']
        self.current_scene = game_state['current_scene']
        # Restore other game state data as needed

    # Additional methods for combat, dialogue, inventory, etc. can be added here

# The GameEngine class can now be imported into main.py to start the game
