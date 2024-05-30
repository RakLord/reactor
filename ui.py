import tkinter as tk
from tkinter import ttk
from components.fuel_rod import FuelRod
from components.vent import Vent
from components.exchanger import Exchanger

GRID_SIZE = 5
CELL_SIZE = 50

def create_left_frame(root, select_component_callback, save_callback, load_callback):
    left_frame = ttk.Frame(root, width=200)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    notebook = ttk.Notebook(left_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

    components_tab = ttk.Frame(notebook)
    upgrade_tab = ttk.Frame(notebook)
    settings_tab = ttk.Frame(notebook)

    notebook.add(components_tab, text="Components")
    notebook.add(upgrade_tab, text="Upgrades")
    notebook.add(settings_tab, text="Settings")

    fuel_rod_button = ttk.Button(components_tab, text="Select Fuel Rod", command=lambda: select_component_callback(FuelRod()))
    fuel_rod_button.pack(pady=5)

    vent_button = ttk.Button(components_tab, text="Select Vent", command=lambda: select_component_callback(Vent()))
    vent_button.pack(pady=5)

    exchanger_button = ttk.Button(components_tab, text="Select Exchanger", command=lambda: select_component_callback(Exchanger()))
    exchanger_button.pack(pady=5)

    save_button = ttk.Button(settings_tab, text="Save Game", command=save_callback)
    save_button.pack(pady=5)

    load_button = ttk.Button(settings_tab, text="Load Game", command=load_callback)
    load_button.pack(pady=5)

    return left_frame

def create_right_frame(root):
    right_frame = ttk.Frame(root, width=600)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(right_frame, width=GRID_SIZE * CELL_SIZE + 1, height=GRID_SIZE * CELL_SIZE + 1)
    canvas.pack()

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x0, y0 = i * CELL_SIZE, j * CELL_SIZE
            x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
            canvas.create_rectangle(x0, y0, x1, y1, outline="black")
    
    canvas.create_rectangle(1, 1, CELL_SIZE * GRID_SIZE, CELL_SIZE * GRID_SIZE, outline="black")
    return canvas

def create_display_frame(left_frame):
    display_frame = ttk.Frame(left_frame)
    display_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    display_canvas = tk.Canvas(display_frame, width=50, height=50)
    display_canvas.pack(side=tk.LEFT, padx=5)

    display_label = ttk.Label(display_frame, text="Empty")
    display_label.pack(side=tk.LEFT, padx=5)

    return display_canvas, display_label

