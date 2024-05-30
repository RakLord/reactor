from .base import Tile

class FuelRod(Tile):
    def __init__(self):
        super().__init__("Fuel Rod")
        self.color = "green"
        self.heat_generation = 1

