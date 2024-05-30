import tkinter as tk
from game import ReactorGame

if __name__ == "__main__":
    root = tk.Tk()
    game = ReactorGame(root)
    game.game_loop()
    root.mainloop()

