# Game state tracking and variables

from entities.player import Player

class GameState:
    def __init__(self):
        self.player = Player()
        self.world = World()
        self.current_scene = None
