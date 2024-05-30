from .base import Tile

class Exchanger(Tile):
    def __init__(self):
        super().__init__("Exchanger")
        self.color = "yellow"

    def distribute_heat(self, grid, x, y):
        if grid[x][y] > 0:
            heat_to_distribute = grid[x][y]
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + i, y + j
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    grid[nx][ny] += heat_to_distribute // 4
            grid[x][y] -= heat_to_distribute

