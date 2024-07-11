from src.Solvers.AbstractSolver import AbstractSolver
import customtkinter # type: ignore


class Solver1(AbstractSolver):
    InputItemList = dict()

    def __init__(self, Controller):
        super().__init__(Controller)

        self.CreateInput()
        self.CreateOutput()

    def CreateInput(self):
        self.AddInputItem("Force", 0)
        print("Solver1.CreateInput")
    
    def CreateOutput(self):
        self.AddOutput("Impulse", 0)

    def CreateGrahps(self):
        pass

    def ShowGraph(self, GraphName):
        pass

    def RunSimulation(self):
        self.AddPlot2D([0, 1], [2, 2], "Plot Solver1")
        print("Run() ok")
