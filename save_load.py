import json
from components.fuel_rod import FuelRod
from components.vent import Vent
from components.exchanger import Exchanger

def save_game(grid, components, selected_component, filename="savefile.json"):
    save_data = {
        "grid": grid,
        "components": [[component.__class__.__name__ if component else None for component in row] for row in components],
        "selected_component": selected_component.__class__.__name__
    }
    with open(filename, "w") as f:
        json.dump(save_data, f)

def load_game(filename="savefile.json"):
    with open(filename, "r") as f:
        save_data = json.load(f)
    
    grid = save_data["grid"]
    components = [[create_component(name) for name in row] for row in save_data["components"]]
    selected_component = create_component(save_data["selected_component"])
    return grid, components, selected_component

def create_component(name):
    if name == "FuelRod":
        return FuelRod()
    elif name == "Vent":
        return Vent()
    elif name == "Exchanger":
        return Exchanger()
    else:
        return None

