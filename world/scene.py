from rich import print as rprint

# Scene management and transitions

class Scene:
    def __init__(self, description, interactions):
        self.description = description
        self.interactions = interactions
