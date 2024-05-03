from keyboard import is_pressed
from markdown_it import MarkdownIt
from mdurl import encode
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from rich.console import Console
import pytextgame

# Initialize the Rich console
console = Console()

# Initialize the Markdown parser
md = MarkdownIt()

class GameEngine:
    def __init__(self):
        # Initialize the game world and player
        #self.game = create_game()
        #self.world = create_world()
        self.is_running = True
        #self.current_scene = self.world.starting_location
        #self.player = self.game.create_player()

    def start_game(self):
        # Display a welcome message using Markdown and Pygments for syntax highlighting
        welcome_message = md.render('# Welcome to the Adventure Game!')
        highlighted_message = highlight(welcome_message, PythonLexer(), TerminalFormatter())
        console.print(highlighted_message)

        # Start the game loop
        while self.is_running:
            self.render_scene()
            self.process_input()

    def render_scene(self):
        # Render the current scene description and available actions
        #scene_description = self.current_scene.description
        #console.print(md.render(scene_description))
        console.print("Available actions:")
        #for action in self.current_scene.available_actions():
           # console.print(f"- {action}")

    def process_input(self):
        # Get player input and process it
        command = console.input("What do you want to do? ")
        if command.lower() == 'quit' or is_pressed('esc'):
            console.print("Goodbye!", style="bold red")
            self.is_running = False
        elif command:
            self.process_command(command)

    def process_command(self, command):
        # Process the player's command
        try:
            # Assume perform_action is a method that processes the command and returns the next scene
            self.current_scene = self.current_scene.perform_action(command, self.player)
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")

    # Additional methods for combat, dialogue, inventory, etc. can be added here

# The GameEngine class can now be imported into main.py to start the game
