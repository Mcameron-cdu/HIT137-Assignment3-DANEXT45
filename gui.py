# gui.py
# This file sets up the Tkinter window and adds a basic label + button.

import tkinter as tk  # Tkinter is Python's built-in GUI library

class App:
    def __init__(self):
        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("HIT137 Assignment 3 - DANEXT45")  # Window title
        self.root.geometry("600x400")  # Set window size (width x height)

        # Add a label (text on screen)
        label = tk.Label(self.root, text="Hello from Tkinter!", font=("Arial", 16))
        label.pack(pady=20)  # Place it in the window with some padding

        # Add a Quit button to close the app
        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        quit_button.pack(pady=10)

    def run(self):
        # Start the Tkinter event loop (keeps the window open)
        self.root.mainloop()

