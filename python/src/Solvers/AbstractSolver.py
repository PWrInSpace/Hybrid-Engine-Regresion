from abc import ABC, abstractmethod
import customtkinter

from python.src.Controllers.Controller import Controller

class AbstractSolver(ABC):
    Controller = None
    InputItemList = dict()
    OutputItemList = []
    GraphItemList = []

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
        ScrollTempLabel = customtkinter.CTkLabel(self.scrollable_frame, text=Item) 
        ScrollTempLabel.grid(row=rowNumber, column=0, padx=10, pady=10, sticky="w")
        self.Controller.SidebarInputItemList.append(ScrollTempLabel)

        ScrollTempEntry = customtkinter.CTkEntry(self.scrollable_frame)
        ScrollTempEntry.grid(row=rowNumber, column=1, padx=10, pady=10, sticky="w")
        self.Controller.SidebarInputItemList.append(ScrollTempEntry)

        self.InputItemList[Item] = ScrollTempEntry