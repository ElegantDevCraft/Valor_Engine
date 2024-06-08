import os
import sys
from entities.player import Player
from world.locations import SomeLocation
from world.scene import Scene
from world.world_builder import build_world

# Game state tracking and variables

class GameState:
    def __init__(self):
        self.player = Player()
        self.world = build_world()
        self.current_scene = Scene(self.world)
