import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Controllers.ControllerLeft import ControllerLeft
from Controllers.ControllerRight import ControllerRight

class Controller:
    def __init__(self):
        self.root = tk.Tk()

        self.root.wm_attributes('-zoomed', 1)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#333333")
        self.style.configure("TLabel", background="#333333", foreground="#ffffff")
        self.style.configure("TCombobox", fieldbackground="#333333", background="#333333", foreground="#ffffff")


        self.paned_window = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)

        self.frame1 = ttk.Frame(self.paned_window, style="TFrame")
        self.paned_window.add(self.frame1)

        self.test_controller = ControllerLeft(self.frame1, self.style)

        # Add another frame to the paned window
        self.frame2 = ttk.Frame(self.paned_window, style="TFrame")
        self.paned_window.add(self.frame2)

        # Create an instance of ControllerRight and add it to frame2
        self.controller_right = ControllerRight(self.frame2, self.style)

        self.paned_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)





    def run(self):
        self.root.mainloop()

