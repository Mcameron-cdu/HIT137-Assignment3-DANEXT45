# gui.py
# Tkinter GUI for the HIT137 Assignment 3

import tkinter as tk
from tkinter import filedialog, messagebox
from models import TextGenerator, ImageCaptioner


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HIT137 Assignment 3 - DANEXT45")
        self.root.geometry("850x600")

        # Dropdown to select model
        self.model_var = tk.StringVar(value="Text Generator")
        tk.Label(self.root, text="Select Model:", font=("Calibri", 12)).pack(pady=5)
        options = ["Text Generator", "Image Captioner"]
        self.model_menu = tk.OptionMenu(self.root, self.model_var, *options)
        self.model_menu.pack(pady=5)

        # Input area
        tk.Label(self.root, text="Input:", font=("Calibri", 12)).pack(pady=5)
        self.input_entry = tk.Entry(self.root, width=70)
        self.input_entry.pack(pady=5)

        # Browse button for image input
        self.browse_button = tk.Button(self.root, text="Browse Image", command=self.browse_file)
        self.browse_button.pack(pady=5)

        # Run button
        self.run_button = tk.Button(self.root, text="Run Model", command=self.run_model)
        self.run_button.pack(pady=10)

        # Output area
        tk.Label(self.root, text="Output:", font=("Calibri", 12)).pack(pady=5)
        self.output_text = tk.Text(self.root, height=10, width=90)
        self.output_text.pack(pady=5)

        # Model Info button
        self.info_button = tk.Button(self.root, text="Show Model Info", command=self.show_model_info)
        self.info_button.pack(pady=10)

        # OOP Explanation button
        self.explain_button = tk.Button(self.root, text="Show OOP Explanations", command=self.show_oop_explain)
        self.explain_button.pack(pady=10)
        
        # Show Logs Button
        self.logs_button = tk.Button(self.root, text="View Logs", command=self.show_logs)
        self.logs_button.pack(pady=10)

        # Quit button
        tk.Button(self.root, text="Quit", command=self.root.quit).pack(pady=10)

        # Load models at startup
        self.text_model = TextGenerator()
        self.text_model.load()
        self.image_model = ImageCaptioner()
        self.image_model.load()

    def browse_file(self):
        """Open a file dialog to select an image."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def run_model(self):
        """Run selected model with input data and show output."""
        choice = self.model_var.get()
        input_data = self.input_entry.get()

        if not input_data:
            messagebox.showwarning("Input Required", "Please enter text or select an image.")
            return

        if choice == "Text Generator":
            output = self.text_model.run(input_data)
        elif choice == "Image Captioner":
            output = self.image_model.run(input_data)
        else:
            output = "Invalid model choice."

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output)

    def show_model_info(self):
        """Display basic info about the selected model."""
        choice = self.model_var.get()
        if choice == "Text Generator":
            info = self.text_model.get_info()
        else:
            info = self.image_model.get_info()
        messagebox.showinfo("Model Info", info)

# Creates a file that stores each input into the models
    def show_logs(self):
        try:
            with open("model.log", "r", encoding="utf-8") as f:
                logs = f.read()
        except FileNotFoundError:
            logs = "No logs found. Use a model first to generate logs."

        log_window = tk.Toplevel(self.root)
        log_window.title("Model Logs")
        log_window.geometry("600x400")

        text_area = tk.Text(log_window, wrap="word")
        text_area.insert("1.0", logs)
        text_area.config(state="disabled")  # read-only
        text_area.pack(expand=True, fill="both")

        # Auto-scroll to bottom so newest logs are visible
        text_area.see("end")
        tk.Button(log_window, text="Close", command=log_window.destroy).pack(pady=5)

    def show_oop_explain(self):
        """Show explanations of OOP usage in this project."""
        explanation = (
            "Object-Oriented Programming concepts in this project:\n\n"
            "- Encapsulation: Model details (_task, _model_name, _pipeline) are private attributes.\n"
            "- Inheritance: BaseModel is inherited by TextGenerator and ImageCaptioner.\n"
            "- Method Overriding: The run() method is defined in BaseModel and overridden in each subclass.\n"
            "- Polymorphism: GUI can call run() on any model without knowing the implementation.\n"
            "- Multiple Inheritance & Decorators: LoggerMixin is combined with BaseModel to add logging to models.\n"
            "- Decorators: @ensure_loaded ensures a model is loaded before run() is executed." 
            )
        messagebox.showinfo("OOP Explanations", explanation)

    def run(self):
        self.root.mainloop()