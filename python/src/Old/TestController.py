import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Controllers.ControllerRight import ControllerRight

class TestController:
    def __init__(self, frame, self_style):
        self.frame = ttk.Frame(frame, style="TFrame")
        self.combo_box = ttk.Combobox(self.frame)
        self.combo_box.pack()

        self.canvas = tk.Canvas(self.frame, bg="#333333")
        self.scrollable_frame = ttk.Frame(self.canvas, style="TFrame")

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Add 60 labels
        for i in range(60):
            label = ttk.Label(self.scrollable_frame, text=f"Label {i+1}", style="TLabel")
            label.pack()

        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)