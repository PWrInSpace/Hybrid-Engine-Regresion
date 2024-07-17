from src.Solvers.AbstractSolver import AbstractSolver
import customtkinter # type: ignore


class Solver1(AbstractSolver):
    InputItemList = dict()

    def __init__(self, Controller):
        super().__init__(Controller)

        self.CreateInput()
        self.CreateOutput()
        self.CreateCheckboxFrame()

    def CreateInput(self):
        self.AddInputItem("Force", 0)
        print("Solver1.CreateInput")
    
    def CreateOutput(self):
        self.AddOutput("Impulse", 0)

    def CreateGrahps(self):
        pass

    def ShowGraph(self, GraphName):
        pass

    def CreateCheckboxFrame(self):
        self.AddCheckbox("Check 1", 0)
        self.AddCheckbox("Skibdib", 1)

    def RunSimulation(self):
        self.AddPlot2D([0, 1], [2, 2], "Check 1", "Example graph", 'orange')
        self.AddPlot2D([0, 2], [3, 3], "Skibdib", "Example graph", 'green')
        print("Run() ok")
