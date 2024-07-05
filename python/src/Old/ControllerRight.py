import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ControllerRight:
    def __init__(self, root, self_style):
        self.MainFrame = ttk.Frame(root, style="TFrame")
        self.style = self_style
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.MainFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.labels = [ttk.Label(self.MainFrame, text=f"Label {i}", style="TLabel") for i in range(6)]
        for label in self.labels:
            label.pack()
        self.MainFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)