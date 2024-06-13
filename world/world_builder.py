# world_builder.py
from world.scene import Scene
import json

def build_world(world_data):
    # Create a dictionary of Scene instances from the JSON data
    scenes = {}
    for loc_name, loc_data in world_data['locations'].items():
        # Instantiate Scene objects with name, description, actions, and interactions
        scenes[loc_name] = Scene(
            name=loc_name,
            description=loc_data['description'],
            actions=loc_data['actions'],
            interactions={}
        )

    # Connect scenes based on the JSON data
    for loc_name, loc_data in world_data['locations'].items():
        if 'directions' in loc_data:
            # Iterate through each direction that has an adjacent location
            for direction, adjacent_loc_name in loc_data['directions'].items():
                # Connect the current scene to the adjacent scene
                scenes[loc_name].connect_scene(direction, scenes[adjacent_loc_name])

    return scenes
