from rich import print as rprint
from .locations import Location

# Scene management and transitions
class Scene:
    def __init__(self, description, interactions):
        self.description = description
        self.interactions = interactions  # This should be a dictionary of possible interactions

    def describe(self):
        return self.description

