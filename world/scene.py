# scene.py
from rich import print as rprint
from .locations import Location

# Scene management and transitions
class Scene(Location):
    def __init__(self, name, description, actions, interactions):
        super().__init__(name, description, actions)
        self.interactions = interactions

    def connect_scene(self, direction, scene):
        self.connected_locations[direction] = scene

    def describe(self):
        return f"{self.name}: {self.description}"
