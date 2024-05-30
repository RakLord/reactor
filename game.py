import tkinter as tk
from tkinter import ttk
from components.fuel_rod import FuelRod
from components.vent import Vent
from components.exchanger import Exchanger
from save_load import save_game, load_game
from ui import create_left_frame, create_right_frame, create_display_frame

GRID_SIZE = 5
CELL_SIZE = 50

class ReactorGame:
    def __init__(self, root):
        self.root = root
        self.heat_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.components = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected_component = None
        self.setup_ui()
        self.bind_hotkeys()

    def setup_ui(self):
        self.root.title("Reactor Game")
        self.root.geometry("800x600")

        self.left_frame = create_left_frame(self.root, self.select_component, self.save, self.load)
        self.canvas = create_right_frame(self.root)
        self.display_canvas, self.display_label = create_display_frame(self.left_frame)

        self.canvas.bind("<Button-1>", self.place_component)

    def bind_hotkeys(self):
        self.root.bind("<Control-s>", lambda event: self.save())
        self.root.bind("<Control-l>", lambda event: self.load())

    def select_component(self, component):
        self.selected_component = component
        self.update_display()

    def update_display(self):
        self.display_canvas.delete("all")
        if self.selected_component:
            self.display_canvas.create_rectangle(0, 0, 50, 50, fill=self.selected_component.color)
            self.display_label.config(text=self.selected_component.name)
        else:
            self.display_label.config(text="Empty")

    def place_component(self, event):
        x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and self.selected_component:
            self.components[x][y] = self.selected_component
            self.update_grid()

    def update_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):

                x, y = i * CELL_SIZE, j * CELL_SIZE
                if isinstance(self.components[i][j], FuelRod):
                    self.heat_grid[i][j] += self.components[i][j].heat_generation
                    self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=self.components[i][j].color )

                elif isinstance(self.components[i][j], Vent):
                    self.heat_grid[i][j] = max(0, self.heat_grid[i][j] - self.components[i][j].heat_removal)
                    self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=self.components[i][j].color )

                elif isinstance(self.components[i][j], Exchanger):
                    self.components[i][j].distribute_heat(self.heat_grid, i, j)
                    self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=self.components[i][j].color )

        self.draw_heat()

    def draw_heat(self):
        self.canvas.delete("heat")
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x0, y0 = i * CELL_SIZE, j * CELL_SIZE
                x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
                heat = self.heat_grid[i][j]
                if heat > 0:
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(heat), tags="heat")

    def game_loop(self):
        self.update_grid()
        self.root.after(1000, self.game_loop)

    def save(self):
        save_game(self.heat_grid, self.components, self.selected_component)

    def load(self):
        self.heat_grid, self.components, self.selected_component = load_game()
        self.update_grid()
        self.update_display()

