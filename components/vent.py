from .base import Tile

class Vent(Tile):
    def __init__(self):
        super().__init__("Vent")
        self.color = "blue"
        self.heat_removal = 4

