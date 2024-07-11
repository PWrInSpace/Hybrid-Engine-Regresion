from abc import ABC, abstractmethod
import customtkinter
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AbstractSolver(ABC):
    Controller = None
    InputItemList = dict()
    InputLabelList = dict()
    InputValueList = dict()
    OutputItemList = dict()
    OutputValueList = dict()
    GraphItemList = []
    
    Figure = None
    Canvas = None

    def __init__(self, Controller):
        self.Controller = Controller
        self.Figure = plt.Figure()
        self.CreateCanvas()

    @abstractmethod
    def CreateInput(self):
        pass

    @abstractmethod
    def CreateOutput(self):
        pass

    @abstractmethod
    def CreateGrahps(self):
        pass

    @abstractmethod
    def ShowGraph(self, GraphName):
        pass

    @abstractmethod
    def RunSimulation(self):
        pass

    def AddInputItem(self, Item, rowNumber):
        Temp = None
        try:
            Temp = self.InputValueList[Item]
        except KeyError:
            self.InputValueList[Item] = None
            
        ScrollTempLabel = customtkinter.CTkLabel(self.Controller.InputFrame, text=Item) 
        ScrollTempLabel.grid(row=rowNumber, column=0, padx=10, pady=10, sticky="w")

        ScrollTempEntry = customtkinter.CTkEntry(self.Controller.InputFrame)
        ScrollTempEntry.insert(0, str(Temp)) 
        ScrollTempEntry.grid(row=rowNumber, column=1, padx=10, pady=10, sticky="w")

        self.InputLabelList[Item] = ScrollTempLabel
        self.InputItemList[Item] = ScrollTempEntry

    
    def DeleteInput(self):
        for item, entry in self.InputItemList.items():
            currentValue = entry.get()
            self.InputValueList[item] = currentValue
            entry.destroy()

        
        for item, label in self.InputLabelList.items():
            label.destroy()

    def AddOutput(self, Item, rowNumber):
        Temp = None
        try:
            Temp = self.OutputValueList[Item]
        except KeyError:
            self.OutputValueList[Item] = None

        ScrollTempLabel = customtkinter.CTkLabel(self.Controller.ScrollableFrameOutput, text=f"{Item}: {self.OutputValueList[Item]}") 
        ScrollTempLabel.grid(row=rowNumber, column=0, padx=10, pady=10, sticky="w")

        self.OutputItemList[Item] = ScrollTempLabel

    def AddPlot2D(self, x, y, name):
        self.ax = self.Figure.add_subplot(111)
        self.ax.plot(x, y, linestyle='-', marker='o')
        self.ax.set_title(name)

        self.Canvas.draw()
    
    def CreateCanvas(self): 
        self.Canvas = FigureCanvasTkAgg(self.Figure, master=self.Controller.graph_frame)
        self.Canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        self.Canvas.draw()

    def DeleteCanvas(self):
        self.Canvas.get_tk_widget().destroy()
