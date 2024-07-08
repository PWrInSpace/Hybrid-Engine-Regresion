from abc import ABC, abstractmethod
import customtkinter


class AbstractSolver(ABC):
    Controller = None
    InputItemList = dict()
    InputValueList = dict()
    OutputItemList = dict()
    OutputValueList = dict()
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
        Temp = None
        try:
            Temp = self.InputValueList[Item]
        except KeyError:
            self.InputValueList[Item] = None
            
        ScrollTempLabel = customtkinter.CTkLabel(self.Controller.InputFrame, text=Item) 
        ScrollTempLabel.grid(row=rowNumber, column=0, padx=10, pady=10, sticky="w")

        ScrollTempEntry = customtkinter.CTkEntry(self.Controller.InputFrame, placeholder_text=Temp)
        ScrollTempEntry.grid(row=rowNumber, column=1, padx=10, pady=10, sticky="w")

        self.InputItemList[Item] = ScrollTempEntry

    
    def DeleteInput(self):
        for widget in self.InputItemList:
            widget.destroy()

    def AddOutput(self, Item, rowNumber):
        Temp = None
        try:
            Temp = self.OutputValueList[Item]
        except KeyError:
            self.OutputValueList[Item] = None


        ScrollTempLabel = customtkinter.CTkLabel(self.Controller.ScrollableFrameOutput, text=f"{Item}: {self.OutputValueList[Item]}") 
        ScrollTempLabel.grid(row=rowNumber, column=0, padx=10, pady=10, sticky="w")

        self.OutputItemList[Item] = ScrollTempLabel