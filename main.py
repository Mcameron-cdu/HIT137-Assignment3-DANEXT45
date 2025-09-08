# main.py
# This is the entry point of the program.
# It imports the GUI (from gui.py) and starts the app.

from gui import App  # Import the App class from gui.py

if __name__ == "__main__":
    app = App()   # Create an instance of the App class
    app.run()     # Run the Tkinter GUI loop
