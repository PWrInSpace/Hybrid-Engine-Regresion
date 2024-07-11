from src.Solvers.AbstractSolver import AbstractSolver
import customtkinter # type: ignore


class Solver2(AbstractSolver):
    InputItemList = dict()

    def __init__(self, Controller):
        super().__init__(Controller)
    
        self.CreateInput()
        self.CreateOutput()

    def CreateInput(self):
        self.AddInputItem("K", 0)
        self.AddInputItem("Dupa", 1)
        print("Solver2.CreateInput")

    def CreateOutput(self):
        self.AddOutput("Skib", 0)

    def CreateGrahps(self):
        pass

    def ShowGraph(self, GraphName):
        pass

    def RunSimulation(self):
        self.AddPlot2D([1,2,3], [0, 1, 2], "Solver 2")
        print("Run() ok 2")
