import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Controllers.ControllerRight import ControllerRight

class ControllerLeft:
    def __init__(self, MainFrame, self_style):
        self.MainFrame = ttk.Frame(MainFrame, style="TFrame")

        self.SolverFrame = ttk.Frame(self.MainFrame, style="TFrame")
        self.SolverFrame.pack(side="top", fill="both", expand=True)

        self.label = ttk.Label(self.SolverFrame, text="Label", style="TLabel")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.combo_box = ttk.Combobox(self.SolverFrame)
        self.combo_box.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.listbox = tk.Listbox(self.SolverFrame)
        self.listbox.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Add items to the listbox
        items = ["Item 1", "Item 2", "Item 3"]
        for item in items:
            self.listbox.insert(tk.END, item)

        self.AttributesFrame = ttk.Frame(self.MainFrame, style="TFrame")
        self.AttributesFrame.pack(side="bottom", fill="both", expand=True)

        self.canvas = tk.Canvas(self.AttributesFrame, bg="#333333")
        self.ScrollFrame = ttk.Frame(self.canvas, style="TFrame")

        self.scrollbar = ttk.Scrollbar(self.AttributesFrame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.create_window((0, 0), window=self.ScrollFrame, anchor="nw")

        self.ScrollFrame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Add 60 labels
        for i in range(60):
            label = ttk.Label(self.ScrollFrame, text=f"Label {i+1}", style="TLabel")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            input_box = ttk.Entry(self.ScrollFrame)
            input_box.grid(row=i, column=1, padx=10, pady=10, sticky="w")

        self.MainFrame.pack(side="left", fill="both", expand=True)