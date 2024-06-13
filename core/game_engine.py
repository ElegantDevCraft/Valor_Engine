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
        world_data = self.data_manager.load_world_data()
        self.scenes = build_world(world_data)
        self.is_running = True
        self.current_scene = self.scenes[world_data['starting_location']]
        self.player = self.data_manager.load_player_data()

    def start_game(self):
        # Display a welcome message using Markdown and Pygments for syntax highlighting
        console.print("Welcome to the Adventure Game!", style="bold green")
        self.render_scene()  # Render the initial scene

        # Start the game loop
        while self.is_running:
            command = console.input("What do you want to do? ").strip().lower()
            if command:
                action_result = self.perform_action(command)
        
                # Check the result and print the appropriate response
                if action_result['result'] == 'success':
                    console.print(action_result['description'], style="bold yellow")
                    # If the action changes the scene, render the new scene
                    if 'new_scene' in action_result:
                        self.current_scene = self.scenes[action_result['new_scene']]
                        self.render_scene()
                else:
                    console.print("An error occurred: " + action_result['description'], style="bold red")

            else:
                console.print("Please enter a command.", style="bold red")

    def perform_action(self, command):
        action_parts = command.split()
        action = action_parts[0]
    
        if action == 'look':
            return {'result': 'success', 'description': self.current_scene.describe()}
        elif action == 'walk':
            if len(action_parts) > 1:
                direction = action_parts[1]
                # Use the inherited get_connected_location method
                new_scene = self.current_scene.get_connected_location(direction)
                if new_scene:
                    return {'result': 'success', 'description': new_scene.describe(), 'new_scene': new_scene.name}
                else:
                    return {'result': 'error', 'description': 'You cannot go that way.'}
            else:
                return {'result': 'error', 'description': 'You need to specify a direction to walk.'}
        else:
            return {'result': 'error', 'description': f'Unknown action: {action}'}

    def render_scene(self):
        # Check if current_scene is an instance of Scene and print its description
        if isinstance(self.current_scene, Scene):
            console.print(self.current_scene.describe(), style="bold blue")
        else:
            console.print("Error: 'current_scene' is not an instance of Scene.", style="bold red")

    # Additional methods for combat, dialogue, inventory, etc. can be added here
