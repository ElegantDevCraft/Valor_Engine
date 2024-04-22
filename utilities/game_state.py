import os
import sys
from entities.player import Player

# Game state tracking and variables

class GameState:
    def __init__(self):
        self.player = Player()
        self.world = World()
        self.current_scene = None
